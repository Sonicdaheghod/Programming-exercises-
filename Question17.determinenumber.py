# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

#my attempt
while True:
    number = float(input("Type a number:"))

    if 900 <= number <= 1000:
        print(number,"is within 100 of 1000")
    elif 1900 <= number <= 2000:
        print(number,"is within 100 of 2000")
    else:
        print(number, "is not a number is within 100 of 1000 or 2000.")

#need to loop program
    askInput = input("""Type 'continue' to use this tool again """)
    if askInput == "continue" or "Continue":
        continue
    else:
        break