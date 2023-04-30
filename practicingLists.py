#https://www.geeksforgeeks.org/python-data-structures-and-algorithms/#

##1- indexing a list

list = ["Sonic","Tails","Knuckles"]

#get first thing in list
print(list[0])

#get last thing on list
print(list[-1])

##2 - tuples - immutable lists

Tuple = ("Chemistry", "Bad")
print(Tuple)

#accessing tuples 
print(Tuple[-1])
print(Tuple[0])

##3- handling lists mixed with strings and numbers

mixedSet = set([ "sonic" , 45 , "chaos" , 7])
print(mixedSet)

#to access elements inside set:
for i in mixedSet:
    print (i, end =" ")
print()

##4- frozen sets
#normal set

set1 = set(["apple", "banana", "cherry"])

set1.add("duran")

print(set1)

#frozen set

set2 = frozenset(["eggs","fish","grapes"])
# set2.add("ham")
print(set2)