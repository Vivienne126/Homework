Dict_1={"Hello" : 2 , "Hello" : 2 ,  "How": 2 , "Are":3 , "You":1} 
count=1
n=int(input("Enter the value you want to check the frequency"))
for n in Dict_1.values():
    if n==count:
        count+=1
print(count)

