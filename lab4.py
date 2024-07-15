nsec = int(input('enter seconds'))
nhours = nsec // 3600 
rsec = nsec % 3600
nmin = rsec // 60 
rsec = rsec % 60
print('number of hours are:',nhours)
print('number of minutes are:',nmin)
print('numbers of seconds are:',rsec)