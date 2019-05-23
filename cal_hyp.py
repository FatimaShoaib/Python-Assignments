#18.	Write a Python program to calculate the hypotenuse of a right angled triangle
import math
base = float(input('Enter base : '))
perp = float(input('Enter perpendicular : '))
hyp = math.sqrt((base**2) + (perp**2))
print('Hypotenuse = ', hyp)