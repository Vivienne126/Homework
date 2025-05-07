import random
n=int(input("Enter how many numbers u want your password to have"))
random_numbers=random.choices(range(1,101), k=n)#i couldnt use the n variable alone it was giving error so i assigned another variable for n just to try and it is working
print(random_numbers)