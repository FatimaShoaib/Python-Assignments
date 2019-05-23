#6.	Write a Python program to get the volume of a sphere, 
#   take the radius as input from user. V=4 / 3 πr3
import math
r = float(input('Enter radius of the sphere: '))
v = (4/3)*(math.pi*r**3)
print('Volume of a sphere of radius ', r , 'is ', v)