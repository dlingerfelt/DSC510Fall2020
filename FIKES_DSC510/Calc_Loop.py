# DSC510 Week 5 Assignment
# Calculate with loops
# Author: Matthew Fikes
# 9/30/2020

import statistics

# Function to check arithmetic operator to use for calculation
def performCalculation(operation):
    value1 = input("Enter first number:")
    value2 = input("Enter second number:")

    if operation == "+":
        print(value1 + "+" + value2 + "=" + str(int(value1) + int(value2)))
    elif operation == "-":
        print(value1 + "-" + value2 + "=" + str(int(value1) - int(value2)))
    elif operation == "*":
        print(value1 + "*" + value2 + "=" + str(int(value1) * int(value2)))
    elif operation == "/":
        # Catch any attempts to divide by zero
        try:
            print(value1 + "/" + value2 + "=" + str(int(value1) / int(value2)))
        except ZeroDivisionError:
            print("Cannot divide by zero")


# Function for averaging n items entered by user
def calculateAverage():
    enteredValues = []  # Create an empty list to hold inputs
    inputCount = int(input("How many values do you want to average?"))
    for i in range(inputCount):
        avgValue = int(input("Input value " + str(i + 1) + ":"))
        enteredValues.append(avgValue)  # append entered value to existing list for calculations

    print("Entered values: " + str(enteredValues))
    print("The mean of the values entered is: " + str(statistics.mean(enteredValues)))
    print("The median of the values entered is: " + str(statistics.median(enteredValues)))


# Create program loop
while True:
    calcType = input("Enter operation you wish to perform (+, -, *, /, avg, anything else to quit):")
# Handle user input of operation to run the right function or exit loop
    if calcType in ["+", "-", "/", "*"]:
        performCalculation(calcType)
    elif calcType == 'avg':
        calculateAverage()

    else:
        break
