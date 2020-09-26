# DSC 510

# Week 4

# Programming Assignment Week 4 - 4_1_function_assignment.py

# Author Aditya Sumbaraju

# 09/24/2020

from datetime import date


# Color definitions
class color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    END = '\033[0m'


# Variable assignments block
svc_fee_default = 0.87
svc_fee_disc_gt_100 = 0.80
svc_fee_disc_gt_250 = 0.70
svc_fee_disc_gt_500 = 0.50
calc_cost_per_ft_default = float(svc_fee_default)
calc_cost_per_ft_gt_100 = float(svc_fee_disc_gt_100)
calc_cost_per_ft_gt_250 = float(svc_fee_disc_gt_250)
calc_cost_per_ft_gt_500 = float(svc_fee_disc_gt_500)
today = date.today()
Receipt_date = today.strftime("%m/%d/%y")  # The USA date Format
disc_cost_per_ft = 0
total_cost = 0


# Function to print banner
def print_banner():
    print(
        color.BLUE + '===================================================================' + color.END)  # prints in blue and same class is applied across receipt details
    print(color.BLUE + '                    Welcome to FIBER OPTIC                               ' + color.END)
    print(color.BLUE + '===================================================================' + color.END)
    return 0


# A function call to print banner
print_banner()

# Data input block
cust_nm = str(input(
    'Please enter your firstname and lastname:\n'))
""" 
1.cust_nm represents input variable to store CustomerName  
2.The sequence \n at the end of the prompt represents a newline
3.Expecting data in string format 
"""
print(color.BLUE + 'Welcome, ' + cust_nm.lower() + color.END)  # print the details provided by customer in bold

cust_cmpy_nm = str(input("What is your company's name?\n"))


# Function to accept the feet requirement and default cost and evaluates the discounted prices based on the feet requirement from user
def install_cost(ft_rqt, cost_rqt):
    if 100 < round(float(ft_rqt)) <= 250:
        calc_cost_per_ft = calc_cost_per_ft_gt_100
    elif 250 < round(float(ft_rqt)) <= 500:
        calc_cost_per_ft = calc_cost_per_ft_gt_250
    elif round(float(ft_rqt)) > 500:
        calc_cost_per_ft = calc_cost_per_ft_gt_500
    else:
        calc_cost_per_ft = cost_rqt

    total_install_cost = (
            round(float(
                ft_rqt)) * calc_cost_per_ft)  # Rounds the feet requirement if entered in decimal value and calculate the cost
    return total_install_cost, calc_cost_per_ft


# Feet requirement validation block.
while True:
    try:
        ft_rqt = float(input(
            "Please enter number of feet of fiber optic cable to be installed: \n"))
        if ft_rqt <= 0:
            raise ValueError
    except ValueError:
        print(
            color.RED + "Invalid Input -  Please enter a valid number > 0 to process the request" + color.END)
    else:
        total_cost, disc_cost_per_ft = install_cost(ft_rqt,
                                                    svc_fee_default)
        break


# Function to print the receipt
def print_receipt():
    print_banner()  # function call to print the banner
    print(color.BLUE + '                           Receipt                                 ' + color.END)
    print(color.BLUE + 'Receipt Date:                                        ' + color.END + Receipt_date)
    print(
        color.BLUE + 'User Name:                                           ' + color.END + cust_nm.lower())  # maintaining case consistency to lower by using lower()
    print(
        color.BLUE + 'Company:                                             ' + color.END + cust_cmpy_nm.lower())
    print(
        color.BLUE + 'Number of feet of fiber optic cable to be installed (rounded value): ' + color.END + str(
            round(ft_rqt)) + ' ft')  # while printing the value needs to be converted to string
    print(color.BLUE + 'Calculated Cost per feet:                            ' + color.END + '$ ' + str("%.2f" %
                                                                                                        disc_cost_per_ft))  # Value provided in assignment 2.1
    print(
        color.BLUE + 'Total Cost :                                         ' + color.END + '$ ' + str(
            "%.2f" % total_cost))  # rounds the value and appends the $ symbol
    print(color.BLUE + '===================================================================' + color.END)
    print(color.BLUE + '                    Thank You Visit Again' + color.END)


if __name__ == '__main__':
    print_receipt()  # function call to print the receipt
