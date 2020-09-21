# DSC 510

# Week 3

# Programming Assignment Week 3 - 3_1_if_else_prog_asnmt.py

# Author Aditya Sumbaraju

# 09/19/2020

from tkinter import TRUE
from datetime import date

today = date.today()


# Color definitions
class color:
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    END = '\033[0m'


# Variable assignments block
svc_fee_default = 0.87
svc_fee_disc_gt_100 = 0.80
svc_fee_disc_gt_250 = 0.70
svc_fee_disc_gt_500 = 0.50
calc_cost_per_ft = 0
install_Cost = 0
val = 0
calc_cost_per_ft_default = float(svc_fee_default)
calc_cost_per_ft_gt_100 = float(svc_fee_disc_gt_100)
calc_cost_per_ft_gt_250 = float(svc_fee_disc_gt_250)
calc_cost_per_ft_gt_500 = float(svc_fee_disc_gt_500)

cust_nm = str(input(
    'Please enter your firstname and lastname:\n'))
""" 
1.cust_nm represents input variable to store CustomerName  
2.The sequence \n at the end of the prompt represents a newline
3.Expecting data in string format 
"""

print(color.BLUE + 'Welcome, ' + cust_nm.lower() + color.END)  # print the details provided by customer in bold

cust_cmpy_nm = str(input("What is your company's name?\n"))
# input variable to store CustomerCompanyName and expecting a string value

ft_rqt = input(
    'Please enter number of feet of fiber optic cable to be installed \n')
# expecting a float value; it could be a decimal value or a whole number.

# Feet requirement input evaluation block. The program exits on invalid input.
try:
    val = float(ft_rqt)
    print("Input is Valid")
except ValueError:
    if isinstance(ft_rqt, str) == TRUE:
        print(
            color.RED + "Invalid Input" + color.END + "\n Input value: " + color.RED + ft_rqt + color.END + color.BLUE + "\n Please enter a valid number > 0 to process the request" + color.END)
    exit()

# cost evaluation block based on number of feet requested as per assignment 3.1
if 0 < val <= 100:
    install_Cost = val * calc_cost_per_ft_default
    calc_cost_per_ft = svc_fee_default
elif 100 < val <= 250:
    install_Cost = val * calc_cost_per_ft_gt_100
    calc_cost_per_ft = svc_fee_disc_gt_100
elif 250 < val <= 500:
    install_Cost = val * calc_cost_per_ft_gt_250
    calc_cost_per_ft = svc_fee_disc_gt_250
elif val > 500:
    install_Cost = val * calc_cost_per_ft_gt_500
    calc_cost_per_ft = svc_fee_disc_gt_500
else:
    print('enter a valid number > 0')
    exit()

Receipt_date = today.strftime("%m/%d/%y")  # The USA date Format

# Receipt print section
print(
    color.BLUE + '===================================================================' + color.END)  # prints in blue and same class is applied across receipt details
print(color.BLUE + '                    Welcome to FIBER OPTIC                               ' + color.END)
print(color.BLUE + '                           Receipt                                 ' + color.END)
print(color.BLUE + 'Receipt Date:                                        ' + color.END + Receipt_date)
print(
    color.BLUE + 'User Name:                                           ' + color.END + cust_nm.lower())  # maintaining case consistency to lower by using lower()
print(
    color.BLUE + 'Company:                                             ' + color.END + cust_cmpy_nm.lower())
print(
    color.BLUE + 'Number of feet of fiber optic cable to be installed: ' + color.END + str(
        ft_rqt) + ' ft')  # while printing the value needs to be converted to string
print(color.BLUE + 'Calculated Cost per feet:                            ' + color.END + '$ ' + str("%.2f" %
                                                                                                    calc_cost_per_ft))  # Value provided in assignment 2.1
print(
    color.BLUE + 'Total Cost :                                         ' + color.END + '$ ' + "%.2f" % install_Cost)  # rounds the value and appends the $ symbol
print(color.BLUE + '===================================================================' + color.END)
print(color.BLUE + '                    Thank You Visit Again' + color.END)
exit()
