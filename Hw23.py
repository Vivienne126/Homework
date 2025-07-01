my_dictionary={ "a":2 , "b":2 , "c":2 , "d":1}
k=int(input("Enter the value you want to  check the frequency of"))
c=0
for value in my_dictionary.values():
    if value==k:
        c=c+1
print(c)
