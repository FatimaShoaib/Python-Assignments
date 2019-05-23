#10.	Write a Python program to find whether a given number (accept from the user) is even or odd, 
#       print out an appropriate message to the user.
num = int(input('Enter a Number: '))
if  num % 2 == 0:
   print('The number ' + str(num) + ' is even')
else:
    print('The number ' +str(num) +' is odd')