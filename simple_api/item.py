from datetime import datetime, UTC

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from simple_api.auth import login_required
from simple_api.db import get_db
from simple_api.utils import utils

bp = Blueprint('item', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    items = db.execute(
        'SELECT id, name, description, image_path, used'
        ' FROM item'
        f" WHERE owner={g.user['id']};"
    ).fetchall()
    return render_template('item/index.html', items=items)


@bp.route("/debf4cb9-0827-4abc-adc3-0454db181b8e", methods=('GET', 'POST'))
@bp.route("/1049a98e-3d9e-475a-8869-b2b3bc5c0d60", methods=('GET', 'POST'))
@bp.route("/d988fa83-fbf8-4c78-8742-cf04447892a6", methods=('GET', 'POST'))
@bp.route("/7d5fc1ed-edd3-42c7-a36a-66a7df419d6e", methods=('GET', 'POST'))
@bp.route("/ee2f5f28-8bb3-4108-89ea-5e3874325fcf", methods=('GET', 'POST'))
@login_required
def one_up():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/a2d1a056-9e2b-41d9-888d-e80234e2b860", methods=('GET', 'POST'))
@bp.route("/b5662985-2ca1-4829-b7ae-65a6c880a130", methods=('GET', 'POST'))
@bp.route("/8c479beb-a901-49ec-b995-0de0f0939772", methods=('GET', 'POST'))
@bp.route("/615e615e-d7ba-408f-b901-afcb6248ac0b", methods=('GET', 'POST'))
@bp.route("/47f9eb6a-f862-45f5-beee-b3b695e70b34", methods=('GET', 'POST'))
@login_required
def bomb():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/d66bc0ba-fd70-47ac-be24-5f3676ec53d3", methods=('GET', 'POST'))
@login_required
def boo():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/1aec4b0f-57c5-4e1d-b0e4-ec66322a3b62", methods=('GET', 'POST'))
@login_required
def duel():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/36819a73-8b40-432f-9421-89d75b216205", methods=('GET', 'POST'))
@login_required
def fludd():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/35a34cbe-7d24-4e9a-adae-fcdcd5e0c083", methods=('GET', 'POST'))
@login_required
def boss_key():

    item_id = "35a34cbe-7d24-4e9a-adae-fcdcd5e0c083"
    if request.method == "POST":
        collect_item(item_id)

    db = get_db()
    item_details = db.execute(f"SELECT * FROM item WHERE id='{item_id}';").fetchone()

    return render_template("item/item_preview.html", item_details=item_details)


@bp.route("/use", methods=('POST',))
@login_required
def use():
    item_id = request.form.get("button_id")
    db = get_db()
    print(item_id)
    items = db.execute(
        f"SELECT * FROM item WHERE id='{item_id}' and owner={g.user['id']};"
    ).fetchall()
    for item in items:
        if item["used"] == 1:
            flash("This item has already been used.")
        else:
            db.execute(f"UPDATE item SET used=1 WHERE id='{item_id}';")
            db.commit()
    display_items = db.execute(
        f"SELECT * FROM item WHERE owner={g.user['id']};"
    ).fetchall()
    return render_template("item/index.html", items=display_items)


def collect_item(item_id: str):
    """Collect an item if the user hasn't already."""

    print(item_id)
    db = get_db()
    owner_items = db.execute(
        f"SELECT * FROM item WHERE owner={g.user['id']};"
    ).fetchall()
    for item in owner_items:
        if item["id"] == item_id:
            flash("You already have this item!")
            return
    db.execute(f"UPDATE item SET owner={g.user['id']}, found='{datetime.now(UTC)}' WHERE id='{item_id}';")
    db.commit()
