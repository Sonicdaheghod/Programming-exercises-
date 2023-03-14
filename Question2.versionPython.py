#Write a Python program to find out what version of Python you are using.
#Question Source: https://www.w3resource.com/python-exercises/python-basic-exercises.php#EDITOR 

#Purpose of this program was to practice how to understand outputting information about the verison of python I am using and understand the version's components

#1) we always ahve to start off by importing a module
import sys
#2) we are now going to print the version of the python used and make it readable for the user 
print("This is the version of the Python program used here-")
print(sys.version)
print("This is the version info of the Python program used here-")

print(sys.version_info)
