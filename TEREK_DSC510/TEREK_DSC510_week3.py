#DSC 510
#Week 3
#Programming Assignment Week 3
#Author Kim Terek
#09/20/2020

print()
print('Hello and Welcome to the Fiber Optic Cabling Installation Program. Glad to be of help for you today.')
print()
print()
name = input('What is your company name? ') #USER INPUTS START HERE
print()
print('Great! We can take your order for ' + name + '. ')
f = input('How much feet of cable would you like to have installed? ')
c = .87

if int(f) > 250:
    c = c - .17
if int(f) <= 250 and int(f) > 100:
    c = c - .07

print('The price per feet for that amount is')
print('$')
print(c)
charge = int(f) * float(c) #cost per foot of installation calculation
print('So the total cost of installation for that much footage is')
print('$')
print(charge)

accept = input('Do you want to place this installation order? (Y/N): ')
print()# RECEIPT BEGINS HERE
if accept == "y" or accept == "Y":
    print('Ok, Your Order Summary is as follows:')
    print()
    print('Company name:')
    print(name)
    print("Number of feet of cable to install:")
    print(f)
    print("Cost for this cable installation:")
    print('$')
    print(charge)
    print()
    print('TOTAL COSTS for this ORDER (tax is 5%):')
    print('$')
    print(charge * 1.05)  # END OF RECEIPT
else: print("Ok, Please come back when ready to order.")

print('Have a good day.')



