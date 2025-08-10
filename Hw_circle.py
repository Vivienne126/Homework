import math

radius=float(input("Enter radius"))


class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius

#Creating objects
c=circle(radius)
print("Area:" , c.area())
print("Perimeter:" , c.perimeter())
    



    