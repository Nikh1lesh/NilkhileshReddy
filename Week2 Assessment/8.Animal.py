class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat meows")
def main():
    animal=Animal()
    dog=Dog()
    cat=Cat()
    animal.speak()
    dog.speak()
    cat.speak()