# File: rattanavilay_assignment_3.1.py
# Assignment: 3.1
# Course: DSC 510
# Week 3
# Programming Assignment Week 3
# Author: Thip Rattanavilay
# DATE: 09/20/2020

"""
This week we will implement “if statements” in a program. Your program will calculate the cost of fiber optic cable installation by multiplying the number of 
feet needed by $0.87. We will also evaluate a bulk discount. You will prompt the user for the number of fiber optic cable they need installed. Using the default 
value of $0.87 calculate the total expense. If the user purchases more than 100 feet they are charged $0.80 per foot. If the user purchases more than 250 feet 
they will be charged $0.70 per foot. If they purchase more than 500 feet, they will be charged $0.50 per foot.

-Your program must have a header. Use the SUI--Edwardsville Programming Style Guide for guidance.
-Display a welcome message for your program.
-Get the company name from the user.
-Get the number of feet of fiber optic cable to be installed from the user.
-Evaluate the total cost based upon the number of feet requested.
-Display the calculated information including the number of feet requested and company name.
"""

print("Welcome to Fiber Optical World!")  # Welcoming statement
Name = input("What is your name?")  # Input your customer name
# Display Welcome Message to customer
print("Welcome to the Store,", Name, "!")
user_company = input('What company are you working for?')
print("You work for " + user_company)  # Ask user to input company name

fiber_needed = input(  # Ask user to input number of feet needed
    'How many feet of fiber optical cable you are looking to install?')
# This next step convert str to int for conditional statement
try:
    # Checking error if user input non-numeric value
    fiber_needed = int(fiber_needed)
except:
    print("The number you entered was not an integer. Please re-enter")
    fiber_needed = input(
        'How many feet of fiber optical cable you are looking to install?')
print("Your looking to buy", fiber_needed, "ft of fiber.")
a = 500
b = 250
c = 100
if fiber_needed >= 500:
    print(f'Thank for purchasing more than 500ft of fiber.\n'
          f'Due to your high purchase volume, your cost per foot is .50c \n'
          f'cost = number of feet needed * .50c')
    Cost = fiber_needed * .50
    # Round number to 2 decimal for dollar value
    final_cost = round(Cost, 2)
elif 250 <= fiber_needed <= 500:
    print(f'Thank for purchasing more than 250ft of fiber.\n'
          f'Due to your high purchase volume, your cost per foot is .70c \n'
          f'cost = number of feet needed * .70c')
    Cost = fiber_needed * .70
    # Round number to 2 decimal for dollar value
    final_cost = round(Cost, 2)
elif 100 <= fiber_needed <= 250:
    print(f'Thank for purchasing more than 100 ft of fiber.\n'
          f'Due to your high purchase volume, your cost per foot is .80c \n'
          f'cost = number of feet needed * .80c')
    Cost = fiber_needed * .80
    # Round number to 2 decimal for dollar value
    final_cost = round(Cost, 2)
else:
    print(f'Thank for purchasing', fiber_needed, 'feet of fiber\n'
          f'Your cost per foot is .87c \n'
          f'cost = number of feet needed * .87c')
    Cost = fiber_needed * .87
    # Round number to 2 decimal for dollar value
    final_cost = round(Cost, 2)
# Display the correctly dolloar amount
print(f'Your purchase final cost is ${final_cost:.2f}')
receipt = "optic2020920"
print(f'Receipt\n'
      # \n is for line break
      f'Thank you {user_company} for your inquiry of {fiber_needed} feet of fiber optical cable.\n'
      # f' is formatted string literals; skip string identification
      # Display the correctly dolloar amount
      f'Your total cost is ${final_cost:.2f}\n'
      f'Your receipt number is {receipt}')
