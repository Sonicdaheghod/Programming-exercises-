#Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014


#my attempt
examDate = (11,12,2014)
print("The exam starts on:",examDate[0],"/",examDate[1],"/",examDate[2])

#answer
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

#%i = integer
#we extract the integers and put them in form "x/x/x" from our exam date variable
