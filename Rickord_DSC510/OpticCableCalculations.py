#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Jake Rickord
#09/7/2020

print ("Welcome to the Optic Cable Calculation Program!")
print() #spacing

#inputs
company_name = input("Please enter the name of your company: ")
num_feet_cable = float(input("Thanks! Now please enter the amount of optic cable to be installed, measured in feet:")) #cast String to float for calculations
print() #spacing

#calculations
calculated_cost_cable = 0.87
total_cost=num_feet_cable*calculated_cost_cable

#output
print("Thank you for your purchase today, here is your receipt:")
print()
print("Company Name: ", company_name)
print('Amount of optic cable to be installed: %.2f' % num_feet_cable, "ft.")
print('Calculated cost of optic cable: $%.2f' % calculated_cost_cable, "/ft")
print('Total Cost of Project: $ %.2f' % total_cost)
#%.2f to limit to two decimals
