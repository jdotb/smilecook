import app
import click
from flask.cli import with_appcontext
from config.Config import DB_URL
from extensions import db

# app.Config['SQLALCHEMY_DATABASE_URI'] = DB_URL


@click.command(name='resetdb')
@with_appcontext
def resetdb_command():
    from sqlalchemy_utils import database_exists, drop_database, create_database
    """Destroys and creates the database + tables."""

    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')