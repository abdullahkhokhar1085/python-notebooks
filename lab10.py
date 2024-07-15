salary=int(input('enter employees salary: '))
employeesyearofservice = 6
bonus=salary*(5/100)
amount=bonus+salary
if employeesyearofservice>5:
   print('net bonus amount=',amount)
else:
   print('no bonus')