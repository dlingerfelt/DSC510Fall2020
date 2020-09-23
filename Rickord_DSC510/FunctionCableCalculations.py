#DSC 510
#Week 4
#Programming Assignment Week 4
#Author Jake Rickord
#09/23/2020

#function definition to perform the cost calculation based on variables of num feet and price based on if statement
def cost_calc (a, b):
    return a*b

print ("Welcome to the Optic Cable Calculation Program!")
print() #spacing

#pre-set boolean for user error
error_created = False

#inputs
company_name = input("Please enter the name of your company: ")
num_feet_cable = input("Thanks! Now please enter the amount of optic cable to be installed, measured in feet:")

#attempt to cast String to float for calculations, iterative upon repeated invalid entries
while error_created != True:
    try:
        num_feet_cable = float(num_feet_cable)
        error_created = True
    except:
        print ("The value entered was non-numerical")
        num_feet_cable = input("Please enter a valid amount of optic cable to be installed, measured in feet: ")

#reset variable in case of later use
error_created = False

print() #spacing

#breakpoints to determine price per foot
if(num_feet_cable > 100 and num_feet_cable <= 250):
    calculated_cost_cable = 0.80
elif (num_feet_cable > 250 and num_feet_cable <= 500):
    calculated_cost_cable = 0.70
elif (num_feet_cable > 500):
    calculated_cost_cable = 0.50
else:
    calculated_cost_cable = 0.87

#calc for total cost
total_cost=cost_calc(calculated_cost_cable, num_feet_cable)

#output
print("Thank you for your purchase today, here is your receipt:")
print()
print("Company Name: ", company_name)
print('Amount of optic cable to be installed: %.2f' % num_feet_cable, "ft.")
print('Calculated cost of optic cable: $%.2f' % calculated_cost_cable, "/ft")
print('Total Cost of Project: $ %.2f' % total_cost)
#%.2f to limit to two decimals
