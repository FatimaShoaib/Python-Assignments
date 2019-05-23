#17.	Write a Python program to convert height (in feet and inches) to centimetres.
h = float(input('Enter height to be converted in cm: '))
print("Height is in:\nSelect '1' or '2'\n1: Feet\n2: inches")
c  =int(input())
if c == 1:
    ans = h*30.48
    print('Height in cm = ', ans)
elif c ==2:
    ans = h*2.54
    print('Height in cm = ', ans)
else:
    print('Invalid option')