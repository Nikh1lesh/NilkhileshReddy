from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass
    @abstractmethod
    def subtract(self, a, b):
        pass
    @abstractmethod
    def multiply(self, a, b):
        pass
    @abstractmethod
    def divide(self, a, b):
        pass
class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
def main():
    b = BasicCalculator()
    print(b.add(5, 3))
    print(b.subtract(5, 3))
    print(b.multiply(5, 3))
    print(b.divide(5, 3))
main()