# functions.py

from typing import Dict, Tuple


class In:
    
    def __init__(self):
        pass

    def truck_to_trolly(self, incoming_items: Dict, trolly_items: Dict): -> Tuple
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
            
        return incoming_items, trolly_items
    

    def trolly_to_shelves(self, trolly_items: Dict, shelves: List): -> Tuple
        """Transfers all of the items on the trolly to empty shelves
           by checking each shelve and seeing which one has enough space
           to fit the items
        
        Args:
            trolly_items: all of the items in the trolly with
                          the key as the item and the value as the quantity of the item
            shelves: a list of singular shelves whose
            first index contains the shelf capacity,
            second index contains the current occupied space,
            and the rest contain dicts of items and their quantities

        Returns:
            A tuple of the variables trolly_items (should be empty if 
            everything fit in the shelves) as well as the shelves variable and
            a boolean (True if everything fit onto the shelves and false if something(s)
            are still in the trolly_items variable)
        """

        for item in trolly_items.keys():
            quantity = trolly_items[item]
            size = trolly_items[item["size"]]
            size_all = quantity * size

            # Finds out if all of the same item can be added into same shelf
            for i, shelf in enumerate(shelves):
                if shelf[0] <= shelf[1] + size_all: # If shelf_capacity <= than cur_capacity + size_all
                    shelves[i][1] += size_all # Updates cur_capacity
                    
                    try:
                        shelves[i][2][item] += quantity # adds items to shelf
                    except:
                        shelves[i][2][item] = quantity # adds items to shelf
                    
                    trolly_items[item] = 0 # removes items from trolly_items

                    break

            # Puts each item as soon as possible
            else:
                for i, shelf in enumerate(shelves):
                    while shelf[0] <= shelf[1] + size: # If shelf_capacity <= than cur_capacity + size
                        shelves[i][2][1] += size # Updates cur_capacity
                        
                        try:
                            shelves[i][2][item] += 1 # adds item to shelf
                        except:
                            shelves[i][2][item] = 1 # adds item to shelf
                        
                        trolly_items[item] -= 1 # removes item from trolly_items
            
        for item in trolly_items.keys():
            if trolly_items[item] <= 0:
                trolly_items.pop(item)
    
    return trolly_items, shelves






         


