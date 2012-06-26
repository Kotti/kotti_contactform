import pytest


@pytest.mark.skip
def evolve(connection):
    """Execute any ALTER TABLE etc. statements needed to bring the
    database up-to-date (upgrade the schema from VERSION n-1 to VERSION n.)"""
    # condition to not let the upgrade be performed for the tests
    if connection.engine.url.database is not None:
        connection.execute("ALTER TABLE contact_forms ADD COLUMN show_attachment BOOLEAN NOT NULL DEFAULT true")  # pragma: no cover
