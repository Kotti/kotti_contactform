import sqlalchemy
import stucco_evolution


def kotti_configure(settings):
    settings['kotti.includes'] += ' kotti_contactform.views'
    settings['kotti.available_types'] += ' kotti_contactform.resources.ContactForm'

    # database migration
    import kotti_contactform
    engine = sqlalchemy.engine_from_config(settings, 'sqlalchemy.')

    with engine.begin() as connection:  # engine.begin() since SQLAlchemy 0.7.6
        stucco_evolution.initialize(connection)
        # j23d, 20120626
        # first create the stucco_evolution table in the database
        stucco_evolution.create_or_upgrade_packages(connection, 'kotti_contactform')
        # then update the version so our the upgrade script perform actually
        # Is there are a more convenient way to do this?
        kotti_contactform.evolve.VERSION = 1
        stucco_evolution.create_or_upgrade_packages(connection, 'kotti_contactform')
