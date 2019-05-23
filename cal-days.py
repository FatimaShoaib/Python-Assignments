#5.	Write a Python program to calculate number of days between two dates.
#from datetime import date
#import datetime
#print("Enter first date (date/month/year): ")
#date1 = input(datetime.date)
#print("Enter second date (date/month/year): ")
#date2 = input(datetime.date)
#print(date1)
#print(date2)
#diff = date2 - date1
#print('The difference of days = ', (diff.days))
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)