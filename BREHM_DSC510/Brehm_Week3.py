# DSC 510
# Week 2
# Programming Assignment Week 3
# Author: David Brehm
# 09/14/2020

print('Welcome Customer!')
name = input('Please enter your name: ')  # User input name
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
    rate = 0.5
elif optic > 250:
    rate = 0.7
elif optic > 100:
    rate = 0.8
else:
    rate = 0.87

cost = round(optic*rate, 2)  # Total cost of feet * rate, rounded to two decimals.

print('{} from {}, you have requested {} ft of fiber optic cable to be installed.'.format(name, company, optic))  # Receipt.
print('At a rate of ${}/ft, your total cost is ${}.'.format(rate, cost))  # Receipt.
