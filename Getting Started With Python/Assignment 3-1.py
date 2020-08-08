hrs = input("Enter Hours:")
hrs = float(hrs)

rph = input("Rates per hour: ")
rph = float(rph)

if (hrs <= 40):
    pay = hrs*rph
    print(pay)
else:
    extrahour = (hrs - 40)
    pay = (40 * rph) + (extrahour * 1.5 * rph)
    print(pay)
