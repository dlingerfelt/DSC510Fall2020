# DSC510 Week 11 Assignment - Cash_Register.py
# Cash Register program
# Author: Matthew Fikes
# 11/9/20


import datetime
import sys

# class to handle register items
class CashRegister:
# create init settings for class
    def __init__(self):
        self.cartsize = 0
        self.cartinventory = {}
        self.total = 0
        self.tax = 7.25

# class method to add new item to cart
    def addItem(self,name,price,quantity):
        self.cartsize += 1*quantity
        self.total += price*quantity
        self.cartinventory[name]=[price,quantity]
        print("--Item(s) added to cart")

# class method to decrease item quantity from cart
    def removeItem(self,name,quantity):
        if self.cartinventory[name][1]>= quantity:
            self.cartsize -= 1*quantity
            self.total -= self.cartinventory[name][0]*quantity
            self.cartinventory[name][1] = self.cartinventory[name][1]-quantity
            print("--Item(s) removed from cart")
        else:
            print("Not enough to remove")
            return

        if self.cartinventory[name][1] == 0:
            del self.cartinventory[name]

# class method to increase item quantity to cart
    def addQuantity(self,name,quantity):
            self.cartsize += 1*quantity
            self.total += self.cartinventory[name][0]*quantity
            self.cartinventory[name][1] = self.cartinventory[name][1]+quantity
            print("--Item(s) added to cart")

# class method to set a new price
    def setPrice(self,name,price):
        for i in self.cartinventory:
            self.cartinventory[name][0] = float(price)
            return

# class methodcheck cart contents and subtotal
    def checkCart(self):
        field_length = 51
        print("Items in cart: ",int(self.cartsize))
        print("-"*field_length)
        for i,v in self.cartinventory.items():
            quantity = (v[1])
            price = (v[0])
            price_string = "${0:0.2f}/ea".format(price)
            chars = 21+1+len(str(int((v[1]))))+2+len(price_string)
            spaces = field_length-chars
            receipt_line = ("{0:20}({1}){2:{spaces}}@ {3}".format(i,int(quantity),'',price_string,spaces=spaces))
            print(receipt_line)

        print("-"*field_length)
        sub_string = str('${0:.2f}'.format(self.getTotal()))
        print("Cart subtotal:{gap:{spaces}}{subtotal}".format(gap='',subtotal=sub_string, spaces=field_length-len(sub_string)-14))
        print("Tax rate:{gap:{spaces}}{tax}%".format(gap='',tax=register.tax,spaces=field_length-len(str(register.tax))-10))

        tax = register.getTotal()*(register.tax/100)
        total_cost = str("${0:.2f}".format(tax + register.getTotal()))
        print("Grand total:{gap:{spaces}}{total}".format(gap='',total=total_cost,spaces=field_length-len(total_cost)-12))

    def findItem(self,item):
        for i,v in self.cartinventory.items():
            if i==item:
                print("Item {0} is in cart with quantity {1}".format(i,int(v[1])))
                return True

# class method to add up cart, return total
    def getTotal(self):
        self.total = 0
        for i,v in register.cartinventory.items():
            self.total += v[0]*v[1]
        return(self.total)

# complete checkout, print receipt, clear register
def CheckOut(register):
    orig_stdout = sys.stdout #save original output

    with open('receipt.txt','w') as r: # loop to write receipt to file
        sys.stdout = r #set output to file instead for print commands
        register.checkCart()

        sys.stdout = orig_stdout #restore default output
    print("Receipt saved to file")
    register.__init__()
    input("Cart emptied - press Enter to start new checkout")
    Welcome()

# function to validate inputs
def InputValidator(prompt, *args):
# Arg values
# -a: Alphabetic only
# -n: Numeric only
# -np: Numeric, positive numbers only
# -nz: Numeric, no zeroes
    while True:
        user_input = input(prompt)
        arguments = args
        for i in range(len(arguments)):
            if '-a' in arguments[i]:

                if str.isalpha(user_input):
                    valid_input = user_input
                    return valid_input
                else:
                    print("Input needs to be alphabetic")
                    break
            elif '-n' in arguments[i]:
                if str.isnumeric(user_input):
                    valid_input = user_input
                    return valid_input
                else:
                    print("Input needs to be numeric")
                    break
            elif '-np' in arguments[i]:
                try:
                    float(user_input)
                    if float(user_input)>0:
                        valid_input = float(user_input)
                        return valid_input
                    else:
                        print("Input needs to be a positive number")
                        break

                except:
                    print("Input needs to be a number")
                    break
            elif '-nz' in arguments[i]:
                if str.isnumeric(user_input):
                    if float(user_input)==0:
                        print("Input needs to be a non-zero number")
                        break
                else:
                        valid_input = user_input
                        return valid_input
            else:
                valid_input = user_input
                return valid_input

# Manager Sale Function - Price change on entered item in cart, all quantity
def Mgr_Sale(mgr_ID):
    for i,v in register.cartinventory.items():
        print(i)
    item_sel = InputValidator("Enter item to reprice: ",[])
    for i,v in register.cartinventory.items():

        while item_sel == i:
            old_price = v[0]
            print("Current price is ${0:.2f}".format(old_price))
            new_price =input("Enter new unit price: ")
            register.setPrice(item_sel,new_price)
            log_string="Manager {0} changed {1} from ${2:.2f} to ${3:.2f}".format(mgr_ID,item_sel,float(old_price),float(new_price))
            ManagerLog(log_string)
            return


    input("Item not found - press Enter to continue")
    return

# Manager Discount Function - Percent discount off entered item.
def Mgr_Disc(mgr_ID):
    for i,v in register.cartinventory.items():
        print(i)
    item_sel = InputValidator("Enter item for discount: ",[])
    if register.findItem(item_sel):

        old_price = v[0]
        print("${0:.2f}".format(v[0]))
        discount =float(input("Enter percentage of sale: "))
        new_price = old_price -(old_price*(discount/100))
        print("New price is ${0:.2f} with a {1}% discount".format(new_price,discount))
        register.setPrice(item_sel,new_price)
        log_string="Manager {0} applied a {4}% discount to {1}, changing price from ${2:.2f} to ${3:.2f}".format(mgr_ID,item_sel,float(old_price),float(new_price),discount)
        ManagerLog(log_string)
    else:
        print("Item not found")
        return

# print Manager Menu
def ManagerWelcome(mgr_ID):
    print("---------------------------------------------------")
    print("   CashCo. Cash Register Program - MANAGER MODE")
    print("---------------------------------------------------")
    print(" Welcome Manager {0}!".format(mgr_ID))
    print("  Choose from the following options:")
    print("     1. Set unit sale price")
    print("     2. Set discount percentage")
    print("     3. Change tax rate")
    print("     4. Close register")
    print("\nAny other input will return to register mode     ")

    print("\nPer corporate policy, any changes made will be ")
    print(" recorded to your ID on a log.")
    print("---------------------------------------------------")

# Manager Mode input loop
def ManagerMode(register, mgr_ID):

    while True:
        ManagerWelcome(mgr_ID) # run manager menu
        mgr_input=InputValidator("Enter selection: ",[])
        if mgr_input=='1':
            Mgr_Sale(mgr_ID)
        elif mgr_input=='2':
            Mgr_Disc(mgr_ID)
        elif mgr_input=='3':
            curr_tax = register.tax
            print("Current tax rate is {0}".format(register.tax))
            new_tax =float(InputValidator("Enter new tax rate: ",['-np']))
            register.tax = new_tax
            log_string="Manager {0} changed tax rate from %{1} to %{2} ".format(mgr_ID,curr_tax,new_tax)
            ManagerLog(log_string)
        elif mgr_input=='4':
            sys.exit("Session complete")
            break

        else:
            Welcome()
            break

# print welcome menu
def Welcome():
    print("---------------------------------------------------")
    print("           CashCo. Cash Register Program")
    print("---------------------------------------------------")
    print("∙Input item, price and quantity to add to cart")
    print("∙Input blank item to view cart")
    print("∙Input '-' followed by item for removal")
    print("∙Input '+' followed by item for addition")
    print("∙Input * for manager console")
    print("∙Input 'checkout' to check out cart")
    print("---------------------------------------------------")

# Register Item Entry Input
def ItemEntry(register):
    while True:
        item_prompt = InputValidator("Enter Item: " ,[])
        item_input = item_prompt

# go to checkout
        if item_input.lower()=='checkout':
            CheckOut(register)

# item removal
        elif item_input.startswith('-'):
            for i,v in register.cartinventory.items():

                if item_input[1:]==i:
                    print("There are {0} {1} in the cart.".format(int(v[1]),i))
                    qty_input = InputValidator("Enter quantity to remove: ",['-np'])
                    register.removeItem(item_input[1:],qty_input)
                    break
                else: "Item not found in cart"

# item increase quantity
        elif item_input.startswith('+'):
            for i,v in register.cartinventory.items():

                if item_input[1:]==i:
                    print("There are {0} {1} in the cart.".format(int(v[1]),i))
                    qty_input = InputValidator("Enter quantity to add: ",['-np'])
                    register.addQuantity(item_input[1:],qty_input)
                    break
                else: "Item not found in cart"

# manager mode
        elif item_input.startswith('*'):
            mgr_ID = InputValidator("Enter Manager ID: ",[])
            ManagerMode(register,mgr_ID)
# item entry
        elif len(item_input) > 0:
            if register.findItem(item_input) == True: return
            price_input = (InputValidator("Unit price: $",['-np']))

            qty_input = (InputValidator("Quantity: ",['-np']))
            register.addItem(item_input,price_input,qty_input)
# check inventory
        else: register.checkCart()

# write manager log to file
def ManagerLog(text):
    with open('manager_log.txt','a') as log:
        log.write("{0}, timestamp: {1}\n".format(text,datetime.datetime.now()))

def main(register):
    ItemEntry(register)

register = CashRegister()
Welcome()

while True:
    main(register)
