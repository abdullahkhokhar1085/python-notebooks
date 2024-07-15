#nested- if
age1 = int(input('enter first person age:'))
age2 =int(input('enter second person age:'))
age3 = int(input('enter third person age:'))
if age1 > age2:
    if age1>age3:
        print(age1,'is oldest')
    else:
        print(age3,'is oldest')

elif age2>age3:
    print(age2,'is oldest')

else:
      print(age3,'is oldest')        