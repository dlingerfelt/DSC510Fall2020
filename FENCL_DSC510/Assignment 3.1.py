#DSC 510
#Week 3
#Programming Assignment Week 3
#Author Riley Fencl
#09/13/2020

print("Welcome User! Please, input the requested information and your receipt will be generated! Thank you!")

# User Input
cname = input("What is the name of your company?\n")

cable = int(input("How many feet of fiber optic cable is to be installed?\n"))

# Setting Up Conditional Pricing
if cable < 100: cost, cablecost = .87, cable * .87
elif 100 < cable < 250: cost, cablecost = .8, cable * .8
elif 250 < cable < 500: cost, cablecost = .7, cable * .7
elif cable > 500: cost, cablecost = .5, cable * .5

# Formatting Cost Per Foot
a = "Cost Per Foot: "
b = str(cost)

# Formatting Grand Total
x = "Grand Total: "
y = "$"
z = str(cablecost)

# Receipt Printout
print("Installation Receipt")
print(cname)
print("Total Cable to be Installed:", cable, "feet")
print(a+y+b)
print(x+y+z)
print("Thank you!")

