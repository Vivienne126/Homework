class roman_converter:
    def __init__(self , roman_values):
        self.roman_values=roman_values
        roman_values={1000:"M" , 900:"CM" , 500:"D" , 400:"CD" , 100:"C" , 90:"XC" , 50:"L" , 40:"XL" , 10:"x" , 9:"IX" , 5:"V" , 4:"IV" , 1:"I" }
    def convert(self , number , roman_values):
        self.number=number
        self.roman_values=roman_values
        roman=""
        for values in self.roman_values:
            while number>=values:
                roman=roman+self.roman_values[values]
                number=number-values
        return roman
result=roman_converter()
number=int(input("Enter number"))
print("The converted result is" , result.roman)
