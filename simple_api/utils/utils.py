from logging import getLogger
from sqlite3 import OperationalError

from datetime import datetime, UTC
from flask import flash, g, render_template, request

from simple_api.db import get_db
from simple_api.utils.item_info import ITEM_INFO


LOGGER = getLogger("utils")


def collect_item(item_id: str):
    """Collect an item if the user hasn't already."""

    db = get_db()
    owner_items = db.execute(
        f"SELECT * FROM item WHERE owner={g.user['id']};"
    ).fetchall()
    for item in owner_items:
        if item["id"] == item_id:
            flash("You already have this item!")
            return
    ineligible_items = db.execute(
        f"SELECT * FROM item WHERE id='{item_id}';"
    ).fetchone()
    if ineligible_items["owner"] and ineligible_items["owner"] != g.user["id"]:
        flash("This item has already been collected!")
        return
    db.execute(f"UPDATE item SET owner={g.user['id']}, found_time='{datetime.now(UTC)}' WHERE id='{item_id}';")
    db.commit()


def dynamic_item_handler(item_id: str):
    if request.method == "POST":
        collect_item(item_id)

    db = get_db()
    item_details = db.execute(f"SELECT * FROM item WHERE id='{item_id}';").fetchone()

    return render_template("item/item_preview.html", item_details=item_details)


def seed_database():
    """Seed the database with `item` data."""

    items = [(item["id"], item["name"], item["description"], item["image_path"]) for item in ITEM_INFO]

    db = get_db()
    db.executemany("insert into item (id, name, description, image_path) values (?, ?, ?, ?)""", items)
    db.commit()
