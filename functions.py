from typing import List, Dict
import pickle

data = {"all_trollies": [], "incoming_products": []}

def load():
    global data
    with open("data.p", "rb") as f:
        data = pickle.load(f)

def reset():
    global data
    data = {'all_trollies': [], 'incoming_products': []}
    with open("data.p", 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

# maybe incvlude product tracking - im lazy :?
class Trolly:
    all_trollies = data["all_trollies"]
    num_trolly = 0

    def __init__(self):
        self.storage = []
        self.weight_capacity = 100
        self.id = Trolly.num_trolly
        Trolly.num_trolly += 1
        Trolly.all_trollies.append(self)
    
    def calculate_weight(self):
        total_weight = 0
        for product in self.storage:
            total += product.weight
        return total_weight

    def __str__(self):
        return f"{self.id} = {self.storage}"


class Product:
    incoming_products = data["incoming_products"]
    
    def __init__(self, name: str, weight: int, barcode: int):
        self.name = name
        self.weight = weight
        self.barcode = barcode
        self.trolley_id = 'None'
        Product.incoming_products.append(self)
    
    def __str__(self):
        return f"{self.name}, {self.barcode}"

    def package(self, address: str, warning: str=None):
        self.address = address
        self.weight = weight
        self.warning = warning
    
    def empty_incoming(self):
        Product.incoming_products = []


class Shipment:
    def __init__(self, name: int, products: List[Product]):
        self.products = products
    
    def load_to_trolly(self):
        original_size = len(self.products)
        for product in self.products:
            print(product)
            for trolly in Trolly.all_trollies:
                if (trolly.calculate_weight() + product.weight) > 100:
                    continue
                else:
                    trolly.storage.append(product)
                    product.trolly_id = trolly.id
                    Product.incoming_products.remove(product)
        if len(Product.incoming_products) != original_size:
            return "There are " + str(len(Product.incoming_products)) + " remaining. Make more trollies to finish loading the products."
        else:
            return "Products have been successfully unloaded."
    
    def check_remaining_products(self):
        for product in Product.incoming_products:
            print(product)
    
    def __str__(self):
        for product in self.products:
            return str(product)

def save():
    data["all_trollies"] = Trolly.all_trollies
    data["incoming_products"] = Product.incoming_products
    with open("data.p", "wb") as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def main():
    pass
    
if __name__ == '__main__':
    load()
    main()