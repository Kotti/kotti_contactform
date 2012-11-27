import colander
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Attachment
from pyramid_mailer.message import Message
from pyramid.i18n import TranslationStringFactory
_ = TranslationStringFactory('kotti_contactform')
from pyramid.i18n import get_locale_name
from deform.widget import RichTextWidget
from deform.widget import TextAreaWidget
from deform.widget import HiddenWidget
from deform import Form
from deform import FileData
from deform import Button
from deform import ValidationFailure
from deform.widget import FileUploadWidget
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from kotti.views.util import template_api
from kotti.views.form import FileUploadTempStore
from kotti_contactform.resources import ContactForm


class ContactFormSchema(ContentSchema):
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


class ContactformEditForm(EditFormView):
    schema_factory = ContactFormSchema


class ContactformAddForm(AddFormView):
    schema_factory = ContactFormSchema
    add = ContactForm
    item_type = _(u"Contact Form")


def mail_submission(context, request, appstruct):
    mailer = get_mailer(request)
    message = Message(subject=appstruct['subject'],
                      sender=appstruct['name'] + ' <'
                      + appstruct['sender'] + '>',
                      extra_headers={'X-Mailer': "kotti_contactform"},
                      recipients=[context.recipient],
                      body=appstruct['content'])
    if 'attachment' in appstruct and appstruct['attachment'] is not None:
        message.attach(Attachment(
            filename=appstruct['attachment']['filename'],
            content_type=appstruct['attachment']['mimetype'],
            data=appstruct['attachment']['fp']
        ))
    mailer.send(message)


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

    def maybe_show_attachment(node, kw):
        if kw.get('maybe_show_attachment', True) is False:
            del node['attachment']

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
        _LOCALE_ = colander.SchemaNode(
            colander.String(),
            widget=HiddenWidget(),
            default=locale_name)

    schema = SubmissionSchema(after_bind=maybe_show_attachment)
    schema = schema.bind(maybe_show_attachment=context.show_attachment)
    form = Form(schema, buttons=[Button('submit', _('Submit'))])
    appstruct = None
    rendered_form = None
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
            mail_submission(context, request, appstruct)
        except ValidationFailure, e:
            appstruct = None
            rendered_form = e.render()
    else:
        rendered_form = form.render()
    return {
        'form': rendered_form,
        'appstruct': appstruct,
        'api': template_api(context, request),
    }


def includeme_edit(config):
    config.add_view(
        ContactformEditForm,
        context=ContactForm,
        name='edit',
        permission='edit',
        renderer='kotti:templates/edit/node.pt',
    )

    config.add_view(
        ContactformAddForm,
        name=ContactForm.type_info.add_view,
        permission='add',
        renderer='kotti:templates/edit/node.pt',
    )


def includeme_view(config):
    config.add_view(
        view_contactform,
        context=ContactForm,
        name='view',
        permission='view',
        renderer='templates/contactform-view.pt',
    )
    config.add_static_view('static-kotti_contactform',
                           'kotti_contactform:static')
#   config.add_static_view('static', 'deform:static')


def includeme(config):
    config.include('pyramid_mailer')
    includeme_edit(config)
    includeme_view(config)
    config.add_translation_dirs('kotti_contactform:locale/',
                                # last two should get included by kotti
                                'colander:locale',
                                'deform:locale',
                                )
