class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side **2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
def main():
    s = Square(5)
    print(s.area())
    t = Triangle(4, 3)
    print(t.area())
main()