# Creating a Directory If It Doesn’t Exist
import glob
import os
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
receipts = glob.iglob('./new/receipt-[0-9]*.json')
receipts = [r.replace('\\', '/') for r in receipts]
subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")


print(f"Receipt subtotal: ${round(subtotal, 2)}")
