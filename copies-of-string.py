#9.	Write a Python program to get a string which is n (non-negative integer) copies of a given string.
string = input('Enter your word or sentence: ')
c = int(input('Avoid floating numbers.\nEnter no. of copies: '))
if c < 0:
    print('You have entered an invalid no.of copies ')
if c == 0:
    print('Ok, Thankyou!\nSee you later')
else:
    for i in range(c):
        print(string)