#1.	Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
r = float(input('Enter radius of the circle: '))
Area = math.pi*r*r
print('Area of circle = ' , Area)