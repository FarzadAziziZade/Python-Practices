# difference between division and floor division
print(11//5)
print(11/5)

#some logical operators
x=6
a= x>5 and x<10
b= not(x>5 and x<10)
c= x>10 or x==6
print('a is',a,'b is',b,'c is',c)

# difference betwee 'is' and '=='
d=1
e=1.0
f= d==e
g= d is e
print('f is',f,'g is',g)
print('d is',type(d),'e is',type(e))