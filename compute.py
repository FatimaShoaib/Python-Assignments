#4.	Write a Python program that accepts an integer (n) and computes the value of (n + nn + nnn)
n = int(input('Enter number: '))
cal = (n + (n*n) + (n*n*n))
print('Result = ', cal)