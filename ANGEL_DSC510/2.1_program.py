# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Daniel Angel
# 09/10/2020
# This block defines variables with user inputted strings or floats.
cust_name = input('What is your name?')    # Ask user's info and prompt input.
proj_name = input('Does your project have a name? If not, leave blank')
comp_name = input('Please write your company name')
print('The price for installation of ' # Explain pre-tax costs and reasoning.
      'our fiber optic cable is 87 cents a foot, parts and labor included.')
footage = input('How many feet are expected for this installation?')
price_per_foot = .87
subtotal = round((int(footage)*price_per_foot), 2) # Calculate subtotal.
tax_rate = .095
tax = round((subtotal*tax_rate), 2)                # Calculate tax.
total = round((subtotal + tax), 2)                 # Sum tax and subtotal.
# This is the end of the user input and the start of the receipt printing.
print()
print()
print('RECEIPT OF PURCHASE')
print()
print('Customer Name:', cust_name) # I used commas instead of + to save space.
print('Project Name :', proj_name)
print('Company Name :', comp_name)
print()
print('Footage       :  ', footage, 'feet')
print('Price per foot: ', str(price_per_foot), '$/foot')
print('Subtotal      : $' + str(subtotal)) # Floats changed to strings.
print('Tax @ 9.5%    : $' + str(tax))      # Floats can not be printed.
print('Total         : $' + str(total))    # Concatenation requires same type.
