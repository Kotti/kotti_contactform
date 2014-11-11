import colander
from deform import Button
from deform import FileData
from deform import Form
from deform import ValidationFailure
from deform.widget import FileUploadWidget
from deform.widget import HiddenWidget
from deform.widget import RichTextWidget
from deform.widget import TextAreaWidget
from kotti import get_settings
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from kotti.views.form import FileUploadTempStore
from kotti.views.util import template_api
from kotti_settings.util import get_setting
from pyramid.i18n import get_locale_name
from pyramid.view import view_config
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Attachment
from pyramid_mailer.message import Message

from kotti_contactform import _
from kotti_contactform.resources import ContactForm
from kotti_contactform.widgets import deferred_recaptcha_widget


@colander.deferred
def deferred_default_sender(node, kw):
    sender = kw.get('sender')
    if not sender:
        sender = get_setting(
            'default_sender',
            get_settings().get('mail.default_sender', ''))
    return sender


class ContactFormSchema(ContentSchema):

    sender = colander.SchemaNode(
        colander.String(),
        missing=deferred_default_sender,
        default=deferred_default_sender)
    recipient = colander.SchemaNode(colander.String())
    body = colander.SchemaNode(
        colander.String(),
        widget=RichTextWidget(theme='advanced', width=790, height=500),
        missing=u"",
    )
    show_attachment = colander.SchemaNode(
        colander.Boolean(),
        title=_(u"Show attachment"),
        description=_(u"If activated, the user can upload an attachment."),
        default=True,
        missing=True,
    )


@view_config(name=ContactForm.type_info.add_view,
             permission='add',
             renderer='kotti:templates/edit/node.pt')
class ContactformAddForm(AddFormView):
    schema_factory = ContactFormSchema
    add = ContactForm
    item_type = _(u"Contact Form")


@view_config(name='edit',
             context=ContactForm, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class ContactformEditForm(EditFormView):

    schema_factory = ContactFormSchema


def mail_submission(context, request, appstruct):
    mailer = get_mailer(request)
    message = Message(
        subject=appstruct['subject'],
        sender='{name} <{email}>'.format(
            name=appstruct['name'],
            email=context.sender),
        extra_headers={
            'X-Mailer': "kotti_contactform",
            'Reply-To': '{name} <{sender}>'.format(**appstruct),
        },
        recipients=[context.recipient],
        body=appstruct['content'])
    if 'attachment' in appstruct and appstruct['attachment'] is not None:
        message.attach(Attachment(
            filename=appstruct['attachment']['filename'],
            content_type=appstruct['attachment']['mimetype'],
            data=appstruct['attachment']['fp']
        ))
    mailer.send(message)


@view_config(name='view',
             context=ContactForm,
             permission='view',
             renderer='kotti_contactform:templates/contactform-view-two-columns.pt')  # noqa
@view_config(name='view-1-col',
             context=ContactForm,
             permission='view',
             renderer='kotti_contactform:templates/contactform-view-one-column.pt')  # noqa
def view_contactform(context, request):

    locale_name = get_locale_name(request)

    tmpstore = FileUploadTempStore(request)

    def file_size_limit(node, value):
        value['fp'].seek(0, 2)
        size = value['fp'].tell()
        value['fp'].seek(0)
        max_size = 10
        if size > max_size * 1024 * 1024:
            msg = _('Maximum file size: ${size}MB', mapping={'size': max_size})
            raise colander.Invalid(node, msg)

    def maybe_show(node, kw):
        if kw.get('show_attachment', True) is False:
            del node['attachment']
        if kw.get('show_captcha', False) is False:
            del node['captcha']

    class SubmissionSchema(colander.MappingSchema):

        name = colander.SchemaNode(colander.String(),
                                   title=_("Full Name"))
        sender = colander.SchemaNode(colander.String(),
                                     validator=colander.Email(),
                                     title=_("E-Mail Address"))
        subject = colander.SchemaNode(colander.String(), title=_("Subject"))
        content = colander.SchemaNode(
            colander.String(),
            widget=TextAreaWidget(cols=40, rows=5),
            title=_("Your message")
        )
        attachment = colander.SchemaNode(
            FileData(),
            title=_('Attachment'),
            widget=FileUploadWidget(tmpstore),
            validator=file_size_limit,
            missing=None,
        )
        captcha = colander.SchemaNode(
            colander.String(),
            title=_('Captcha'),
            widget=deferred_recaptcha_widget
        )
        _LOCALE_ = colander.SchemaNode(
            colander.String(),
            widget=HiddenWidget(),
            default=locale_name)

    schema = SubmissionSchema(after_bind=maybe_show)
    schema = schema.bind(show_attachment=context.show_attachment,
                         show_captcha=get_setting('show_captcha', False),
                         request=request)
    form = Form(schema, buttons=[Button('submit', _('Submit'))])
    appstruct = None
    rendered_form = None
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except ValidationFailure, e:
            appstruct = None
            rendered_form = e.render()
        else:
            mail_submission(context, request, appstruct)
            request.session.flash(_('Thanks for your submission!'), 'success')
    else:
        rendered_form = form.render()
    return {
        'form': rendered_form,
        'appstruct': appstruct,
        'use_captcha': get_setting('use_captcha'),
        'api': template_api(context, request),
    }
