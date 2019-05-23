#3.	Write a Python function to check whether a number is completely divisible by another number.
#   Accept two integer values form the user.
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
if num1 % num2 == 0:
    print('The given two numbers are completely divisible by each other')
else:
    print('The given two numbers are not completely divisible by each other')