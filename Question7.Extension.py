#7 - Write a Python program that accepts a filename from the user and prints the extension of the file. Go to the editor
#Sample filename : abc.java
#Output : java
 
#my attempt:
# userFile = input("Enter the whole name of your file including its extension:")

# print(userFile)

#solution
userFile = input("Enter the whole name of your file including its extension:")
fileExtension = userFile.split(".")
print("The extension of your file is "+ repr(fileExtension[-1]))
