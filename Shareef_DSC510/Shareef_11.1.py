# DSC 510
# Week 11
# Programming Assignment Week 11
# Author Adonis Shareef
# 11/15/2020

# Change#: 5
# Change(s) Made: Class CashRegister with methods addItem,getCount, and getTotalPrice and OVveriding the __str__ method
# Date of Change: 11/15/2020
# Author: Adonis Shareef
# Change Approved by: Adonis Shareef
# Date Moved to Production: 11/15/2020
import locale
class CashRegister: #class for cash register
    def __init__(self): #constructor
        self.totalPrice = 0
        self.count = 0

    def addItem(self,price): #add item method to increase count by 1 and add the price to total price
        self.totalPrice += price
        self.count += 1
#getter methods for count and totalPrice which have property decorators
    @property
    def getCount(self):
        return self.count

    @property
    def getTotalPrice(self):
        return self.totalPrice

    def __str__(self): #ovveriding to print out the instanced objects information
        locale.setlocale( locale.LC_ALL, 'en_US.UTF-8')
        return 'Number of items in the cart:  {0}\nTotal Price: {1}'.format(self.getCount,locale.currency(self.getTotalPrice,grouping=True))

def main():
    ShoppingCart = CashRegister()
    while True:
        toShop = input('Welcome! Would you like to go shopping? (shop/exit)')
        if toShop.lower() == 'shop':
            while True:
                try:
                    itemPrice = float(input("How much does the item cost? $"))
                    ShoppingCart.addItem(itemPrice)
                except ValueError:
                    print('Please enter a numeric value: (2.34, 4.0, 5)')
                else:
                    break
        elif toShop.lower() == 'exit':  # break if user wants to stop
            print(ShoppingCart.__str__())
            print("Take care! Come shop with us again")
            break
        else:
            print("Please enter valid input(shop/exit)")
            continue


if __name__ == "__main__":
    main()
