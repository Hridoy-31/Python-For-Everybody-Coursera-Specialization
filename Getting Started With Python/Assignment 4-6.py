def computepay(hrs,rph):
    if(hrs <= 40):
        pay = hrs * rph
    else:
        extra = (hrs - 40)
        pay = (40 * rph) + (extra * rph * 1.5)
        
    return pay

hrs = input("Enter Hours:")
hrs = float(hrs)

rph = input("Rates per Hour:")
rph = float(rph)

p = computepay(hrs,rph)
print("Pay",p)
