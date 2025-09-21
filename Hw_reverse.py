class Reverse:
    def __init__(self , s):
        self.s=s
    def reverse(self):
        return self.s[::-1]
user=input("Enter string")
obj=Reverse(user)
print("Reversed" , obj.reverse())