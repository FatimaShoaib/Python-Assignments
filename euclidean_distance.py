#16.	Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
import math
print('Enter first point (x1,y1):')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
print('Enter second point (x2,y2):')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
dis = math.sqrt((x2-x1)**2 + (y2 - y1)**2) 
print('(' , x1,',',y1, ')' '\t (' ,x2,',',y2, ')')
print('Euclidean distance of the given two points = ' , dis)