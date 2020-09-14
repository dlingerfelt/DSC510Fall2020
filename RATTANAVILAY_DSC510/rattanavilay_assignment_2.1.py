#File: rattanavilay_assignment_2.1.py
#Assignment: 2.1
#Course: DSC 510
#Week 2
#Programming Assignment Week 2
#Author: Thip Rattanavilay
#DATE: 09/10/2020

"""
Description: 
- Display a welcome message for your user.
- Retrieve the company name from the user.
- Retrieve the number of feet of fiber optic cable to be installed from the user.
- Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
- Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
- Include appropriate comments throughout the program.
"""
from datetime import datetime # Import datatime

print("Hello and Welcome to Fiber World!") # Display Welcome to Fiber World
Name = input("What is your name?") # Input your customer name
print("Welcome to the Store,", Name, "!") # Display Welcome Message to customer


Company_Name = input("What is your company name?") # Input company name from customer
Fiber = float(input("How many feet of fiber optic cable do you need to install?")) # Input number of feet of fiber optic cable to be installed from customer


Cost_per_feet = 0.87  # Cost of installation of Fiber optic cable in feet * Cost per feet ($0.87)
Subtotal = Fiber * Cost_per_feet # Calculate Fiber number with Cost per feet
Tax = Subtotal * 0.0925 # Calculate Subtotal with Tax (CA sales tax of 9.25%) customer is in CA
Total_cost = Subtotal + Tax # Calculate Total cost with Tax 


print("Receipt") # Print a receipt for user including company name, number of feet to be installed, calculated cost, total cost

today = datetime.today() #Today's date and time 
print(today.strftime("%m/%d/%y %I:%M")) #Display today's date and time

print("Company:", Company_Name) #Display customer company
print("Number of feet of fiber to be installed=", Fiber) #Display Number of feet of fiber to be installed
print("Subtotal =", Subtotal) #Display Subtotal (Tender)
print("Sales Tax 9.25% =", Tax) #Display Sales Tax from CA
print("Total Cost =", Total_cost) #Display Total cost (Final cost)
