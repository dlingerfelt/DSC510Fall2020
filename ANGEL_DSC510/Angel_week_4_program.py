# DSC 510
# Week 4
# Programming Assignment Week 4
# Author Daniel Angel
# 09/27/2020
# 1st block collects customer information including name and footage.
print('Hello. Welcome to this fiber optic installation estimator.')
cust_name = input('What is your name?')  # Ask user to input info.
proj_name = input('Does your project have a name? If not, leave blank')
comp_name = input('Please write your company name')
print('We have discounts. The more you buy the more you save.')
footage = input('How many feet of cable do you need?')
footage = int(footage)
print('RECEIPT OF PURCHASE')
print('Customer Name is: '+cust_name)
print('Project Name is: ' + proj_name)
print('Company Name is: ' + comp_name)


def cost_calculator(footage, price_per_foot):
    # Function Calculates Cost.
    subtotal = footage * price_per_foot
    print('Footage of project is: ', footage, 'feet')
    print('Price per foot is: $', "{:.2f}".format(price_per_foot), 'per foot')
    print('Subtotal is $', "{:.2f}".format(subtotal))
    print('Tax at 9.5% is $', "{:.2f}".format(subtotal*.095))
    print('Total is $', "{:.2f}".format(subtotal*1.095))
    return


if footage <= 100:              # Else-If conditional ladder.
    price_per_foot = .87
    cost_calculator(footage, price_per_foot)
elif footage <= 250:
    price_per_foot = .8
    cost_calculator(footage, price_per_foot)
elif footage <= 500:
    price_per_foot = .7
    cost_calculator(footage, price_per_foot)
else:
    price_per_foot = .5
    cost_calculator(footage, price_per_foot)

