class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def display_vehicle_details(self):
        return f"Name: {self.name}\nMax Speed: {self.max_speed}\nMileage: {self.mileage}"
class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, color):
        super().__init__(name, max_speed, mileage)
        self.color = color
    def display_car_details(self):
        return f"Name: {self.name}\nMax Speed: {self.max_speed}\nMileage: {self.mileage}\nColor: {self.color}"
class Bike(Vehicle):
    def __init__(self, name, max_speed, mileage, color):
        super().__init__(name, max_speed, mileage)
        self.color = color
    def display_bike_details(self):
        return f"Name: {self.name}\nMax Speed: {self.max_speed}\nMileage: {self.mileage}\nColor: {self.color}"
class ElectricCar(Car):
    def __init__(self, name, max_speed, mileage, color, battery_capacity):
        super().__init__(name, max_speed, mileage, color)
        self.battery_capacity = battery_capacity
    def display_electric_car_details(self):
        return f"Name: {self.name}\nMax Speed: {self.max_speed}\nMileage: {self.mileage}\nColor: {self.color}\nBattery Capacity: {self.battery_capacity}"

def main():
    c=Car("Car",100,20,"Red")
    print(c.display_car_details())
    b=Bike("Bike",60,40,"Black")
    print(b.display_bike_details())
    e=ElectricCar("Electric Car",120,30,"Blue",100)
    print(e.display_electric_car_details())
main()