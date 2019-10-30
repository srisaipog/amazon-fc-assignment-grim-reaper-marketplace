from functions import *

def main():
    pizza = Product('pepperoni', 50, 1)
    for product in Product.incoming_products:
        print(product)
    
    reset()
    print(Product.incoming_products)

    
if __name__ == '__main__':
    main()