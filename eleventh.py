#conuter
j=0
#sum
k=0
Largest=None
Smallest=None
for i in [2,5,454,6,898,4,55,1300]:
    j=j+1
    k=k+i
    if Largest is None:
        Largest=i
    elif i>=Largest:
        Largest=i
    if Smallest is None:
        Smallest=i
    elif i<=Smallest:
        Smallest=i
    print(j,'-','number is',i,'smallest is',Smallest,'largest is',Largest
    ,'total is',k,'average is',k/j)