# File: rattanavilay_assignment_5.1.py
# Assignment: 5.1
# Course: DSC 510
# Week 5
# Programming Assignment Week 5
# Author: Thip Rattanavilay
# DATE: 10/3/2020

"""

This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
This program will contain a variety of loops and functions.
The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
This function will print the calculated value for the end user.
Define a function named calculateAverage which takes no parameters.
This function will ask the user how many numbers they wish to input.
This function will use the number of times to run the program within a for loop in order to calculate the total and average.
This function will print the calculated average.
This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
The main program should prompt the user for the operation they wish to perform.
The main program should evaluate the entered data using if statements.
The main program should call the necessary function to perform the calculation.

"""

print("Welcome to Arithmetic World!")  # Welcoming statement
print("")

Name = input("What is your name?")  # Display Welcome Message to customer
print("")
# Display Welcome Message to customer
print("Welcome,", Name, "!")


def getResponse():

    # This function asks user if they want to continue with the program

    response = input('Would you like to continue? Yes "y" or NO "n"')
    # give the user 5 times to input correct response before ending the program
    for i in range(5):
        # If user enters n, the program will end and print thank you!
        if response == "n":
            print("Thank You!")
            return False
        # If user enters y, the program continue to operator selection menu
        elif response == "y":
            return True
        # If user enters other than y or n, the program reiterates
        else:
            response = input('Please enter Yes "y" or No "n"')
            continue


def getOperator():

    # This function asks user to choose an operation to perform and returns the operator

    operators = ['+', '-', '*', '/', 'avg']
    while True:
        print("")
        print("Here are your Operations selection")
        print("--------------------------")
        print("")
        print("+ = Addition")
        print("- = Subtraction")
        print("* = Multiplication")
        print("/ = Division")
        print("avg = Average")
        print("")
        print("--------------------------")
        # Enter operations here
        print("Enter one of the following Arithmetic Operations:")
        Input_operator = input()
        if Input_operator in operators:
            return Input_operator
        else:
            continue


def performCalculation(operator):

    # Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
    print("")
    # Input first number
    Number1 = float(input('Please Enter First Number: \n'))
    # Input second number
    Number2 = float(input('Please Enter Second Number: \n'))
    while True:
        # If operator is +, the 2 numbers will be added
        if operator == "+":
            result = Number1 + Number2
            print("")
            print("Result =", round(result, 2))
        # If operator is -, the 2 numbers will be subtracted
        elif operator == "-":
            result = Number1 - Number2
            print("")
            print("Result =", round(result, 2))
        # If operator is *, the 2 numbers will be multiplied
        elif operator == "*":
            result = Number1 * Number2
            print("")
            print("Result =", round(result, 2))
        # If operator is /, the 2 numbers will be divided
        elif operator == "/":
            result = Number1 / Number2
            print("")
            print("Result =", round(result, 2))
        return


def calculateAverage():

    # This function calculates the average for total numbers inputted by the user

    print("Calculating the average for total numbers entered")
    while True:
        try:
            # Prompts user to input total numbers for the list
            count = int(
                input('How many total numbers do you want to enter: \n'))
            # Will tell user to enter number a different number greater than 0, if user enters a 0
            if count == 0:
                print("")
                print("Enter number greater than 0")
                continue
            break
            # Prompts user to enter an integer only
        except ValueError:
            print("")
            print("Not an integer, try again!")
    sum_number = 0
    for i in range(0, count):  # for loop where input_number = total numbers entered
        # Enter each number for the list of numbers
        input_number = float(input('Enter Number: \n'))
        sum_number = sum_number + input_number  # Calculates sum here
    average = sum_number / count  # Calculates average
    # Prints sum and average of the total numbers entered, round to 2 decimal places
    print("")
    print("Sum total numbers entered =", round(sum_number, 2))
    print("")
    print("Average of total numbers entered =", round(average, 2))


def main():

    # This function is used to start the main menu of the program and asks user if the user want to continue or end the program

    response = True
    while response:
        operation = getOperator()
        # If operation is chosen as avg (average), this will calculate average
        if operation == "avg":
            calculateAverage()
        # Any other chosen operators, will perform the basic arithmetic operation calculation
        else:
            performCalculation(operation)
        response = getResponse()


if __name__ == "__main__":
    main()
