# 25. Write a Python program that checks whether a specified value is contained within a group of values.

#my attempt
# listNumbers = [1,2,3,4]

# if listNumbers == "3":
#     print("the number 3 is included")
# else:
#     print("there is no number 3 in the list")

#correct answer

def numberIdentify(listNumber,n):
    for value in listNumber:
        if n == value:
            return True
    # do not use else
    return False

print(numberIdentify([1,2,3,4],3))
print(numberIdentify([1,2,3,4],5))