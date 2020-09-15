# DSC510

# Week 2 Assignment - fiber_optic_installation.py

# Program to calculate the cost of fiber installation based on the user input

# Author Sowmya Chavali

# 09/09/20


import getpass

# gets the username to display it in the welcome message
UserName = getpass. getuser()

print("------ Welcome to FIBER OPTICS "+UserName+" ------")

# Retrieving the company's name from the user

CompanyName = input("Enter the company's name :")

CostPerFoot = 0.87

# Looping through until we get valid input from the user
while True:
    try:
        # Retrieving the number of feet of fiber optic cable to be installed from the user.
        installMeasurementInFeet = float(input("Enter the length of optical cable to install in feet:"))
        if installMeasurementInFeet <= 0:
          raise ValueError     # Raising value exception for negative and zero value inputs

    except ValueError:
        print("oops! Length provided must be greater than zero")
    else:
        # Total installation cost
        InstallationCost = installMeasurementInFeet * CostPerFoot
        break


#Printing the Itinerary

print("--------------Invoice--------------")
print("Company: "+CompanyName)
print("-----------------------------------")
print("Fiber to be installed in feet: "+str(installMeasurementInFeet))
print("cost per foot: $"+str(CostPerFoot))
print("-----------------------------------")
print("Total installation cost: $"+str(InstallationCost))









