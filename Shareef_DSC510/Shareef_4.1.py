# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Adonis Shareef
# 09/27/2020


# welcome the user
print("Welcome!")

# ask the user for thier company name
companyName = input("Enter the name of your servicing company.")

fiberOpticCable = 0
# validate user input with try except
valid_input = False
while not valid_input:
    try:
        fiberOpticCable = float(input(
            "Enter the number of feet of fiber optic cable needed."))  # ask the user for the amount of cable needed in feet
        if fiberOpticCable < 0:
            print("Enter a positive numerical value such as 1,2,3...")
            continue
        break
    except ValueError:
        print("Enter a positive numerical value such as 1,2,3...")
        continue

# conditional statements for cost per feet
if 100 < fiberOpticCable <= 250:
    charge_per_foot = 0.8
elif 250 < fiberOpticCable <= 500:
    charge_per_foot = 0.7
elif fiberOpticCable > 500:
    charge_per_foot = 0.5
else:
    charge_per_foot = 0.87


# calculating cost function
def calcCost(a, b):
    return a * b


# calculate the total cost
initialCost = round(calcCost(int(fiberOpticCable), charge_per_foot), 2)
# calculate tax
tax = round(calcCost(0.095, initialCost), 2);
totalCost = initialCost + tax;

# receipt format
print("\tRecipt")
print("\tCompany: ", companyName)
print("\t" + "Calbe: ", fiberOpticCable, "ft")
print("\tRate per foot: $", charge_per_foot)
print("\tCost: $", initialCost)
print("\tTax: $", tax)
print("\tTotal: $", totalCost)
