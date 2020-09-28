# DSC 510
# Week 4
# Programming Assignment Week4
# Author: David Brehm
# 09/21/2020

# Function to calculate the total cost.
def rateCalc(inFeet, inRate):
    total = inFeet * inRate
    return total


print('Welcome Customer!')  # Welcome message.
name = input('Please enter your name: ')  # User input name.
company = input('Please enter your company name: ')  # User input company name.
optic = 0

while True:
    try:
        optic = float(input("How many feet of fiber optic cable would you like installed? "))  # User input cable amount.
        if optic < 0:  # Check if input is negative.
            print('Please enter a non-negative number.')
            continue
        break
    except ValueError:  # Error if input is not a float.
        print('Please enter a numerical value.')
        continue

# Determine rate by amount of fiber optic cable ordered. Larger purchases have a decreased rate.
if optic > 500:
    rate = 0.50
elif optic > 250:
    rate = 0.70
elif optic > 100:
    rate = 0.80
else:
    rate = 0.87

outTotal = rateCalc(optic,rate)  # Calculate the total cost.

print('{} from {}, you have requested {} ft of fiber optic cable to be installed.'.format(name, company, optic))  # Receipt.
print('Your rate is: ${0:.2f}/ft.'.format(rate))  # Receipt.
print('Your total cost is: ${0:,.2f}'.format(outTotal))  # Receipt.
