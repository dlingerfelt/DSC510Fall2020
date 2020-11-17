# DSC 510

# Week 11

# Programming Assignment Week 11 - 11_1_Programming_Assignment.py

# Author Aditya Sumbaraju

# 11/15/2020

# Change Control Log:

# Change#:1
# Change(s) Made: Added iteration check to check with user to perform operation or exit from the program
# Date of Change: 11/15/2020
# Author: Aditya Sumbaraju
# Change Approved by: Catie Williams
# Date Moved to Production: 11/15/2020

import locale


# Color definitions
class color:
    RED = '\033[91m'
    END = '\033[0m'
    BLUE = '\033[94m'


# cash register class to add an item to basket, get the count of items added to basket and calculate the total price of items.
class CashRegister:
    def __init__(self):  # constructor
        self.totalPrice = 0
        self.count = 0

    def addItem(self, price):
        self.totalPrice += price
        self.count += 1

    def getCount(self):
        return self.count

    def getTotal(self):
        return self.totalPrice


# function calls locale to print the value in local currency
def pretty_print(cashReg):
    locale.setlocale(locale.LC_ALL, '')
    print("The total number of items added to basket : {} \n  Total cost is : {}.".format(cashReg.getCount(),
                                                                                                locale.currency(
                                                                                                    cashReg.getTotal())))
    print("*** Please visit again ***")


# main function calls the CashRegister based on the input provided by cashier
def main():
    basket = CashRegister()
    print('Hello Cashier- please collect the items from customer and add the items to the basket')
    while True:
        in_basket = input("select 'a' to add item and 'q' to exit:").lower()
        if in_basket == 'a':
            while True:
                try:
                    in_price = input("enter item cost: $")
                    symbol = in_price[0:1]
                    if symbol == "-":
                        print(
                            color.RED + "Are you trying to remove the item - please repeat the process by adding correct values this time" + color.END)
                        exit()
                    else:
                        basket.addItem(float(in_price))
                except ValueError:
                    print(color.RED +'Please enter valid value'+ color.END)
                else:
                    break
        elif in_basket == 'q':
            pretty_print(basket)
            break
        else:
            print(color.RED + "please use a to add and q to exit" + color.END)
            continue


if __name__ == "__main__":
    main()
