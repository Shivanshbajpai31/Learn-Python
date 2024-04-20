#Negative indexing
tup=(1,2,76,342,34)
print(tup[-1])

#check for an item
if 342 in tup:
    print("Yes 342 in the tuple")
else:
    print("It is not there")

#RANGE OF THE INDEX
tup=tup[1:2]
print(tup)