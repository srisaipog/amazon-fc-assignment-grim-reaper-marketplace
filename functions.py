from typing import List, Dict
import json

# maybe incvlude product tracking - im lazy :?
class Trolly:

    def __init__(self, num: int):
        self.storage = []
        self.weight_capacity = 100
        self.num = number
        all_trollies.append(self)
    
    def calculate_weight(self):
        total_weight = 0
        for product in self.storage:
            total += product.weight
        return total_weight

    def __str__(self):
        return f"{trolly.num} = {trolly.storage}"


class Product:
    incoming_products = []

    def __init__(self, name: str, weight: int, barcode: int, image: str):
        self.name = name
        self.barcode = barcode
        self.image = image
        self.trolley_num = 'None'
        Product.incoming_products.append(self)
    
    def __str__(self):
        return f"{self.name}, {self.barcode}, {self.image}"

    def package(self, address: str, warning: str=None):
        self.address = address
        self.weight = weight
        self.warning = warning


class Shipment:
    def __init__(self, name: int, products: List[Product]):
        self.products = products
    
    def load_to_trolly(self):
        original_size = len(Product.incoming_products)
        for product in Product.incoming_products:
            for trolly in Trolly.all_trollies:
                if (trolly.calculate_weight() + product.weight) > 100:
                    continue
                else:
                    trolly.storage.append(product)
                    product.trolly.num = trolly.num
                    Product.incoming_products.remove(product)
                    #end the function (indicates that a trolly was found)
        if len(Product.incoming_products) != original_size:
            return "There are " + str(len(Product.incoming_products)) + "remaining. Make more and try again."
        else:
            return "Products have been successfully unloaded."