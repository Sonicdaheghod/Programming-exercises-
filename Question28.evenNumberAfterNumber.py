# 28. Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence. Go to the editor
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

#my attempt
list = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

#step 1- get all even numbers

for i in list:
    if i == 237:
        print (i)
        break; 
    
#correct answer - I did not know how to stop at a certain point in list
    elif i % 2 ==0:
        print(i)
#somehow this only prints out two even numbers 
# this is because it stops once it reaches the earliers odd number in the list
    # else:
    #     break

    
