#20.	Write a Python program to convert all units of time into seconds.
t = float(input('Enter time: '))
print("Time is in:\n1: hour\n2: minute\n3: day\n4: week\n5: month\n6: year ")
c  =int(input())
if c == 1:
    ans = t*3600
    print('Time in seconds = ', ans)
elif c ==2:
    ans = t*60
    print('Time in seconds = ', ans)
elif c ==3:
    ans = t*86400
    print('Time in seconds = ', ans)
elif c ==4:
    ans = t*604800
    print('Time in seconds = ', ans)
elif c ==5:
    ans = t*2628000
    print('Time in seconds = ', ans)
elif c ==6:
    ans = t*31540000
    print('Time in seconds = ', ans)
else:
    print('Invalid option')