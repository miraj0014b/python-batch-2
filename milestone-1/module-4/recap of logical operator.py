salary = int(input('enter your salary: '))
years_of_services = float(input('enter your service year: '))

if years_of_services > 5 and salary >=20000 :
    bonus = 0.05
    net_salary = salary + salary * bonus
    print(net_salary)
else:
    print('You get only your salary', salary, 'BDT')