# DSC510

# Week 4 Assignment - Assignment_4.1.py

# Program to calculate the cost of fiber installation based on the user input

# Author Sowmya Chavali

# 09/25/20

import getpass

# gets the username to display it in the welcome message
UserName = getpass. getuser()

print("------ Welcome to FIBER OPTICS "+UserName+" ------")

# Retrieving the company's name from the user

CompanyName = input("Enter the company's name :")

BaseRatePerFoot = 0.87


#This function calculates the cost/foot based on the requested fiber length
def CalcCost(length,cost):
    if (length > 0) and (length <= 100):
        CostPerFoot = cost
    elif (length > 100) and (length <= 250):
        CostPerFoot = 0.80
    elif (length > 250) and (length <= 500):
        CostPerFoot = 0.70
    else:
         CostPerFoot = 0.50

    # Total installation cost
    InstallationCost = length * CostPerFoot
    return  InstallationCost,'{:,.2f}'.format(CostPerFoot)

#function to print the invoice
def PrintInvoice():
    # Printing the Invoice
    print("\n--------------Invoice--------------")
    print("Company:  " + CompanyName)
    print("-----------------------------------")
    print("Fiber to be installed in feet: " + str(installMeasurementInFeet))
    print("cost per foot                : $" + str(CostPerFoot))
    print("-----------------------------------")
    print("Total installation cost      : $" + "%.2f" % InstallationCost)
    print("\n      Thank You Visit Again")


# Looping through until we get valid input from the user
while True:
    try:
        # Retrieving the number of feet of fiber optic cable to be installed from the user.
        installMeasurementInFeet = float(input("Enter the length of optical cable to install in feet:"))
        if installMeasurementInFeet <= 0:
          raise ValueError     # Raising value exception for negative and zero value inputs

    except ValueError:
        print("oops! Length provided must be a number greater than zero")
    else:
        # run function and unpack returned tuple into variables
        InstallationCost, CostPerFoot = CalcCost(installMeasurementInFeet, BaseRatePerFoot)
        break

#function to display the invoice
PrintInvoice()