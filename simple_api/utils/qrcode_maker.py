import qrcode

from item_info import ITEM_INFO

base_url = "https://qrapi.patrick-cooper.com"

for item in ITEM_INFO:
    img = qrcode.make("/".join([base_url, item["id"]]))
    img.save(f"codes/{item['id']}.png")