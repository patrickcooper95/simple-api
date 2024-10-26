import sqlite3

import click
from flask import current_app, g

from simple_api.utils.item_info import ITEM_INFO


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def seed_db():
    """Seed the database with `item` data."""
    items = [(item["id"], item["name"], item["description"], item["image_path"]) for item in ITEM_INFO]

    db = get_db()
    db.executemany("insert into item (id, name, description, image_path) values (?, ?, ?, ?)""", items)
    db.commit()


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


@click.command('seed-db')
def seed_db_command():
    seed_db()
    click.echo("Seeded item data.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(seed_db_command)
