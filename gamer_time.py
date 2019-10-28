from typing import List, Dict
import json

class Trolly:
    all_trollies = []
    def __init__(self):
        self.storage = []
        self.status = False
        self.weight_capacity = 100
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
        self.status = 'Incoming'
        Product.incoming_products.append(self)
    
    def __str__(self):
        return f"{self.name}, {self.barcode}, {self.image}"

    def package(self, address: str, warning=None):
        self.address = address
        self.weight = weight
        self.warning = warning
        self.status = 'Packaged'

class Shipment:
    def __init__(self, products: List[Product]):
        self.products = products
    
    def load_to_trolly(self):
        available_trolly = True
        for product in Product.incoming_products:
            for trolly in Trolly.all_trollies:
                if (trolly.calculate_weight() + product.weight) > 100:
                    continue
                else:
                    pass

