# DSC 510

# Week 2

# Programming Assignment Week 2 - 2_1_programming_assignment.py

# Author Aditya Sumbaraju

# 09/08/2020

class color:
    BLUE = '\033[94m'  # Color class:BLUE prints the line in blue
    BOLD = '\033[1m'  # Color class:BOLD prints the line in bold text
    END = '\033[0m'  # class:END; ends the color on a given line issued to print


svc_fee = 0.87  # service fee 'svc_fee' is hard code value provided in assignment 2.1.
calc_cost_per_ft = float(svc_fee)

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

ft_rqt = float(input(
    'Please enter number of feet of fiber optic cable to be installed \n'))
# expecting a float value; it could be a decimal value or a whole number.

install_Cost = ft_rqt * calc_cost_per_ft
# installation cost is calculated by multiplying the number of feet times $0.87

# Receipt print section
print(
    color.BLUE + '===================================================================' + color.END)  # prints in blue and same class is applied across receipt details
print(color.BLUE + '                    Welcome to FIBER OPTIC                               ' + color.END)
print(color.BLUE + '                           Receipt                                 ' + color.END)
print(
    color.BLUE + 'User Name:                                           ' + color.END + cust_nm.lower())  # maintaining case consistency to lower by using lower()
print(
    color.BLUE + 'Company:                                             ' + color.END + cust_cmpy_nm.lower())
print(
    color.BLUE + 'Number of feet of fiber optic cable to be installed: ' + color.END + str(
        ft_rqt) + ' ft')  # while printing the value needs to be converted to string
print(color.BLUE + 'Calculated Cost per feet:                            ' + color.END + '$ ' + str(
    calc_cost_per_ft))  # Value provided in assignment 2.1
print(
    color.BLUE + 'Total Cost :                                         ' + color.END + '$ ' + "%.2f" % install_Cost)  # rounds the value and appends the $ symbol
print(color.BLUE + '===================================================================' + color.END)
print(color.BLUE + '                    Thank You Visit Again' + color.END)
exit()
