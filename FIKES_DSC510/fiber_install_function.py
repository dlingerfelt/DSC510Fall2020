# DSC510 Week 4 Assignment - fiber_install_function.py
# Program to calculate cost of fiber install based on input
# Python 3.8
# Author Matthew Fikes
# 9/23/20


print("Fiber Installation Basic Entry Routine - F.I.B.E.R.")
print('----------------------------------------------------')

# Take input for company name
companyName = input("Enter name of company providing installation:")

baseFootCost = 0.87

# Assign calculated cost/foot based on length
def footageCost(measure):
    if float(measure) > 100 and float(measure) <= 250:
        footCost = 0.80
    elif float(measure) > 250 and float(measure) <= 500:
        footCost = 0.70
    elif float(measure) > 500:
        footCost = 0.50
    else:
        footCost = baseFootCost

    installCost = (float(measure) * footCost)
    return installCost, footCost

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
# run function and unpack returned tuple into variables
        totalCost, costPerFoot = footageCost(installMeasurement)



# format output receipt
        print('\n' + companyName + ' INVOICE' + '\n' + '-----------------' + '\n' + 'Feet installed: ' + str(installMeasurement))
        print('cost/ft: $' + '{:.2f}'.format(costPerFoot) + '\n' + 'Bulk install discount: $' + '{:.2f}'.format(baseFootCost - costPerFoot) + '/ft')
        print('-----------------' + '\n' + 'Total install cost: $' + '{:.2f}'.format(round(totalCost, 2)))
        print('Total savings: $' + '{:.2f}'.format((baseFootCost - costPerFoot)*float(installMeasurement)))
        break


