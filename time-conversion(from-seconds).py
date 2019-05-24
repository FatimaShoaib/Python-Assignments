#21.	Write a Python program to convert seconds to day, hour and minutes.
t = float(input('Enter time: '))
print("Select conversion:\n1: day\n2: hour\n3: minute")
c  =int(input())
if c == 1:
    ans = t/86400
    print('Time  = ', ans,' day(s)')
elif c ==2:
    ans = t/3600
    print('Time in seconds = ', ans,' hr(s)')
elif c ==3:
    ans = t/60
    print('Time in seconds = ', ans,' min(S)')
else:
    print('Invalid option')