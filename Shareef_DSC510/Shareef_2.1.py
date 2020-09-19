#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Adonis Shareef
#09/13/2020

#welcome the user
print("Welcome!")

#ask the user for thier company name
companyName = input("Enter the name of your servicing company.")

#ask the user for the amount of cable needed in feet
fiberOpticCable = input("Enter the number of feet of fiber optic cable needed.")

#calculate the total cost
initialCost = round((int(fiberOpticCable)*0.87),2);

#calculate tax
tax = round((0.095*initialCost),2);
totalCost = initialCost + tax;

#receipt format
print("\tRecipt")
print("\t"+companyName)
print("\t"+"Calbe: "+fiberOpticCable+"ft")
print("\tCost: $",initialCost)
print("\tTax: $",tax)
print("\tTotal: $",totalCost)
