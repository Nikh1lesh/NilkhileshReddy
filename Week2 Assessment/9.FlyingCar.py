class Car:
    def __init__(self, name, max_speed,color):
        self.name = name
        self.max_speed = max_speed
        self.color = color
    def display_car_details(self):
        return f"Name: {self.name}\nMax Speed: {self.max_speed}\nColor: {self.color}"
    def move(self):
        return "Car is moving"
class Airplane:
    def __init__(self, name, max_speed,color):
        self.name = name
        self.max_speed = max_speed
        self.color = color
    def display_airplane_details(self):
        return f"Name: {self.name}\nMax Speed: {self.max_speed}\nColor: {self.color}"
    def fly(self):
        return "Airplane is flying"
class FlyingCar(Car,Airplane):
    def __init__(self, name, max_speed,color):
        Car.__init__(self, name, max_speed, color)
        Airplane.__init__(self, name, max_speed,color)
def main():
    f=FlyingCar("Flying Car",200,"White")
    print(f.display_car_details())
    print(f.display_airplane_details())
    print(f.move())
    print(f.fly())
main()