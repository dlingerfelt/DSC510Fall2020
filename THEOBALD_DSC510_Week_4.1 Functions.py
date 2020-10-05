# DSC510
# Week 4
# Programming Assignment Week 3
# Author Ammy Theobald
# 09/27/2020

# Get Name, Company and Cable Length Required
name = input('What is your name?\n')
company = input('Please enter your company name: ')
print('')
print('Welcome to the Fiber Optic Cost Calculator', name, 'with', company)
print('')


def fiber_cost():
    """Calculate cost less discount based on user input for length in feet and provide estimate."""
    length = float(input('How many feet of Fiber Optic Cable do you require? '))
    base_cost = .87
    discount_tier1 = (length) * .07
    discount_tier2 = (length) * .10
    discount_tier3 = (length) * .30
    total_base_cost = (length) * (base_cost)
    total_discount_tier1 = (length * base_cost) - discount_tier1
    total_discount_tier2 = (length * base_cost) - discount_tier2
    total_discount_tier3 = (length * base_cost) - discount_tier3

    if length <= 100:
        print('Your total cost is: $ %.2f' % total_base_cost)
        print('You are only', 101 - length, 'feet away from Discount Tier 1!')
        print('*********     THANKS FOR YOUR BUSINESS!!!!     *********')
        return total_base_cost
    elif length > 100 and length <= 250:
        print('Total base cost for your order is: $ %.2f' % total_base_cost)
        print('Your total discount is: $ %.2f' % discount_tier1)
        print('Your final cost is: $ %.2f' % total_discount_tier1)
        print('You are only', 251 - length, 'feet away from Discount Tier 2!')
        print('*********     THANKS FOR YOUR BUSINESS!!!!     *********')
        return total_discount_tier1
    elif length > 250 and length <= 500:
        print('Total base cost for your order is: $ %.2f' % total_base_cost)
        print('Your total discount is: $ %.2f' % discount_tier2)
        print('Your final cost is: $ %.2f' % total_discount_tier2)
        print('You are only', 501 - length, 'feet away from Discount Tier 3!')
        print('*********     THANKS FOR YOUR BUSINESS!!!!     *********')
        return total_discount_tier2
    else:
        print('Total base cost for your order is: $ %.2f' % total_base_cost)
        print('Your total discount is: $ %.2f' % discount_tier3)
        print('Your final cost is: $ %.2f' % total_discount_tier3)
        print('How exciting!!! You are receiving our best discounted rate!')
        print('*********     THANKS FOR YOUR BUSINESS!!!!     *********')
        return total_discount_tier3


fiber_cost()
