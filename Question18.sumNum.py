# 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum. 

input1, input2, input3 = (input("Enter 3 numbers:")).split()

sumList = float(input1)+float(input2)+float(input3)

if input1 == input2 == input3:
    print("The sum of the three numbers is", float(sumList) * 3)

else:
    print("The sum of the three numbers is", float(sumList))
