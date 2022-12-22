user_one = ['mofiz', 26, True, 'kamruk kamakkha']
# mofiz is a man of 26 years old. he lives in kamruk kamakkha

name= user_one[0]
age = user_one[1]
living_place = user_one[3]
is_male = user_one[2]
if is_male:
    pronoun = 'he'
    gender = 'man'
else:
    pronoun = 'she'
    gender = 'female'

sentenct =f'{name} is a {gender} of {age} years old. {pronoun} lives in {living_place}'

print(sentenct)
