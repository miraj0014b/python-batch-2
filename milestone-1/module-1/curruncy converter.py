usd = input('enter usd amount: ')
usd_number= float(usd)
exchange_rate = 102
bdt = usd_number * exchange_rate
#print(usd_number, 'is equal to', bdt, 'bdt')

paragraph = str(usd_number) + ' is equal to ' + str(bdt) + ' BDT'
print(paragraph)

