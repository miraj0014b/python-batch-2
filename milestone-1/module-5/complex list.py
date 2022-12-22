# person_one = ['moris', 'male', 'australia', '1988', 'mirsa@jab.com', '01-0716-1221']
# person_two = ['lalo', 'male', 'ukrain', '29 octob 1995', 'vasko@lal.com', '11-0325-1995']

person = [
    ['moris', 'male', 'australia', '1988', 'mirsa@jab.com', '01-0716-1221'],
    ['lalo', 'male', 'ukrain', '29 octob 1995', 'vasko@lal.com', '11-0325-1995'],
    ['ruma', 'female', 'ukrain', '29 octob 1995', 'vasko@lal.com', '11-0325-1995'],
    ['kiran', 'female', 'india', '29 octob 1995', 'vasko@lal.com', '11-0325-1995'],
    ['nila', 'female', 'pakistan', '29 octob 1995', 'vasko@lal.com', '11-0325-1995'],
    ['saleha', 'female', 'bangladesh', '29 octob 1995', 'vasko@lal.com', '11-0325-1995'],
          ]
# print(person[2][2])

i = 0

while i < len(person):
    single_person = person[i]
    name = single_person[0]
    gender = single_person[1]
    country = single_person[2]
    birth_year = single_person[3]
    email = single_person[4]
    if gender == 'male':
        pronoun = 'he'
        relative = 'his'
    else:
        pronoun = 'she'
        relative = 'her'
    sentence = f'{name.title()} was born in {country}. {pronoun.title()} was born in {birth_year}. {relative} email {email}'
    print(sentence)
    i = i+1
    # print(name, gender, country, birth_year, email, sep="---")