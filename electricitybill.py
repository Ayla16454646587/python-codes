units=int(input("please enter a number of units:"))

if (units<50):
    amount=units* 2.60
    surcharge=25

elif(units <= 100):
    amount=130+((units - 50)* 3.25)
    surcharge=35

elif(units<200):
    amount=130+162.50+((units-200)*8445)
    surcharge=75

total=amount+surcharge
print("/nElectricity bill=%.2f"%total)
