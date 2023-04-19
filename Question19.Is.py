# 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is". 

#my attempt
# userString = input("Type a sentence: ")

# newUserString = ("Is " + userString)

# if newUserString == "is" or "Is" in [0]:
#     print(userString)
# else:
#     print(newUserString)

#correct answer
def new_string(text):
  if len(text) >= 2 and text [:2] == "Is" or "is":
    return text
  return "Is " + text
print(new_string(input("Type a sentence: ")))


#I did not include that if the first two characters are "IS", we don't have to add the "is" abd if the length of string is at least 2