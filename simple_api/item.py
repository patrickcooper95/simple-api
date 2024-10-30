from datetime import datetime, UTC

from flask import (
    Blueprint, abort, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from simple_api.auth import login_required
from simple_api.db import get_db
from simple_api.utils import utils
from simple_api.utils.item_info import ITEM_INFO

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


@bp.route("/admin")
@login_required
def admin():
    db = get_db()
    items = db.execute(
        "SELECT i.id, i.name, i.description, i.image_path, i.found_time, i.used, i.used_time, u.username as owner_name"
        " FROM item i LEFT JOIN user u on owner = u.id;"
    ).fetchall()
    if g.user["admin"]:
        return render_template("item/admin.html", items=items)
    else:
        # Don't let the user see this page if they're not admin
        abort(404)


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
@login_required
def bomb():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/d66bc0ba-fd70-47ac-be24-5f3676ec53d3", methods=("GET", "POST"))
@bp.route("/c5f6624e-d8e2-4988-9c7a-2403ae62702c", methods=("GET", "POST"))
@bp.route("/615e615e-d7ba-408f-b901-afcb6248ac0b", methods=("GET", "POST"))
@bp.route("/47f9eb6a-f862-45f5-beee-b3b695e70b34", methods=("GET", "POST"))
@login_required
def boo():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/1aec4b0f-57c5-4e1d-b0e4-ec66322a3b62", methods=('GET', 'POST'))
@bp.route("/343a4135-21ed-4a8f-aba0-a05c87065fed", methods=("GET", "POST"))
@bp.route("/c7a49043-c3c0-4732-82bf-b60779d9feae", methods=("GET", "POST"))
@bp.route("/386d5588-9a17-426f-9a4f-defe0fec83bd", methods=("GET", "POST"))
@bp.route("/4e407b2c-209a-4198-a274-a10045b4a353", methods=("GET", "POST"))
@bp.route("/9f905027-e05b-4f8c-bad6-a355eb032539", methods=("GET", "POST"))
@bp.route("/755fe9dc-6585-4eb6-a702-d1ebe8714692", methods=("GET", "POST"))
@bp.route("/737b5b0e-f10f-473a-937b-3d1d5d2d5a7f", methods=("GET", "POST"))
@login_required
def duel():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/36819a73-8b40-432f-9421-89d75b216205", methods=('GET', 'POST'))
@bp.route("/ab20ccdc-1062-4d1f-9278-00ba3071c527", methods=('GET', 'POST'))
@bp.route("/d0bbd9d3-39ea-4077-aca5-93f5ba3e0763", methods=('GET', 'POST'))
@bp.route("/f928cc0c-831b-488e-815c-3e7fe26b9db2", methods=('GET', 'POST'))
@bp.route("/54c8b161-cf0e-4fac-9733-66dbb665ec60", methods=('GET', 'POST'))
@bp.route("/b92f467c-8b0c-441e-8a71-675cf99dd761", methods=('GET', 'POST'))
@bp.route("/35e4aea2-0dca-4dcb-8ce8-ab161b5a3b77", methods=('GET', 'POST'))
@login_required
def fludd():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/a090c6a6-d36d-4da9-a7b0-c1cd4175f4e4", methods=('GET', 'POST'))
@bp.route("/1e002ec0-bff2-40bf-9a69-769e3cd45edb", methods=('GET', 'POST'))
@bp.route("/8d229ba6-7b17-43f3-b843-c1ebe44e3dcb", methods=('GET', 'POST'))
@bp.route("/e0faf21a-f510-4f8f-828e-d451ad0fd762", methods=('GET', 'POST'))
@bp.route("/f6d646a6-a760-4e4a-a465-9bb9206b98e3", methods=('GET', 'POST'))
@bp.route("/680b15e2-4489-4161-98bc-51e3ba99457f", methods=('GET', 'POST'))
@bp.route("/dbf464c7-3fc2-437e-abbf-d3c83519fbdb", methods=('GET', 'POST'))
@bp.route("/c92d179f-d69c-4fb7-a069-51a7d50d76e5", methods=('GET', 'POST'))
@bp.route("/45507691-6d8b-4fc4-8d0b-367fce52868e", methods=('GET', 'POST'))
@bp.route("/81dda5d5-bd5e-4fd5-890b-0b589718e389", methods=('GET', 'POST'))
@login_required
def flower_power():
    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/35a34cbe-7d24-4e9a-adae-fcdcd5e0c083", methods=('GET', 'POST'))
@login_required
def boss_key():

    endpoint_used = request.path.replace("/", "")
    return utils.dynamic_item_handler(endpoint_used)


@bp.route("/74f9f95d-ced7-4ac2-82ce-b0079e54b938", methods=("GET", "POST"))
def boss_chest():

    item_id = "74f9f95d-ced7-4ac2-82ce-b0079e54b938"
    db = get_db()
    item_details = db.execute(f"SELECT * FROM item WHERE id='{item_id}';").fetchone()

    if request.method == "POST":

        boss_key_id = [item["id"] for item in ITEM_INFO if item["name"] == "Boss Key"][0]

        # Check if the user even has the boss key to open the chest
        has_boss_key = db.execute(f"SELECT * FROM item WHERE id='{boss_key_id}' and owner={g.user['id']};").fetchone()
        if not has_boss_key:
            flash("You don't have the boss key! You cannot open the chest.")
            return render_template("item/boss_chest.html", item_details=item_details)

        # If they already own the item, then they can't open it again
        owner_items = db.execute(
            f"SELECT * FROM item WHERE owner={g.user['id']};"
        ).fetchall()
        for item in owner_items:
            if item["id"] == item_id:
                flash("You've already opened this chest!")
                return render_template("item/boss_chest.html", item_details=item_details)

        # If someone else has opened it, they cannot
        ineligible_items = db.execute(
            f"SELECT * FROM item WHERE id='{item_id}';"
        ).fetchone()
        if ineligible_items["owner"] and ineligible_items["owner"] != g.user["id"]:
            flash("This item has already been collected!")
            return render_template("item/boss_chest.html", item_details=item_details)

        # Finally, if all conditions above pass - open the chest and mark it found/used
        db.execute(
            f"UPDATE item"
           f" SET owner={g.user['id']}, found_time='{datetime.now(UTC)}', used=1, used_time='{datetime.now(UTC)}'"
           f" WHERE id='{item_id}';"
        )
        db.commit()

        # re-run item details to reflect ownership and use changes
        item_details = db.execute(f"SELECT * FROM item WHERE id='{item_id}';").fetchone()

    return render_template("item/boss_chest.html", item_details=item_details)


@bp.route("/use", methods=('POST',))
@login_required
def use():
    item_id = request.form.get("button_id")
    db = get_db()

    items = db.execute(
        f"SELECT * FROM item WHERE id='{item_id}' and owner={g.user['id']};"
    ).fetchall()
    for item in items:
        if item["used"] == 1:
            flash("This item has already been used.")
        else:
            db.execute(f"UPDATE item SET used=1, used_time='{datetime.now(UTC)}' WHERE id='{item_id}';")
            db.commit()
    display_items = db.execute(
        f"SELECT * FROM item WHERE owner={g.user['id']};"
    ).fetchall()
    return render_template("item/index.html", items=display_items)


@bp.route("/reset_use", methods=("POST",))
@login_required
def reset_use():
    if not g.user["admin"]:
        abort(404)
    item_id = request.form.get("button_id")
    db = get_db()

    db.execute(f"UPDATE item SET used=0, used_time=null WHERE id='{item_id}';")
    db.commit()

    items = db.execute(
        "SELECT i.id, i.name, i.description, i.image_path, i.found_time, i.used, i.used_time, u.username as owner_name"
        " FROM item i LEFT JOIN user u on owner = u.id;"
    ).fetchall()

    return render_template("item/admin.html", items=items)

# def collect_item(item_id: str):
#     """Collect an item if the user hasn't already."""
#
#     print(item_id)
#     db = get_db()
#     owner_items = db.execute(
#         f"SELECT * FROM item WHERE owner={g.user['id']};"
#     ).fetchall()
#     for item in owner_items:
#         if item["id"] == item_id:
#             flash("You already have this item!")
#             return
#     db.execute(f"UPDATE item SET owner={g.user['id']}, found_time='{datetime.now(UTC)}' WHERE id='{item_id}';")
#     db.commit()
