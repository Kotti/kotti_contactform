import colander
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

def view_contactform(context, request):
    return {
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

def includeme(config):
    includeme_edit(config)
    includeme_view(config)
