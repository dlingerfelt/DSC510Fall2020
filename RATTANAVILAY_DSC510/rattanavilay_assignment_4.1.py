# File: rattanavilay_assignment_4.1.py
# Assignment: 4.1
# Course: DSC 510
# Week 4
# Programming Assignment Week 4
# Author: Thip Rattanavilay
# DATE: 09/27/2020

"""

This week we will modify our IF Statement program to add a function to do the heavy lifting.
Modify your IF Statement program to add a function. This function will perform the cost calculation. 
The function will have two parameters (feet and price). When you call the function, you will 
pass two arguments to the function; feet of fiber to be installed and the cost (remember that price 
is dependent on the number of feet being installed). You should have the following:
Your program must have a header. Use the SIU Edwardsville Programming Guide for guidance.

-A welcome message.
-A function with two parameters.
-A call to the function.
-The application should calculate the cost based upon the number of feet being ordered.
-A printed message displaying the company name and the total calculated cost.
-All costs should display in USD Currency Format Ex: $123.45.

"""

from datetime import datetime


def get_costPerFoot(lengthInFeet):

    # This function will calculate the cost per foot based on the length of optic fiber in feet.

    if lengthInFeet >= 500:  # greater or equal to 500 feet = $0.50/foot
        costPerFoot = 0.50
    elif lengthInFeet >= 250:  # greater or equal to 250 feet = $0.70/foot
        costPerFoot = 0.70
    elif lengthInFeet >= 100:  # greater or equal to 100 feet = $0.80/foot
        costPerFoot = 0.80
    else:
        costPerFoot = 0.87  # less than 100 feet = $0.87/foot
    return costPerFoot

# This function will calculate total cost by multiplying the length in feet and cost per foot


def calculateTotalCost(lengthInFeet, costPerFoot):
    return lengthInFeet*costPerFoot


print("Welcome to Fiber Optical World!")  # Welcoming statement

Name = input("What is your name?")  # Display Welcome Message to customer

# Display Welcome Message to customer
print("Welcome to the Store,", Name, "!")

# Retrieve company name from customer
Company_Name = input("What is your company name?")

# Retrieve number of feet of fiber optic cable to be installed from customer
length_in_Feet = float(
    input("How many feet of fiber optic cable do you need to install?"))

# Calculate cost per foot, round to 2 decimal places
cost_per_foot = round(get_costPerFoot(length_in_Feet), 2)

# calculate the total cost
totalCost = round(calculateTotalCost(length_in_Feet, cost_per_foot), 2)

# Print a receipt for customer including company name, number of feet to be installed, cost per foot, total cost
print("Receipt")
# Display the date of purchase
today = datetime.today()
print(today.strftime("%m/%d/%y %I:%M"))
# Display the customer company name
print("Company:", Company_Name)

# f' is formatted string literals; skip string identification
# Display the correctly length
print(f"Number of feet of fiber to be installed: {length_in_Feet:.0f}")
# Display the correctly cost per foot amount
print(f"Cost per foot: ${cost_per_foot:.2f}")
# Display the correctly dolloar amount
print(f"Total Cost: ${totalCost:.2f}")
