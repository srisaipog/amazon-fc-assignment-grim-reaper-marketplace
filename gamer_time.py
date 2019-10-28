from typing import List, Dict
import json

# maybe incvlude product tracking - im lazy :?
class Trolly:
    all_trollies = []

    def __init__(self, number: int):
        self.storage = []
        self.weight_capacity = 100
        self.num = number
        all_trollies.append(self)
    
    def calculate_weight(self):
        total_weight = 0
        for product in self.storage:
            total += product.weight
        return total_weight


class Product:
    incoming_products = []

    def __init__(self, name: str, weight: int, barcode: int, image: str):
        self.name = name
        self.barcode = barcode
        self.image = image
        self.trolley_num = None
        Product.incoming_products.append(self)
    
    def __str__(self):
        return f"{self.name}, {self.barcode}, {self.image}"

    def package(self, address: str, warning=None):
        self.address = address
        self.weight = weight
        self.warning = warning


class Shipment:
    def __init__(self, products: List[Product]):
        self.products = products
    
    def load_to_trolly(self):
        for product in Product.incoming_products:
            for trolly in Trolly.all_trollies:
                if (trolly.calculate_weight() + product.weight) > 100:
                    continue
                else:
                    trolly.storage.append(product)
                    product.trolly.num = trolly.num
                    Product.incoming_products.remove(product)
                    #end the function (indicates that a trolly was found)
                    return False
        return "The warehouse has run out of available trollies. Feel free to create a new one."

