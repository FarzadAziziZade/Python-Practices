a='Hi'
try:
    b=float(a)
except:
    b=float(1)
    print('you should set a= digits for example a=1')
print('result is:',b)

a='123'
try:
    b=float(a)
except:
    b=float(1)
    print('you should set a= digits for example a=1')
print('result is:',b)