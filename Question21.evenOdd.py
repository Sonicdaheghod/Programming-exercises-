# 21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user. 

number = int(input("Type in a number: "))

if (number % 2)==0:
    print("The number you typed is even.")
else:
    print("The number you typed is odd.")


#the ==0 means that if a number divided by (%) 2 has a remainder of zero, then that number is even