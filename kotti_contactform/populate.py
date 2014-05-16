from kotti_settings.util import add_settings
from kotti_contactform import _

recaptcha_themes = ['red', 'white', 'blackglass', 'clean']


ContactFormSettings = {
    'name': 'contactform_settings',
    'title': _(u'Contact form settings'),
    'description': _(u"Settings for kotti_contactform"),
    'success_message': _(u"Successfully saved kotti_contactform settings."),
    'settings': [
        {'type': 'Bool',
         'name': 'show_captcha',
         'title': _(u'Show captcha'),
         'description': _(u'Use a reCaptcha in your contact forms.'),
         'default': False, },
        {'type': 'String',
         'name': 'public_key',
         'title': _(u'Public key'),
         'description': _(u'Your public API key.'),
         'default': '', },
        {'type': 'String',
         'name': 'private_key',
         'title': _(u'Private key'),
         'description': _(u'Your privat API key.'),
         'default': '', },
    ]
}


def populate():
    add_settings(ContactFormSettings)
