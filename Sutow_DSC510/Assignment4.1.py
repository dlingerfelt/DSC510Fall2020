#DSC 510#
#Week 4#
#Programming Assignment Week 4#
#Author: Brett Sutow#
#9/21/2020#
#Please input your company name below#
#Says hello to company#
print('Hello!')
name = input('What is your company name?')
#Introduces company#
print("Welcome {name}! Let's find out more information!".format(name = name))
#Input feet to calculate the price of perfoot#
feet = float(input('Enter feet needed: '))
if feet < 100:
    price = .87
elif 250 > feet > 99:
    price = .80
elif 500 > feet > 249:
    price = .70
elif feet > 499:
    price = .50
#Following is defining totalcost() as the formula for measurement and cost#
def total_cost(feet,price):
    cost=(feet*price)
    return(cost)
totalcost=total_cost(feet,price)
#Repeats feet, price perfoot, and presents the total cost#
print('Feet needed {feet:.0f}ft price perfoot is ${price:.2f}.'.format(**locals()))
print('Total cost is ${totalcost:.2f}.'.format(**locals()))
#Thanks customer#
print('Thank you {name} for your purchase!'.format(name = name))
