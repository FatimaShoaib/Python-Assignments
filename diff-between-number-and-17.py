#7.	Write a Python program to get the difference between a given number and 17, 
#   difference cannot be negative
num = float(input('Enter number: '))
diff = num - 17
if diff < 0:
    print('Your answer is in negative. Please enter number greater than 17')
else:
    print('difference between ', num , 'and 17 = ', diff)