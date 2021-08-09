def computepay(h, r):
    if h<=40:
        ans=h*r
    else:
        ans=h*r+(h-40)*0.5*r
    return ans

hrs = input("Enter Hours:")
h=float(hrs)
rate = input("Enter Rate:")
r=float(rate)
p = computepay(h, r)
print("Pay", p)