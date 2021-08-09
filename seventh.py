#function practice
def square (x):
    print(x*x)
square(2)
square(4)
square(16)

def square (x):
    return x*x
a=square(2)
b=square(4)
c=square(16)
print(a,b,c)

def square(x,y,z):
    a=x*x
    b=y*y
    c=z*z
    return a ,b ,c
e=square(2,4,16)
print(e)
print( type(e) )