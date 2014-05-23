import colander
import deform

from kotti_settings.util import add_settings
from kotti_contactform import _


class ShowCaptchaSchemaNode(colander.SchemaNode):
    name = 'show_captcha'
    title = _(u'Show captcha')
    description = _(u'Use a reCaptcha in your contact forms.')
    missing = False
    default = False


class PublicKeySchemaNode(colander.SchemaNode):
    name = 'public_key'
    title = _(u'Public key')
    description = _(u'Your public key.')
    missing = u''
    default = u''


class PrivateKeySchemaNode(colander.SchemaNode):
    name = 'private_key'
    title = _(u'Private key')
    description = _(u'Your private key.')
    missing = u''
    default = u''


recaptcha_themes = ((u'red', _(u'Red')),
                    (u'white', _(u'White')),
                    (u'blackglass', _(u'Blackglass')),
                    (u'clean', _(u'Clean')))


class RecaptchaThemeSchemaNode(colander.SchemaNode):
    name = 'recaptcha_theme'
    title = _(u'reCaptcha theme')
    default = u'red'
    widget = deform.widget.SelectWidget(values=recaptcha_themes)


class ContactFormSchema(colander.MappingSchema):
    show_captcha = ShowCaptchaSchemaNode(colander.Boolean())
    public_key = PublicKeySchemaNode(colander.String())
    private_key = PrivateKeySchemaNode(colander.String())
    recaptcha_theme = RecaptchaThemeSchemaNode(colander.String())


ContactFormSettings = {
    'name': 'contactform_settings',
    'title': _(u'Contact form settings'),
    'description': _(u"Settings for kotti_contactform"),
    'success_message': _(u"Successfully saved kotti_contactform settings."),
    'schema_factory': ContactFormSchema,
}


def populate():
    add_settings(ContactFormSettings)
