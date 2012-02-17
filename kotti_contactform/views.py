import colander
from pyramid_mailer import get_mailer
from pyramid_mailer.message import Message
from deform import Form
from deform import ValidationFailure
from kotti.views.edit import ContentSchema
from kotti.views.edit import generic_edit
from kotti.views.edit import generic_add
from kotti.views.util import ensure_view_selector
from kotti.views.util import template_api

from kotti_contactform.resources import ContactForm

class ContactFormSchema(ContentSchema):
    recipient = colander.SchemaNode(colander.String())

@ensure_view_selector
def edit_contactform(context, request):
    return generic_edit(context, request, ContactFormSchema())

def add_contactform(context, request):
    return generic_add(context, request, ContactFormSchema(), ContactForm, u'contactform')


class SubmissionSchema(colander.MappingSchema):
    sender = colander.SchemaNode(colander.String(), validator=colander.Email())
    subject = colander.SchemaNode(colander.String())
    content = colander.SchemaNode(colander.String())

def mail_submission(context, request, appstruct):
    mailer = get_mailer(request)
    message = Message(subject=appstruct.subject,
                      sender=appstruct.sender,
                      recipients=[context.recipient],
                      body=appstruct.content)
    mailer.send(message)

def view_contactform(context, request):
    schema = SubmissionSchema()
    form = Form(schema, buttons=('submit',))
    appstruct = None
    rendered_form = None
    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
        except ValidationFailure, e:
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
        edit_contactform,
        context=ContactForm,
        name='edit',
        permission='edit',
        renderer='kotti:templates/edit/node.pt',
        )

    config.add_view(
        add_contactform,
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
    config.add_static_view('static-kotti_contactform', 'kotti_contactform:static')
#   config.add_static_view('static', 'deform:static')

def includeme(config):
    config.include('pyramid_mailer')
    includeme_edit(config)
    includeme_view(config)
