#DSC 510
#Week 4
#Programming Assignment Week 4
#Author Kim Terek
#09/27/2020

import math
print()
print('Hello and Welcome to the Fiber Optic Cabling Installation Program. Glad to be of help for you today.')
print()
print()
name = input('What is your company name? ') #USER INPUTS START HERE
print()
print('Great! We can take your order for ' + name + '. ')
#price ranges
#range1 = "under 100ft"
prrange1 = float(.87)

#range2 = "mid_price"
prrange2 = float(.80)

#range3 = "low_price"
prrange3 = float(.70)

f = int(input('How much feet of cable would you like to have installed? '))
if f < 100:
    p = prrange1
elif f >= 100 and f < 250:
    p = prrange2
else:
    p = prrange3

#SECTION FOR FN1 defined: cost_calc
def cost_c (f, p):
    cost = f * p
    return cost

print("Total cost for these feet installed: ")
#SECTION for executing (calling) FN1:
print('$',cost_c(f, p))

#print(name('range'))

#charge = int(f) * float(c) #cost per foot of installation calculation
#print('So the total cost of installation for that much footage is')
#print('$')
#print(charge)

accept = input('Do you want to place this installation order? (Y/N): ')
print()# RECEIPT BEGINS HERE
if accept == "y" or accept == "Y":
    print('Ok, Your Order Summary is as follows:')
    print()
    print('Company name:', name)
    print("Number of feet of cable to install:",f)
    formattedchargeperft = format(p,",.2f")
    print("Cost per foot being charged:",'$',formattedchargeperft)
    print("Cost for this cable installation:",' $',cost_c(f, p))
    print()

   # currency = "${:,}".format(cost_c(f,prrange))
   # print(currency)
    formattedtaxtotalamt = format((cost_c(f, p)* 1.05),",.2f")
    print('TOTAL COSTS for this ORDER (tax is 5%):')
    print('$',formattedtaxtotalamt)
    print()
   # currency = "${:,}".format(cost_c(f,prrange) * .05)
   # print(currency)
    # END OF RECEIPT
else:
    print("Ok, Please come back when ready to order.")

print('Have a good day.')



