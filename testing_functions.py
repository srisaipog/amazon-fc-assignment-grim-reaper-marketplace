# testing_functions.py

from functions import *
# from typing import Dict, List, Tuple

# item = (barcode: int, name: str, size: int)

def test_scan_to_truck():
    pass


def test_truck_to_trolly():

    items = (
    (1235, "test 1", 1),
    (145, "test 2", 67),
    (1459, "test 3", 13),
    (1461, "test 4", 5),
    (9876, "test 5", 3)
    )

    assert In.truck_to_trolly({items[0]: 5, items[1]: 57, items[3]: 15}, {}) == ({}, {items[0]: 5, items[1]: 57, items[3]: 15})
    assert In.truck_to_trolly({}, {}) == ({}, {})
    assert In.truck_to_trolly({items[2]: 5, items[3]: 4, items[0]: 6}, {items[2]: 10}) == ({}, {items[2]: 15, items[3]: 4, items[0]: 6})
    assert In.truck_to_trolly({items[0]: 1}, {}) == ({}, {items[0]: 1})

def test_trolly_to_shelves():
    
    shelves = []
    for i in range(15):
        shelves.append([16, 0])
    for j in range(25):
        shelves.append([25, 0])
    
    

