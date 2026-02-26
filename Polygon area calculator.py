# Parent Class
class Polygon:
    def area(self):
        print("Area method will be defined in child class")


# Rectangle Class
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Triangle Class
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Main Program
print("1. Rectangle")
print("2. Triangle")

choice = int(input("Enter choice: "))

if choice == 1:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    obj = Rectangle(l, w)

elif choice == 2:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    obj = Triangle(b, h)

else:
    print("Wrong choice")
    exit()

print("Area is:", obj.area())