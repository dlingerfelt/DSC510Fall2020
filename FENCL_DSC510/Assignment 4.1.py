# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Riley Fencl
# 09/13/2020

print("Welcome User! Please, input the requested information and your receipt will be generated! Thank you!")

# User Input
cname = input("What is the name of your company?\n")

cable = int(input("How many feet of fiber optic cable is to be installed?\n"))


# Defining the calculation function
def pricing(arg1, arg2):
    return arg1 * arg2


# Setting Up Conditional Pricing
if cable <= 100:
    cost = .87
    cablecost = pricing(cable, cost)
elif 100 <= cable <= 250:
    cost = .8
    cablecost = pricing(cable, cost)
elif 250 <= cable <= 500:
    cost = .7
    cablecost = pricing(cable, cost)
elif cable >= 500:
    cost = .5
    cablecost = pricing(cable, cost)

# Formatting Cost Per Foot
a = "Cost Per Foot: "
b = "${:,.2f}".format(cost)

# Formatting Grand Total
x = "Grand Total: "
z = "${:,.2f}".format(cablecost)

# Receipt Printout
print("Installation Receipt")
print(cname)
print("Total Cable to be Installed:", cable, "feet")
print(a + b)
print(x + z)
print("Thank you!")
