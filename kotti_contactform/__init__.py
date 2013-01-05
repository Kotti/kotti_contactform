from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_contactform')


def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_contactform'
    settings['kotti.available_types'] += (
        ' kotti_contactform.resources.ContactForm'
    )
    settings['kotti.alembic_dirs'] += ' kotti_contactform:alembic'


def includeme(config):
    config.include('pyramid_mailer')
    config.add_translation_dirs('kotti_contactform:locale')
    config.add_static_view('static-kotti_contactform',
                           'kotti_contactform:static')
    config.scan()
