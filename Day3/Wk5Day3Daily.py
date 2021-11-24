import math
class Circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2
    def __add__(self, other):
        return self.radius+other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def sort(self, other):
        list = []
        list.append(int(self.radius))
        list.append(int(other.radius))
        list = sorted(list)
        return list
circle1 = Circle(5)
circle2 = Circle(6)
print("The area of circle1 is: ", circle1.area())
addition = circle1 + circle2
print("The sum of the two circles is:", addition)
print(circle1>circle2)
print(circle1<circle2)
print(circle1.sort(circle2))
