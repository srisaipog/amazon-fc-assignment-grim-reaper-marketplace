from typing import List, Dict
import json

class Trolly:
    all_trollies = []
    def __init__(self, weight_capacity=100):
        self.weight_capacity = weight_capacity
        self.storage = []
        self.status = False
        all_trollies.append(self)


class Product:
    incoming_products = []
    def __init__(self, name: str, barcode: int, image: str):
        self.name = name
        self.barcode = barcode
        self.image = image
        self.status = 'Incoming'
        Product.incoming_products.append(self)
    
    def __str__(self):
        return f"{self.name}, {self.barcode}, {self.image}"

    def package(self, address: str, weight: int, warning=None):
        self.address = address
        self.weight = weight
        self.warning = warning
        self.status = 'Packaged'

class Shipment:
    def __init__(self, products: List[Product]):
        self.products = products
    
    def load_to_trolly(self, incoming_products):
        pass
