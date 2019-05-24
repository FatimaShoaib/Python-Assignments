#22.	Write a Python program to calculate body mass index. 
w = float(input('Enter weight(kg): '))
h = float(input('Enter height(m): '))
bmi = w/h**2
print('BMI = ', bmi)