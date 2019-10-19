# functions.py

from typing import Dict, Tuple, List

# CHANGE ALL item VARIABLES INTO TUPLES FROM LISTS
# tuples are hashable while lists are not, that's why

class In:
    
    def __init__(self):
        pass

    
    def scan_to_truck(self, barcode: int, name: str, size: int) -> Tuple:
        """Creates a tuple in the order: barcode, name, size
        
        Args:
            barcode: an integer of the barcode of the item
            name: a string of the name of the item
            size: an integer of the size of the item

        Returns:
            A tuple of the barcode, name and size
        """

        pass


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






         


