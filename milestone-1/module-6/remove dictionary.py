car = {
    'brand': 'ford',
    'model': 'mustang',
    'year': 2020,
    'color': 'black'
}
car.update({'color': 'blue'})
car.pop('color')
print(car)