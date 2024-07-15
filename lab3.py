ndays = int(input('enter number of days:'))
nyears = ndays // 365  #quotient
rdays = ndays % 365    #remainder
nweeks = rdays // 7
rdays = rdays % 7
print('numbers of years are:',nyears)
print("numbers of weeks are:",nweeks)
print("number of days are:",rdays)
