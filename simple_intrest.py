p=float(input("enter principal amount:))
t=float(input("enter the time period :))
r=float(input("enter rate of intrest:))
si=(p*t*r)/100
ci=p*((1+r/100)**t)-p
print(f"compound intrest:{ci}")
print(f"simple intrest: {si})
