import math
class circle:
    radius=int(input("Enter the radius of the circle"))
    def __init__(self,radius):
        self.radius=radius
    def areaOfCircle(self):
        print("My area is :" , 3.14*self.radius*self.radius)
    def perimeter(self):
        return 2*math.pi*self.radius
obj=circle(radius)
circle_obj=circle()
Area=circle_obj.areaOfCircle
Perimeter=circle_obj.perimeter
print( "The perimeter of the circle is \n" , Perimeter)
print("The area of the circle is \n" , Area)

