# testing_functions.py

from functions import *
# from typing import Dict, List, Tuple

# item = (barcode: int, name: str, size: int)

items = (
    (1235, "test 1", 1),
    (1458, "test 2", 2),
    (1459, "test 3", 13),
    (1461, "test 4", 5),
    (9876, "test 5", 3)
    )


def test_scan_to_truck():
    pass


def test_truck_to_trolly():

    assert In.truck_to_trolly({items[0]: 5, items[1]: 57, items[3]: 15}, {}) == ({}, {items[0]: 5, items[1]: 57, items[3]: 15})
    assert In.truck_to_trolly({}, {}) == ({}, {})
    assert In.truck_to_trolly({items[2]: 5, items[3]: 4, items[0]: 6}, {items[2]: 10}) == ({}, {items[2]: 15, items[3]: 4, items[0]: 6})
    assert In.truck_to_trolly({items[0]: 1}, {}) == ({}, {items[0]: 1})

def test_trolly_to_shelves():
    
    """
    test_shelves = []
    for i in range(2):
        test_shelves.append([16, 0, {}])
    for j in range(3):
        test_shelves.append([25, 0, {}])
    """
    
    # FIND OUT WHY I NEED TO RE-DECLARE test_shelves EVERY TIME!!!! ?!!??!?!?

    test_shelves = [[16, 0, {}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]]
    assert In.trolly_to_shelves({}, test_shelves) == ({}, test_shelves)
    
    test_shelves = [[16, 0, {}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]]
    assert In.trolly_to_shelves({items[0]: 6}, test_shelves) == ({}, [[16, 6, {items[0]: 6}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]])

    test_shelves = [[16, 0, {}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]]
    assert In.trolly_to_shelves({items[1]: 11}, test_shelves) == ({}, [[16, 0, {}], [16, 0, {}], [25, 22, {(1458, 'test 2', 2): 11}], [25, 0, {}], [25, 0, {}]])
    
    test_shelves = [[16, 0, {}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]]
    assert In.trolly_to_shelves({items[1]: 12}, test_shelves) == ({}, [[16, 0, {}], [16, 0, {}], [25, 24, {(1458, 'test 2', 2): 12}], [25, 0, {}], [25, 0, {}]])
    
    test_shelves = [[16, 0, {}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]]
    assert In.trolly_to_shelves({items[1]: 18}, test_shelves) == ({}, [[16, 16, {(1458, 'test 2', 2): 8}], [16, 16, {(1458, 'test 2', 2): 8}], [25, 4, {(1458, 'test 2', 2): 2}], [25, 0, {}], [25, 0, {}]])

    test_shelves = [[16, 0, {}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]]
    assert In.trolly_to_shelves({items[1]: 13}, test_shelves) == ({}, [[16, 16, {(1458, 'test 2', 2): 8}], [16, 10, {(1458, 'test 2', 2): 5}], [25, 0, {}], [25, 0, {}], [25, 0, {}]])
    
    test_shelves = [[16, 0, {}], [16, 0, {}], [25, 0, {}], [25, 0, {}], [25, 0, {}]]
    assert In.trolly_to_shelves({items[0]: 16, items[1]: 12}, test_shelves) == ({}, [[16, 16, {(1235, 'test 1', 1): 16}], [16, 0, {}], [25, 24, {(1458, 'test 2', 2): 12}], [25, 0, {}], [25, 0, {}]])