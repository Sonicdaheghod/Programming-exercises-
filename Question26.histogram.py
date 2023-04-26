# 26. Write a Python program to create a histogram from a given list of integers.

from matplotlib import pyplot as plt

#figure size

plt.rcParams["figure.figsize"] = [7,3.5]
plt.rcParams["figure.autolayout"] = True

#list of numbers
listNumbers = [1,2,4,6,8,45,2,2]

#Plot histogram from data set
plt.hist(listNumbers)

#show the chart
plt.show()