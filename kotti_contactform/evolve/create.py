def create(connection):
    """Create the latest version of the schema. This function should be
    idempotent and can be usefully called more than once per database
    for development, but stucco_evolution tries to call this only once
    in production."""
    from kotti import Base
    Base.metadata.create_all(connection)
