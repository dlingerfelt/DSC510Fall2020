# File: rattanavilay_assignment_11.1.py
# Assignment: 11.1
# Course: DSC 510
# Week 11
# Programming Assignment Week 11
# Author: Thip Rattanavilay
# DATE: 11/15/2020



"""
This week we’re going to demonstrate our knowledge of Python object oriented programming concepts by creating a simple
 cash register program.

Your program must have a header.
Your program must have a welcome message for the user.
Your program must have one class called CashRegister.
Your program will have an instance method called addItem which takes one parameter for price. The method should also
keep track of the number of items in your cart.
Your program should have two getter methods.
getTotal – returns totalPrice
getCount – returns the itemCount of the cart
Your program must create an instance of the CashRegister class.
Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
Your program should print the total number of items in the cart.
Your program should print the total $ amount of the cart.
The output should be formatted as currency. Be sure to investigate the locale class. You will need to call
locale.setlocale and locale.currency.

"""


# Welcoming statement - Header
print("\n")
print("=================**==================")
print("Welcome to the Cash Register program")
print("=================**==================")
print("\n")
# Display Welcome Message to customer
Name = input("What is your name?")
print("")
# Display Welcome Message to customer
print("Welcome,", Name, "!")

import locale
class CashRegister:  # class name CashRegister
    count = 0
    total = 0

    def get_total(self):  # Get total
        locale.setlocale(locale.LC_ALL, 'en_US')  # US locale
        return locale.currency(self.total, grouping=True)

    def get_count(self):  # Get count
        return self.count

    def add_item(self, price):  # Add item
        self.count += 1
        self.total = self.total + price


# Display the cash register details
def display(register_obj):
    print("\n")
    print("--------------------------------------------------------")
    print(f'Number of items you added : {register_obj.get_count()}')
    print(f'Total Price:{register_obj.get_total()}')
    print("\n")
    print("========================================================")
    print("Thank you for coming to Cash Register, have a great day!")
    print("========================================================")


def main():
    print("\n")
    print("To complete your order.\n - Please Enter q, to calculate your total price -")
    print("\n")

    # creating cash register object
    cash_register = CashRegister()

    while True:
        try:
            price = input(f"Enter the price of item: ")
            if 'Q' == price.upper():
                break
            else:
                # Add price to cash register
                cash_register.add_item(float(price))

        except Exception as err:
            print(
                f'Invalid price Entered, Please check your price again: {err}')

    display(cash_register)


if __name__ == '__main__':
    main()
