#2.	Write a Python program to check if a number is positive, negative or zero.
num = float(input('Enter number: '))
if num == 0:
    print('The number is zero')
elif num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')