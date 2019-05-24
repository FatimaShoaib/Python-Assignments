#23.	Write a Python program to convert temperatures to and from Celsius, Fahrenheit
t = float(input('Enter temperature: '))
print("Select conversion:\n1: Celsius to Fahrenheit\n2: Fahrenheit to Celsius")
c  =int(input())
if c == 1:
    ans = (t*9/5)+32
    print('Temperature  = ', ans,' °F')
elif c ==2:
    ans = (t-32)*5/9
    print('Temperature = ', ans,' °C')
else:
    print('Invalid option')