largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        a=float(num)
    except:
        print('Invalid input')
    if largest is None:
        largest=a
    elif largest<=a:
        largest=a
    if smallest is None:
        smallest=a
    elif smallest>=a:
        smallest=a
   

print("Maximum is", int(largest))

print("Minimum is", int(smallest))