# #https://www.geeksforgeeks.org/python-data-structures-and-algorithms/#

# ##1- indexing a list

# list = ["Sonic","Tails","Knuckles"]

# #get first thing in list
# print(list[0])

# #get last thing on list
# print(list[-1])

# ##2 - tuples - immutable lists

# Tuple = ("Chemistry", "Bad")
# print(Tuple)

# #accessing tuples 
# print(Tuple[-1])
# print(Tuple[0])

# ##3- handling lists mixed with strings and numbers

# mixedSet = set([ "sonic" , 45 , "chaos" , 7])
# print(mixedSet)

# #to access elements inside set:
# for i in mixedSet:
#     print (i, end =" ")
# print()

# ##4- frozen sets
# #normal set

# set1 = set(["apple", "banana", "cherry"])

# set1.add("duran")

# print(set1)

# #frozen set

# set2 = frozenset(["eggs","fish","grapes"])
# # set2.add("ham")
# print(set2)

##5 indexing strings

# string = "Sonic is the fastest thing alive"

#first letter
# print(string[0])

#last letter
# print(string[-1])
#also count type the actual number corresponding to it but that is too much

##6 - creating a dictionary

#1 making the dictionary

# myDict = {"Character": "Metal Sonic", 1: [2064,2065, 2210, 2211]}
# print("This is a sample dictionary:")
# print(myDict)

# #2 accessing material in dictionary
# print("This will print out the character's name:")
# print(myDict["Character"])

# #3 accessing element using "get"
# print("Example of how to use 'get':" )
# print(myDict.get(1))

#4 Dictionary comprehension
# print("this does some math operation for the numbers in a dictionary")
# sampleDict = {x: ((x**2)//2) for x in [20,40,60,80,100]}
# print(sampleDict)

##7 - Matricies
#forming matrix

import numpy as py

myArray = py.array([[2,4,6,8],[1,3,5,7],
                   [20,40,60,80],[30,50,70,90]])

matrixSize = py.reshape(myArray,(4,4))

print(matrixSize)
