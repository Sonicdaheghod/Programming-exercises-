#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
#Sample value of n is 5
#Expected Result : 615

#my attempt
# userNumber = input("Type in a number:")
# answerInput = (int(userNumber) + int(userNumber**2) + int(userNumber**3))
# print(answerInput)

#correct answer
userNumber = int(input("Type in a number:"))

#%s places the variable userNumber into the math equation where we multiply the number a certain number of times (ex. 5 is th enumber, so 5 x 5 for secondNumber)
firstNumber = int("%s" % userNumber)
secondNumber = int("%s%s" % (userNumber,userNumber))
thirdNumber = int("%s%s%s" % (userNumber,userNumber,userNumber))

print(firstNumber+secondNumber+thirdNumber)
