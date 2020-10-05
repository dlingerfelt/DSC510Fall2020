# DSC 510

# Week 5

# Programming Assignment Week 5 - 5_1_Programming_Assignment.py

# Author Aditya Sumbaraju

# 10/04/2020

# Change Control Log:

# Change#:1
# Change(s) Made: Added iteration check to check with user to perform operation or exit from the program
# Date of Change: 10/4/2020
# Author: Aditya Sumbaraju
# Change Approved by: Catie Williams
# Date Moved to Production: 10/5/2020


from datetime import date


# Color definitions
class color:
    RED = '\033[91m'
    END = '\033[0m'
    BLUE = '\033[94m'


today = date.today()
Receipt_date = today.strftime("%m/%d/%y")


# perform arithmetic operations  by passing one of the operators (+,-,/,*) as a parameter
# function validates non-numeric and divide by zero exceptions
def performCalculation(a_o):
    try:
        num1 = float(input("Enter Number 1: "))
        num2 = float(input("Enter Number 2: "))

        if a_o == "+":
            print("Addition of two numbers: " + str(
                num1 + num2))
        elif a_o == "-":
            print("Subtraction of two numbers: " + str(num1 - num2))
        elif a_o == "*":
            print("Multiplication two numbers: " + str(num1 * num2))
        elif a_o == "/":
            print("Division two numbers: " + str("%.2f" % (num1 / num2)))

    except ValueError:
        print(
            color.RED + "please avoid non-numeric values " + color.END)
    except ZeroDivisionError:
        print(color.RED + "divide by zero is infinite" + color.END)


# Function to calculate average of numbers and exceptions when it encounters non-numeric value and divide by zero exceptions.
# Prompts the user to enter count and list of numbers to calculate average
# calculates average based on numeric values and ignores none numeric values while calculation.
def calculateAverage():
    # default variable assignment
    a = 1
    cnt = 1
    try:
        a = []
        cnt = int(input("How many numbers you wish to enter: "))
        if cnt <= 0:
            print("Average calculated for the numbers entered :" + str(1 / cnt))
        else:
            for i in range(cnt):
                val = input("Number " + str(i + 1) + "=")
                a.append(int(val))  # appends values to the existing list
    except ValueError:
        print(color.RED + "please avoid non-numerics" + color.END)
    except ZeroDivisionError:
        print(color.RED + "divide by zero is infinite" + color.END)

    if cnt > 0:
        avg = sum(a) / int(cnt)
        print("values entered :" + str(a))
        print("sum of values : " + str(sum(a)))
        print("Calculated Average towards entered numberic values (ignoring non-numerics in list) :" + str(avg))
    else:
        print(color.RED + 'Please enter whole number' + color.END)
        pass


# function to print menu for Arithmetic Operations and Average of Numbers
def print_menu():
    print(" ==========Assignment5.2 - Arithmetic Operations and Average of Numbers =============\n")
    print(color.BLUE + 'Execution Date: ' + color.END + Receipt_date)
    print(" Choose one arithmetic operator from the list below:")
    print(color.BLUE + " 1. Please enter  '+' for Addition" + color.END)
    print(color.BLUE + " 2. Please enter  '-' for Subtraction" + color.END)
    print(color.BLUE + " 3. Please enter  '*' for Multiplication" + color.END)
    print(color.BLUE + " 4. Please enter  '/' for Division" + color.END)
    print(color.BLUE + " 5. Please enter  '!' for Average" + color.END)
    print(color.BLUE + " 6. Please enter any key other than +,-,*,/,!  to  Exit the program" + color.END)


# main program to process the arithmetic operations and calculate average
# prompts user to choose the operations from menu or quit the process.
if __name__ == '__main__':
    print_menu()
a_o = input("Enter one arithmetic operator: ")

while True:
    if a_o in ('+', '-', '*', '/'):
        performCalculation(a_o)
        check1 = input('want to try another operation? (y/n): ')
        if check1 == 'y':
            print_menu()
            a_o = input("Enter one arithmetic operator: ")
        elif check1 == 'n':
            exit()
    elif a_o == '!':
        calculateAverage()
        check2 = input('want to try another operation? (y/n):')
        if check2 == 'y':
            print_menu()
            a_o = input("Enter one arithmetic operator: ")
        elif check2 == 'n':
            exit()
    else:
        print("\n enter valid input from the menu and try again ")
        break
