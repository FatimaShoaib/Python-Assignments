#15.	Write a Python program to compute the future value of a specified principal amount,
#       rate of interest, and a number of years.
P = float(input('Enter Principal Amount(Rs): '))
r = float(input('Enter Rate per year: '))
t = int(input('Enter no. of years: '))
I = P*(1 + r*t)
print('Total Amount = ', I,'Rs')