# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Daniel Angel
# 09/10/2020
# This block defines variables with user inputted strings or floats.
print('Hello. Welcome to this fiber optic installation estimator.')
cust_name = input('What is your name?')    # Ask user's info and prompt input.
proj_name = input('Does your project have a name? If not, leave blank')
comp_name = input('Please write your company name')
print('We have discounts. The more you buy the more you save.')
footage = input('How many feet of cable do you need?')
footage = int(footage)
if footage <= 100:              # Else-If conditional ladder.
    price_per_foot = .87
elif footage <= 250:
    price_per_foot = .8
elif footage <= 500:
    price_per_foot = .7
else:
    price_per_foot = .5
subtotal = round((int(footage)*price_per_foot), 2)  # Calculate subtotal.
tax_rate = .095
tax = round((subtotal*tax_rate), 2)                # Calculate tax.
total = round((subtotal + tax), 2)                 # Sum tax and subtotal.
# This is the end of the user input and the start of the receipt printing.
print()
print()
print('RECEIPT OF PURCHASE')
print()
print('Customer Name:', cust_name)  # I used commas instead of + to save space.
print('Project Name :', proj_name)
print('Company Name :', comp_name)
print()
print('Footage       :  ', footage, 'feet')
print('Price per foot: ', format(price_per_foot, '.2f'), '$/foot')
print('Subtotal      : $' + format(subtotal, '.2f'))  # Floats into strings.
print('Tax @ 9.5%    : $' + format(tax, '.2f'))
print('Total         : $' + format(total, '.2f'))
