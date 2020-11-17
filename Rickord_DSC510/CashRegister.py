#DSC 510
#Week 11
#Programming Assignment Week 11
#Author Jake Rickord
#11/14/2020

import string, locale

#new class
class CashRegister:
    ##each instance has numItems and order total that is unique
    def __init__(self):
        self.numItems=0
        self.order_total=0

    ##add count of new item and add price to order total
    def addItem(self, price):
        self.order_total=self.order_total+price
        self.numItems=self.numItems+1

    #return the total price
    def getTotal(self):
        return self.order_total

    #return the number of items purchased
    def getCount(self):
        return self.numItems

def input_check(user_input):
    #get in comparable form to a string quit
    user_input = user_input.translate(user_input.maketrans('','',string.punctuation))
    user_input = user_input.lower()
    user_input = user_input.rstrip()

    if(user_input == "quit"): return True
    else: return False

def pretty_print(cr):
    #set local currency
    locale.setlocale(locale.LC_ALL, '')

    print("The total number of items purchased was {}.".format(cr.getCount()))
    print("The value of those {} items totaled to {}.".format(cr.getCount(),locale.currency(cr.getTotal())))
    print("Thank you for shopping with us, have a wonderful day!")

#get num in comparable form by dropping $ sign and any trailing spaces
def numCheck(proxyValue):
    proxyValue=proxyValue.rstrip()
    proxyValue=proxyValue.lstrip('$')
    return proxyValue

def main():
    #set Sentinel value to false for recurring loop and instantiate an instance of cashregister
    sentinelValue = False
    mainRegister = CashRegister()

    #welcome message
    print("Welcome to our Store!")

    #initialcheck
    new_Price=input("Please enter the price of the first item purchased, else type 'quit': ")
    sentinelValue=input_check(new_Price)
    print()

    #recurring check to get in comparable form, try to add to list, if it's not a number print error message and try again
    while(sentinelValue != True):
        new_Price=numCheck(new_Price)
        try:
            new_Price=float(new_Price)
            if(new_Price>0):
                mainRegister.addItem(new_Price)
            else:
                raise ValueError()
        except:
            print("You entered a negative or non-numerical value other than quit, please try again!")
        print()
        new_Price=input("Please enter the price of the next item purchased. If order is complete, please type 'quit': ")
        sentinelValue=input_check(new_Price)


    if(mainRegister.getCount()>0):
        pretty_print(mainRegister)
    else: print("We're sorry we couldn't help you find anything today, come back soon!")

if __name__ == "__main__":
    main()
