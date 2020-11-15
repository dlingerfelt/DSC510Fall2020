# DSC510
# Week 11 Assignment - Assignment_11.1.py
# Cash register program
# Author Sowmya Chavali
# 11/14/20

import locale
import getpass


# creating a class to handle item registery
class CashRegister:
    # init method to set the variables
    def __init__(self):
        self.count=0
        self.totalPrice=0
    # method to add items and corresponding prices to the cart
    def addItem(self, price):
        self.count = self.count + 1
        self.totalPrice = self.totalPrice + price
    @property
    def getCount(self):
        return self.count
    @property
    def getTotal(self):
        return self.totalPrice

def main():
    cart=CashRegister()
    # gets the username to display it in the welcome message
    UserName = getpass.getuser()
    print('------------------------------------')
    print("Welcome " + UserName)
    print("Input ADD/add/+ to add items to cart")
    print("Input exit to checkout")
    print('------------------------------------')
    while True:
        choice = input("Enter your choice:")
        if choice.lower() == 'add' or choice == '+':
            while True:
                try:
                    price = float(input("enter the price of the item : $"))
                    cart.addItem(price)
                except ValueError:
                    print("Enter a numeric value")
                else:
                    break
        elif choice.lower() == 'exit':
            print("-------------------------------------------")
            print("Number of items in the cart : {0} ".format(cart.getCount))
            # Formatting currency
            locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8')
            print("The total price             : "+locale.currency(cart.getTotal, grouping=True))
            print("-------------------------------------------")
            break
        else:
            print("Enter a valid input")
            continue

main()
