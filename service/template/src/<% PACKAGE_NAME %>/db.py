"""The database connection, configured by DATABASE_URL."""

import os

from sqlalchemy import Engine, create_engine


def engine() -> Engine:
    """Create an engine for the database DATABASE_URL names."""
    return create_engine(os.environ["DATABASE_URL"])
