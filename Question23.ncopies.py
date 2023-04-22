# 23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

#my attempt

#use if len(x) and text [:2]
#for n in x
# stringUser = input("Type something: ")
# ntimes = input("How many times do you want your string to be written? ")
# text = range(int(ntimes))
# #1- defining a string
# def string(text):
#     if len(text) >= 2 or len(text) <= 2:
#         for n in text:
#             print(stringUser)
#2- looping number time print


#correct answer:

def nString(text, n):
    flen = 2

    #this gets the first 2 characters of a string
    if flen > len(text):
        flen = len(text)
    otherString = text[:flen]
    #if the length of the text is less than 2, that string will use that to repeat n times
    #otherwise, it will ge the first 2 characters of a string and use that

    outcome = ""

    #the looping
    for i in range(n):
        
        outcome = outcome + otherString
    return outcome
print(nString("Sonic",2))
