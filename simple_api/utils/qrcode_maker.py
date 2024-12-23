import qrcode

from item_info import ITEM_INFO

# Set your host URL here
base_url = "https://example-site.com"

qrcode.make(base_url).save(f"codes/root.png")

for item in ITEM_INFO:
    img = qrcode.make("/".join([base_url, item["id"]]))
    img.save(f"codes/{item['id']}.png")