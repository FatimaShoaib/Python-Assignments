#8.	Write a Python program to get a new string from a given string where "Is" has been added to the front. 
#    If the given string already begins with "Is" then return the string unchanged.
a = input('Please avoid spacing at the beginning. \nEnter your sentence: ')
check = (a[0:2])
if check == 'Is' or check == 'is':
    print('Your sentence is correct')
else:
    print('Your sentence is modified to : "Is '+ a + '"' )

