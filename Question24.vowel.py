# 24. Write a Python program to test whether a passed letter is a vowel or not.

#1 - have person write text
#2- write function that detects if letter is vowel or not (use if else)



# def voweldetect(text):
    
#     if text == "a" or "e" or  "i" or "o" or "u":
#         print("This is a vowel")
#     else:
#         print("This is a consonant")

# text = input("Type a letter: ")
# voweldetect(text)

#Regular 
text = input("Type a letter: ")
vowels = {"a","e","i","o","u"}
if any(char in vowels for char in text):
    print("This is a vowel")
else:
    print("This is a consonant")
        
#using def function
text = input("Type a letter: ")
vowels = {"a","e","i","o","u"}
def vowel():
    if any(char in vowels for char in text):
        print("This is a vowel")
    else:
        print("This is a consonant")
vowel()
        

