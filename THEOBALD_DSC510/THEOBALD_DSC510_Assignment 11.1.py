#DSC510
#Week 11
#Programming Assignment Week 11
#Author Ammy Theobald
#11/15/2020

#Change#:1
#Change(s) Made: Initial Program
#Date of Change: 11/15/2020
#Author: Ammy Theobald
#Change Approved by: N/A
#Date Moved to Production: 11/15/2020

import locale

# Create a CashRegister class
class CashRegister:
    def __init__(self):
        self.numItems=0
        self.totalPrice=0.0

# Create a CashRegister class
class CashRegister:
    def __init__(self):
        self.numItems=0
        self.totalPrice=0.0

# Create Method addItem for customer to input item cost and add to running total.
# Also increments numItems by 1
    def addItem(self, price):
        self.numItems += 1
        self.totalPrice += price

    def getTotal(self):
        return self.totalPrice

    def getCount(self):
       return self.numItems


#calls locale to print value in local currency format
def pretty_print(register):
    locale.setlocale(locale.LC_ALL, '')
    print('')
    print('The total # items added to your cart: {} \n Your total cost today is: {}.'.format(register.getCount(),locale.currency(register.getTotal())))
    print('*** Thanks for your business!!! ***')

# Main Program
def main():
    #creating an instance of CashRegister class
    register = CashRegister()

    print('Greetings!! Please add the items to your shopping cart.')
    while True:
        item = input("Please enter 'A' to add item or Q if finished: ").lower()
        if item == 'q':
            pretty_print(register)
            break
        elif item == 'a':
            cost = float(input('Please enter cost of your item: '))
            register.addItem(cost)
        else:
            print('Oops! Something went wrong. Please try again.')


if __name__=='__main__':
    main()


