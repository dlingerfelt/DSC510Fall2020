# DSC510

# Week 3 Assignment - Assignment_3.1.py

# Program to calculate the cost of fiber installation based on the user input

# Author Sowmya Chavali

# 09/19/20


import getpass

BaseCostPerFoot = 0.87

# gets the username to display it in the welcome message
UserName = getpass. getuser()

print("------ Welcome to FIBER OPTICS "+UserName+" ------")

# Retrieving the company's name from the user

CompanyName = input("Enter the company's name :")

# Looping through until we get valid input from the user
while True:
    try:
        # Retrieving the number of feet of fiber optic cable to be installed from the user.
        installMeasurementInFeet = float(input("Enter the length of optical cable to install in feet:"))
        if installMeasurementInFeet <= 0:
            raise ValueError     # Raising value exception for negative and zero value inputs
        else:                    # enter if the input is greater than zero
            if (installMeasurementInFeet > 0) and (installMeasurementInFeet <= 100):
                CostPerFoot = BaseCostPerFoot
            elif (installMeasurementInFeet > 100) and (installMeasurementInFeet <= 250):
                CostPerFoot = 0.80
            elif (installMeasurementInFeet > 250) and (installMeasurementInFeet <= 500):
                CostPerFoot = 0.70
            else:
                CostPerFoot = 0.50
            # Total installation cost
            InstallationCost = installMeasurementInFeet * CostPerFoot
        break
    except ValueError:
        print("oops! Invalid value, Length provided must be a greater than zero")

# Calculating the discount received
discount = installMeasurementInFeet * BaseCostPerFoot - InstallationCost

# Printing the Itinerary

print("\n--------------Invoice--------------")
print("Company:  "+CompanyName)
print("-----------------------------------")
print("Fiber to be installed in feet: "+str(installMeasurementInFeet))
print("cost per foot: $"+str(CostPerFoot))
print("-----------------------------------")
print("Total installation cost:      $" + "%.2f" % InstallationCost)
print("Total discount:               $" + "%.2f" % discount)
print("\n      Thank You Visit Again")
