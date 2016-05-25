from deform import Form
from pkg_resources import resource_filename
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_contactform')


def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_contactform'
    settings['kotti.available_types'] += (
        ' kotti_contactform.resources.ContactForm'
    )
    settings['kotti.alembic_dirs'] += ' kotti_contactform:alembic'
    settings['kotti.populators'] += ' kotti_contactform.populate.populate'


def add_search_path():
    loader = Form.default_renderer.loader
    try:
        path = resource_filename('kotti_contactform', 'templates')
    except ImportError:
        # On Google AppEngine resource_filename() uses os.path.expanduser()
        # which uses pwd which isn't available, so we work around that mess:
        from os.path import dirname, join
        path = join(dirname(__file__), 'templates')
    loader.search_path = (path,) + loader.search_path


def includeme(config):
    add_search_path()
    config.include('pyramid_mailer')
    config.add_translation_dirs('kotti_contactform:locale')
    config.add_static_view('static-kotti_contactform',
                           'kotti_contactform:static')
    config.scan()

    settings = config.get_settings()
    if settings.get('kotti_contactform.asset_overrides') is not None:
        for override in [a.strip()
                         for a in settings['kotti_contactform.asset_overrides'].split()
                         if a.strip()]:
            config.override_asset(to_override='kotti_contactform', override_with=override)
