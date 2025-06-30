set_1A={"Blue" , "Green"}
set_2A={"Blue" , "Yellow"}
print("Orignal sets: \n" , set_1A , set_2A)
print("The unique componets/values in the sets are:")
print(set_1A.symmetric_difference(set_2A))
print("The same components/Values is:")
print(set_1A.intersection(set_2A))

#Integers difference in sets

set_1B={1,2,3,4,5}
set_2B={1,5,6,7,8,9}
print("\n Orignal sets:" , set_1B , set_2B)
print("The unique components are:")
print(set_1B.symmetric_difference(set_2B))

print("The same components/values are:")
print(set_1B.intersection(set_2B))
