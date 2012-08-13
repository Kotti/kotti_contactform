def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_contactform.views'
    settings['kotti.available_types'] += (
        ' kotti_contactform.resources.ContactForm'
    )
    settings['kotti.alembic_dirs'] += ' kotti_contactform:alembic'
