# DSC510 Week 3 Assignment - fiber_install_v2.py
# Program to calculate cost of fiber install based on input
# Python 3.8
# Author Matthew Fikes
# 9/15/20


print("Fiber Installation Basic Entry Routine - F.I.B.E.R.")
print('----------------------------------------------------')

# Take input for company name
companyName = input("Enter name of company providing installation:")

baseFootCost = 0.87

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
# Assign calculated cost/foot to variable
        if float(installMeasurement) > 100 and float(installMeasurement) <= 250:
            footCost = 0.80
        elif float(installMeasurement) > 250 and float(installMeasurement) <= 500:
            footCost = 0.70
        elif float(installMeasurement) > 500:
            footCost = 0.50
        else:
            footCost = baseFootCost

        installCost = (float(installMeasurement) * footCost)


# format output receipt
        print('\n' + companyName + ' INVOICE' + '\n' + '-----------------' + '\n' + 'Feet installed: ' + str(installMeasurement))
        print('cost/ft: $' + '{:.2f}'.format(footCost) + '\n' + 'Bulk install discount: $' + '{:.2f}'.format(baseFootCost - footCost) + '/ft')
        print('-----------------' + '\n' + 'Total install cost: $' + '{:.2f}'.format(round(installCost, 2)))
        print('Total savings: $' + '{:.2f}'.format((baseFootCost - footCost)*float(installMeasurement)))
        break


