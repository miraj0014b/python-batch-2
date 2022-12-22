import random
person = ['moris', 'chitagong']
name = person[0]
location = person[1]

sentence_one_group =[
    f'this is {name}',
    f'my name is {name}',
    f'{name} is my name'
]

sentence_one =random.choice(sentence_one_group)
print(sentence_one)