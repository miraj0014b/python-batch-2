number = int(input('enter number: '))
if number >= 80 and number <= 100:
    print('A+')
elif number >= 70 and number <= 79 :
    print('A')
elif number < 69 and number >= 0:
    print('you have failed')
else:
    print('invalid number')