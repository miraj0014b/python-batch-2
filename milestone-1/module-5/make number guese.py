# students = []
# while True:
#     name = input('enter students name ')
#     if name == 'shesh':
#
#         print(students)
#         print('total students: ', len(students))
#         break
#     else:
#         students.append(name)


import random
numbers = [1,2,3,4,5,6,7,8,9]

print('games start and guess a number 1-9')
print('*'*40)
computer_number = random.choice(numbers)
while True:
    number = int(input('what is your guess: '))
    if computer_number == number:
        print('congratulations')
        break
    else:
        print('hoy nai')