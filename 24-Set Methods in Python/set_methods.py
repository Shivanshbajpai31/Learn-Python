#Union and update()
s1={1,2,3,6}
s2={3,6,7}
print (s1.union(s2))
s1.update(s2)
print(s1,s2)

#Intersection and intersection_update()
cities={"Lucknow","Delhi", "Mumbai" ,"Pune"}
cities2={"Lucknow","Pune","Howrah"}
cities3=cities.intersection(cities2)
print(cities3)

cities={"Lucknow","Delhi", "Mumbai" ,"Pune"}
cities2={"Lucknow","Pune","Howrah"}
cities3=cities.intersection_update(cities2)
print(cities3)

#Symmetric_difference and symmetric_update()
cities={"Lucknow","Delhi", "Mumbai" ,"Pune"}
cities2={"Lucknow","Pune","Howrah"}
cities3=cities.symmetric_difference(cities2)
print(cities3)

#Difference() and difference_update()
cities={"Lucknow","Delhi", "Mumbai" ,"Pune"}
cities2={"Lucknow","Pune","Howrah"}
cities3=cities.difference(cities2)
print(cities3)

#isdisjoint()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

#issuperset()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

#isSubset()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

#add()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

#update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

#remove
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

#pop
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#Check if this is exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")