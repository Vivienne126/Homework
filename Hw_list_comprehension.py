value=int(input("Enter a number"))
odd=[x for x in range(value) if x%2 != 0]
print(odd)

l1=["apple" , "Banana" , "Blueberry"]
capital=[items[0].upper()+items[1:].lower() for items in l1]
print(capital)