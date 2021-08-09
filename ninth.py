#Loop Practice
n=20
while n>=0:
    print(n)
    n=n-1
print('Game Over')
print(n)


while True:
    Say=input('Type something I will repeat it. Type # as first charecter to say don not print. Type Done to finsh >  ')
    if Say[0]=='#':
        continue
    if Say=='Done':
        break
    print(Say)
print('Done!!!!')