# 27. Write a Python program that concatenates all elements in a list into a string and returns it.

#myattempt

# list = ["Sonic1", "Tails1", "Knuckles1"]

# printList = [i.split('1', 1)[0] for i in list]

# final  = str(printList)

#correct answer

def concatenateList(List):
    result = ""
    for i in List:
        result += str(i)
    return result

#we defined function, but we have to type in print to actually have function show in terminal

print(concatenateList(["s","o","n","i","c"]))