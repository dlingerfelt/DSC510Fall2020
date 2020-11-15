#DSC 510#
#Week 11#
#Programming Assignment Week 11#
#Author: Brett Sutow#
#11/09/2020#
#If changes made please fill-out log#
#Change:#
#Changes Made:#
#Date of Change:#
#Author:#
#Change Approved By:#
#Date Moved to Production:#
name= input("Hello! First what is your name?")
print("Welcome {name}, to Brett's Bold Clothing!".format(name=name))
class CashRegister:
    def __init__(self):
       self.totalprice=0
       self.itemcount=0

    def add_item(self, price):
        self.totalprice += float(price)
        self.itemcount += 1

    def gettotal(self):
       return self.totalprice
    def getcount(self):
        return self.itemcount


def main():
    cashregister = CashRegister()
    itempurchased = True
    while itempurchased:
        itempurchased= input('What item would you like to purchase: tanktop, sweatshirt, or t-shirt? Once complete write done\n')
        if itempurchased == "Tanktop":
            price= 5.99
            cashregister.add_item(price)
        if itempurchased == "tanktop":
            price= 5.99
            cashregister.add_item(price)
        if itempurchased == "tank top":
            price= 5.99
            cashregister.add_item(price)
        if itempurchased == "Tank Top":
            price= 5.99
            cashregister.add_item(price)
        if itempurchased == "Sweatshirt":
            price= 19.99
            cashregister.add_item(price)
        if itempurchased == "Sweat Shirt":
            price= 19.99
            cashregister.add_item(price)
        if itempurchased == "sweat shirt":
            price= 19.99
            cashregister.add_item(price)
        if itempurchased == "Sweat Shirt":
            price= 19.99
            cashregister.add_item(price)
        if itempurchased == "sweatshirt":
            price= 19.99
            cashregister.add_item(price)
        if itempurchased == "T-shirt":
            price= 9.99
            cashregister.add_item(price)
        if itempurchased == "T-Shirt":
            price= 9.99
            cashregister.add_item(price)
        if itempurchased == "t-shirt":
            price= 9.99
            cashregister.add_item(price)
        if itempurchased == "Tshirt":
            price= 9.99
            cashregister.add_item(price)
        if itempurchased == "tshirt":
            price= 9.99
            cashregister.add_item(price)
        if itempurchased == 'Done':
            print('Thank You! Have a Great Day!')
            print('The total cost would be $',cashregister.gettotal())
            print('The total amount of items being purchased:', cashregister.getcount())
            exit()
        if itempurchased == 'done':
            print('Thank You! Have a Great Day!')
            print('The total cost would be $',cashregister.gettotal())
            print('The total amount of items being purchased:', cashregister.getcount())
            exit()
        if itempurchased == 'D':
            print('Thank You! Have a Great Day!')
            print('The total cost would be $',cashregister.gettotal())
            print('The total amount of items being purchased:', cashregister.getcount())
            exit()
        if itempurchased == 'd':
            print('Thank You! Have a Great Day!')
            print('The total cost would be $',cashregister.gettotal())
            print('The total amount of items being purchased:', cashregister.getcount())
            exit()
        else :
            print('The total cost would be $',cashregister.gettotal())
            print('The total amount of items being purchased:', cashregister.getcount())
            selection = False


main()
