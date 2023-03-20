#6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
#the purpose of this activity was to practice problem solving using lists and tuples.


#my attempt:
# userNumbers = input("Enter four numbers seperated by a comma.")

# print(list(userNumbers))
# print(tuple(userNumbers))

#Solution:
userNumbers = input("Enter four numbers seperated by a comma.")
#this makes list and tuple
myList = userNumbers.split(",")
myTuple = tuple(myList)
print('This is your list of values you entered: ',myList)
print('This is your tuple of values you entered: ',myTuple)