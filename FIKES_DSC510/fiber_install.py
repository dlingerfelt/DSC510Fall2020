# DSC510 Week 2 Assignment - fiber_install.py
# Program to calculate cost of fiber install based on input
# Python 3.8
# Author Matthew Fikes
# 9/8/20

import sys

# Assign calculated cost/foot to variable
footCost = 0.87

print("Fiber Installation Basic Entry Routine - F.I.B.E.R.")
print('----------------------------------------------------')

# Take input for company name
companyName = input("Enter name of company providing installation:")

# while loop to go back to input if there is an input error
while True:
    try:
        installMeasurement = input("Enter the length of cable install in feet:")

# catch bad inputs
        if float(installMeasurement) <= 0:
            raise ValueError()

# tell user what went wrong
    except ValueError:
        print("ERROR: Install length must be entered as a number greater than zero")

    else:
        installCost = round((float(installMeasurement) * footCost),2)

# format output receipt
        print('\n' + companyName + ' INVOICE' + '\n' + '-----------------' + '\n' + 'Feet installed: ' + installMeasurement)
        print('cost/ft: $' + str(footCost) + '\n' + '-----------------' + '\n' + 'Total install cost: $' + str(installCost))
        break







