# DSC510
# Week 5 Assignment - Assignment_5.1.py
# Program to perform Arithmetic operations
# Author Sowmya Chavali
# 10/03/20

import getpass

# Function to perform Arithematic operations like +,-,*,/
def performCalculation(opr):
    try:
        value1 = float(input("Enter first number: "))     # Validating the input values
        value2 = float(input("Enter second number: "))

        if opr == "+":
            print("\033[32m"+"Addition of given numbers: " + str(value1 + value2)+"\033[0m")     # Color coding the output to green with the code \033[32m
        elif opr == "-":
            print("\033[32m"+"Subtraction of given numbers: " + str(value1 - value2)+"\033[0m")
        elif opr == "*":
            print("\033[32m"+"Multiplication of given numbers: " + str(value1 * value2)+"\033[0m")
        elif opr == "/":
            print("\033[32m"+"Division of given numbers: " + str(value1 / value2)+"\033[0m")
    except ValueError:
        print("\033[31m" +"You have entered a non-numeric value. "+"\033[0m")  # Color coding the exceptions to red with the code \033[31m
    except ZeroDivisionError:
        print("\033[31m" +"Cannot divide by zero"+"\033[0m")


# Function to calculate average of numbers
def calculateAverage():
    try:
        count = int(input("To calculate average how many numbers you wish to enter: "))
        sum = 0
        for c in range(count):    # This loop iterates to the input count times which takes the numbers and calculates the sum
            sum = sum + float(input("Enter num"+ str(c+1) +": "))
        avg = sum / count
        print("\033[32m"+"Average calculated is :"+str(avg)+"\033[0m")
    except ValueError:
        print("\033[31m" +"You have entered a non-numeric value. "+"\033[0m")



# gets the username to display it in the welcome message
UserName = getpass. getuser()

print("--------------Welcome "+UserName+"---------------")
print("             Lets perform some calculations\n")
print("\033[33m" +" Choose one option from the list below:")   # Color coding the index in yellow with the code \033[33m
print("   + for Addition")
print("   - for Subtraction")
print("   * for Multiplication")
print("   / for Division")
print("   A for Average")
print("   Any other key to  Exit"+"\033[0m")
opr = input("Enter your choice: ")
# Based on the entered choices respective functions are called in this loop.
while True:
    if opr in ('+', '-', '*', '/'):
        performCalculation(opr)
    elif opr == 'A':
        calculateAverage()
    else:
        print("\nThanks for using the calculator! ")
        break      # Will exit from the program if the input is not in the list
    opr = input("Enter your choice again: ")
