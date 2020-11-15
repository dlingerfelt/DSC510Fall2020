# DSC 510
# Week 11
# Programming Assignment Week11 - Cash register program. User inputs items and prices, receives an item count and total cost when done.
# Author: David Brehm
# 11/15/2020

# Change Log:
# No changes.

import locale


class CashRegister:
    """
    Cash Register class.
    """
    def __init__(self):
        """
        Set count and total to 0.
        """
        self.count = 0
        self.total = 0

    def additem(self, price):
        """
        Add item price to the total.
        :param price: Price of the individual item.
        :return: No return.
        """
        self.total += price

    def getTotal(self):
        """
        Get total price of the cart.
        :return: totalPrice.
        """
        return self.total

    def getCount(self):
        """
        Get item count of the cart.
        :return: itemCount.
        """
        return self.count


def main():
    """
    Main function. Prompts the user for inputs then prints the item count and total cost when complete.
    :return: No return.
    """
    cr = CashRegister()  # Initialize cash register.
    locale.setlocale(locale.LC_ALL, '')  # Set location.
    print("Welcome! Enter one item then its decimal price separated by a comma per line. Enter 'Done' when you are finished.")

    while True:  # Main loop.
        temp = input()
        if temp == 'Done':  # Break loop if the user is done inputting values.
            break
        try:
            item, price = temp.split(',')  # Split input by item and price.
        except ValueError:
            print('Please enter an item and a price.')  # Error if there isn't two inputs.
            continue
        try:
            fprice = float(price)  # Convert price input to float.
            cr.additem(fprice)  # Add item to cash register.
            cr.count += 1  # Increment item count.
        except ValueError:
            print('Please enter a numerical value for the price.')

    cartcount = cr.getCount()  # Get number of items in cart.
    carttotal = cr.getTotal()  # Get total price of items in cart.

    print('You entered {} items totaling {}.'.format(cartcount, locale.currency(carttotal)))  # Print cart count and total cost.


if __name__ == "__main__":
    main()
