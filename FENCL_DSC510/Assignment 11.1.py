# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Riley Fencl
# 11/7/2020

import locale

locale.setlocale(locale.LC_ALL, 'en_US')


class CashRegister:
    def __init__(self, count=0, total=0):
        self.registertotal = total
        self.registercount = count

    def getTotal(self):
        return self.registertotal

    def getCount(self):
        return self.registercount

    def additem(self, price):
        self.registercount += 1
        self.registertotal += price


def main():
    print("Howdy! Welcome to Cash Register Program!")
    user_register = CashRegister()
    user_action = {}
    while user_action != "quit":
        user_action = input("Would you like to add an item to your shopping cart? (Type Quit to exit).\n").lower()
        if user_action == "quit":
            break
        elif user_action != "yes":
            print("Please enter either yes or quit")
            continue
        user_input = float(input("Please enter the price of your item (No $ is necessary).\n"))
        user_register.additem(user_input)
    print("Thanks for using my program!\n"
          "Here are the totals for your shopping cart!")
    print("-------------------------------------------")
    print("Shopping Cart Quantity: ", user_register.getCount(), "item(s)")
    print("Shopping Cart Total: ", locale.currency(user_register.getTotal()))


main()
