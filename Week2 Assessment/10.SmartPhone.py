class Electronics:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f'{self.brand} {self.model} costs {self.price}')
class MobileDevice(Electronics):
    def __init__(self, brand, model, price, os):
        super().__init__(brand, model, price)
        self.os = os

    def display(self):
        super().display()
        print(f'OS: {self.os}')
class SmartPhone(MobileDevice):
    def __init__(self, brand, model, price, os, camera):
        super().__init__(brand, model, price, os)
        self.camera = camera

    def display(self):
        super().display()
        print(f'Camera: {self.camera}')
def main():
    s = SmartPhone('Apple', 'iPhone 12', 799, 'iOS', '12 MP')
    s.display()
main()
    