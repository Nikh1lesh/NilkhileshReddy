class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    def check_availability(self,quantity):
        if quantity <= self.stock:
            return True
        else:
            return False
    def display_product_details(self):
        print(f"Name: {self.name}\nPrice: {self.price}\n")
        
def create_product_details():
    name = input("Enter the name of the product: ")
    price = float(input("Enter the price of the product: "))
    stock = int(input("Enter the stock of the product: "))
    product = Product(name,price,stock)
    return product

def main():
    Products=[]
    while True:
        Products.append(create_product_details())
        choice = input("Do you want to add more products? (y/n): ")
        if choice == 'n' or choice == 'N':
            break
    while True:
        for i in Products:
            i.display_product_details()
        product_name = input("Enter the name of the product you want to buy: ")
        for i in Products:
            if i.name == product_name:
                quantity = int(input("Enter the quantity of the product you want to buy: "))
                if i.check_availability(quantity):
                    print(f"Total cost: {i.price*quantity}")
                    i.stock -= quantity
                else:
                    print("Insufficient stock")
        choice = input("Do you want to buy more products? (y/n): ")
        if choice == 'n' or choice == 'N':
            break
main()