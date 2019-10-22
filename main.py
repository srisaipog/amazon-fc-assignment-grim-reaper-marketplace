# main.py

from functions import *
import json

DATA_FILE = "data.json"

incoming_items = {} # incoming_items = {item: quantity, ...}
trolly_items = {} # trolly_items = {item: quantity, ...}
to_package_items = {} # to_package_items = {item: quantity, ...}
packaged_items = {} # packaged_items = {item: quantity, ...}
to_ship_items = {} # to_ship_items = {item: quantity, ...}
# item = (barcode: int, name: str, size: int, img_file: str)

truck = [] # truck = [order, order, order, ...]
orders = [] # orders = [order, order, order, ...]
# order = {address, barcode, items}
# items = {item: quantity, ...}

shelves = [] # shelves = [shelf, shelf, shelf]
# shelf = [max_capacity, cur_capacity, {item: quantity, item: quantitiy, ...}]
