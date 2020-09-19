#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Riley Fencl
#09/13/2020

print("Welcome User! Please, input the requested information and your receipt will be generated! Thank you!")

# User Input
cname = input("What is the name of your company?\n")

cable = input("How many feet of fiber optic cable is to be installed?\n")

cablecost = int(cable) * .87

# Formatting Grand Total
x = "Grand Total: "
y = "$"
z = str(cablecost)

# Receipt Printout
print("Installation Receipt")
print(cname)
print("Total Cable to be Installed:", cable, "feet")
print("Cost per foot: $0.87")
print(x+y+z)
print("Thank you!")

