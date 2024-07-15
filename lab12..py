import math
a = float(input('enter coefficient of x^2:'))
b = float(input('enter coefficient of x:'))
c = float(input('enter coefficient of c:'))
delta = b**2-4*a*c

if delta>0:
    print('the roots are real & different!')
    x1=(-b+math.sqrt(delta)) / (2*a)
    x2=(-b-math.sqrt(delta)) / (2*a)
    print('roots are',x1,'and',x2)

elif delta == 0:
    print('the roots are real & equal!')
    x = -b (2*a)
    print('roots are',x,'and',x)

else:
    print('the roots are complet!\n')
    realpart = -b/(2*a)
    imgpart = math.sqrt (-delta)/2*a
    print('roots one is','real part','+i',imgpart)
    print('second root is','realpart','-i',imgpart)