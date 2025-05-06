class BMW():
    def fuel_type(self):
        print("Premium Gasoline is the fuel type for BMW")
    def max_speed(self):
        print("250km/h is the max speed for BMW")
class ferrari():
    def fuel_type(self):
        print("Petrol(Gasoline) is the fuel type forferrari")
    def max_speed(self):
        print("340km/h is the max speed for ferrari")
obj1=BMW()
obj2=ferrari()
for i in(obj1,obj2):
    i.fuel_type()
    i.max_speed()