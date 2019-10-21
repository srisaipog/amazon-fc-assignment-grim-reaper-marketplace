# functions.py

from typing import Dict, Tuple, List
import json

# CHANGE ALL item VARIABLES INTO TUPLES FROM LISTS
# tuples are hashable while lists are not, that's why

# Item Flow: In
class In:
    
    def __init__(self):
        pass

    
    def scan_to_truck(barcode: int, name: str, size: int, img_file: str) -> Tuple:
        """Creates a tuple in the order: barcode, name, size
        
        Args:
            barcode: an integer of the barcode of the item
            name: a string of the name of the item
            size: an integer of the size of the item

        Returns:
            A tuple of the barcode, name and size
        """

        return (barcode, name, size, img_file)


    def truck_to_trolly(incoming_items: Dict, trolly_items: Dict) -> Tuple:
        """Takes items from the incoming shipment and
        transfers them to the trolly

        Args:
            incoming_items: all of the incoming items with 
                            the key as the item and the value as the quantity of the item
            trolly_items: all of the items in the trolly with
                          the key as the item and the value as the quantity of the item

        Returns:
            A tuple of the variables incoming_items and trolly_items (after having the
            items transferred from incoming_items to trolly_items)

        """

        for item in incoming_items.keys():
            try:
                trolly_items[item] += incoming_items[item]
            except:
                trolly_items[item] = incoming_items[item]
            
            incoming_items[item] -= incoming_items[item]
        
        incoming_items_duplicate = incoming_items.copy()

        for item in incoming_items.keys():
            if incoming_items_duplicate[item] <= 0:
                incoming_items_duplicate.pop(item)

        return incoming_items_duplicate, trolly_items
    

    def trolly_to_shelves(trolly_items: Dict, shelves: List) -> Tuple:
        """Transfers all of the items on the trolly to empty shelves
        by checking each shelve and seeing which one has enough space to fit the items
        
        Args:
            trolly_items: all of the items in the trolly with
                          the key as the item and the value as the quantity of the item
            shelves: a list of singular shelves whose
                     first index contains the shelf capacity,
                     second index contains the current occupied space,
                     and the rest contain dicts of items and their quantities

        Returns:
            A tuple of the variables trolly_items (should be empty if 
            everything fit in the shelves) as well as the shelves variable
        """

        for item in trolly_items.keys():
            quantity = trolly_items[item]
            size = item[2]
            size_all = quantity * size

            if quantity <= 0:
                continue


            # Finds out if all of the same item can be added into same shelf
            for i, shelf in enumerate(shelves):
                if shelf[0] >= shelf[1] + size_all: # If max_capacity >= than cur_capacity + size_all
                    shelves[i][1] += size_all # Updates cur_capacity
                    
                    try:
                        shelves[i][2][item] += quantity # adds items to shelf
                    except:
                        shelves[i][2][item] = quantity # adds items to shelf
                    
                    trolly_items[item] = 0 # removes items from trolly_items

                    break
            # Puts each item as soon as possible
            else:
                j = 0
                while True:

                    if trolly_items[item] == 0:
                        break

                    if shelves[j][0] >= shelves[j][1] + size:
                        shelves[j][1] += size
                    
                        try:
                            shelves[j][2][item] += 1
                        except:
                            shelves[j][2][item] = 1
                        
                        trolly_items[item] -= 1
                        
                        continue

                    j += 1
                    if j == len(shelves):
                        break

        trolly_items_duplicate = trolly_items.copy()

        for item in trolly_items.keys():
            if trolly_items_duplicate[item] <= 0:
                trolly_items_duplicate.pop(item)
    
        return trolly_items_duplicate, shelves



# Item Flow: Order-fulfilment station
class Process:
    
    def __init__(self):
        pass


    def get_item_location(item: Tuple, quantity: int = 0) -> Dict:
        """Finds the location of the given item based on the quantity
        If the quantity is <= 0 or not given, find all instances of the
        item. If a quantity > 0 is given, that many instances of the item

        Args:
            item: A tuple of the item (with it's barcode, name, size and img_file)
            quantity: the number of the specified item you want to find
        
        Returns:
            A dict of the shelf numbers and how many
            of each item there in each shelf

            Ex: {1: 6, 9: 1, 10: 13}
            There are 6 of the item in shelf 1
            1 of the item in shelf 9
            13 of the item in shelf 10
        """
        
        pass


    def shelf_to_package(item: Tuple, quantity: int, shelves: List, to_package_items: Dict) -> Tuple:
        """Recieves the item and the quantity of the number
        wanted to move to the packagers. Will call get_item_location
        to find out where each item is, remove it from that shelf
        and place it in to_package_items along with their quantity.

        Args:
            item: A tuple of the item (with it's barcode, name, size and img_file)
            quantity: the number of the specified item you want to find
            shelves: A list of the shelves
            to_package_items: a dict of items to be packaged with their respective quantities
        
        Returns:
            A tuple: (shelves, to_package_items)
        """

        pass


    def package(to_package_items: Dict, packaged_items: Dict) -> Tuple:
        """Packages items. Moves them from to_package_items
        to packaged_items onces packaged. Do this one at
        a time for each item. If an item has a quantity of 6,
        make sure to move it 1 at a time. Finds the total size of
        the items in the order (to_package_item) and finds a box size.

        Args:
            to_package_items: a dict of items to be packaged with their respective quantities
            packaged_items: a dict of packaged items with their respective quantities
        
        Returns:
            a tuple: (to_package_items, packaged_items, box_size)
        """

        pass


    def packaged_to_to_ship(packaged_items: Dict, to_ship_items: Dict) -> Tuple:
        """Moves packaged items to to_ship_items one at a time

        Args:
            packaged_items: a dict of packaged items with their respective quantities
            to_ship_items: a dict of items to be stamped with their respective quantities
        
        Returns:
            a tuple: (packaged_items, to_ship_items)
        """

        pass



# Item Flow: Ship-out station
class Out:
    def __init__(self):
        pass


    def stamp(to_ship_items: Dict, address: str, barcode: int) -> Dict:
        """Takes the items to be shipped, address and barcode
        and puts them into an order
        
        Args:
            to_ship_items: to_ship_items: a dict of items to be stamped with their respective quantities
            address: the address of which the package should be sent to
            barcode: the barcode of the order
        Returns:
            A tuple of A dictionary of the order and to_ship_items
            Ex: 
            order = {address, bsarcode, items}
                                       items = {item: quantity, ...}
        
        """

        order = {}
        order["address"] = address
        order["barcode"] = barcode
        order["items"] = {}

        for item in to_ship_items:
            for num in range(to_ship_items[item]):
                try:
                    order["items"][item] += 1
                except:
                    order["items"][item] = 1
                
                to_ship_items[item] -= 1
        
        to_ship_items_duplicate = to_ship_items.copy()

        for item in to_ship_items_duplicate:
            if to_ship_items_duplicate[item] <= 0:
                to_ship_items.pop(item)
        
        return order, to_ship_items


    def to_truck(order, truck):
        """Adds the order to the list of orders (truck)

        Args:
            order: A dict with the address, barcode and items
            truck: A list of orders that need to be delivered
        
        Returns:
            The list truck with the order added to it
        """
        
        pass



def save(file, to_store):
    """Replaces the set in data.json with
    the newer variables

    Args:
        file: the name of the file to save to
        to_store: A set of:

        incoming_items: a dict with items
        trolly_items: a dict with items
        to_package_items: a dicts with items
        packaged_items: a dict with items
        to_ship_items: a dict with items
        truck: a list of orders
        orders: a list of orders
        shelves: a list of shelves
    Returns:
        None
    """

    all = {
        0: incoming_items,
        1: trolly_items,
        2: to_package_items,
        3: packaged_items,
        4: to_ship_items,

        5: truck,
        6: orders,

        7: shelves
    }

    with open(file, "w") as f:
        json.dump(all, f)


def load(file):
    """Loads variables from data.json
    into memory

    Args:
        file: the name of the file to load from
    
    Returns:
        A set of:

        incoming_items: a dict with items
        trolly_items: a dict with items
        to_package_items: a dicts with items
        packaged_items: a dict with items
        to_ship_items: a dict with items
        truck: a list of orders
        orders: a list of orders
        shelves: a list of shelves
    """

    with open(file, "r") as f:
        to_load = json.load(f)

    return to_load