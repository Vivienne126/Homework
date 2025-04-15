class dog:
    animal="Dog"
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color
ob=dog("German Stepherd" , "Brown")
ob_1=dog("Bulldog" , "White")
print("{} is {} in colour".format(ob.animal))
print("{} is {} in color".format(ob_1.animal))