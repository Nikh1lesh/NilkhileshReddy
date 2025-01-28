def addItems(cart, name, price):
    cart.append([name, price])
def displayItems(cart):
    for i in cart:
        print(i)
def calculateTotal(cart):
    total = 0
    for i in cart:
        total+=i[1]
    return total
def main():
    cart = []
    while True:
        print("1. Add item")
        print("2. Display cart")
        print("3. Calculate total")
        print("4. Exit")
        choice = int(input())
        if choice == 1:
            name = input("Enter name of item")
            price = int(input("Enter price of item"))
            addItems(cart, name, price)
        elif choice == 2:
            displayItems(cart)
        elif choice == 3:
            print("Total price is", calculateTotal(cart))
        elif choice == 4:
            break
        else:
            print("Enter valid choice")