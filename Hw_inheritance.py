class vehical:
    def __init__(self , seating_capacity):
        self.seating_capacity=seating_capacity
    def fare(self):
        return self.seating_capacity*100
class Bus:
    def __init__(self , seating_capacity):
        self.seating_capacity=seating_capacity
    def fare(self , seating_capacity):
        base= base=seating_capacity*100 
        extra=base*0.1 #10% extra charge
        total=base+extra
        return total
bus=Bus(50)
print("Total fare is =" , bus.fare(50))