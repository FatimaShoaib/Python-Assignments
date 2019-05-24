#19.	Write a Python program to convert the distance (in feet) to inches, yards, and miles.
# 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile
d = float(input('Enter distance (in ft): '))
print("Select conversion\n1: inches\n2: yards\n3: miles")
c  =int(input())
if c == 1:
    ans = d*12
    print('Distance = ', ans,' inch(es)')
elif c ==2:
    ans = d/3
    print('Distance = ', ans, 'yard(s)')
elif c ==3:
    ans = d/5280
    print('Distance = ', ans, 'mile(s)')
else:
    print('Invalid option')