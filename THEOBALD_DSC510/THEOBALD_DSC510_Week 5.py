#DSC 510
#Week 5
#Programming Assignment Week 5
#Author:Ammy Theobald
#10/04/2020

#Change Control Log:
#Change(s) Made: New Program
#Date of Change: 10/04/2020
#Author: Ammy Theobald
#Change Approved By: N/A
#Date Moved to Production: 10/04/2020

#This program will perform various calculations based on User Inputs.
#Calculations performed: Addition, Subtraction, Multiplication, Division and Average

#This section will get User's name and Welcome User to the program
from typing import List

print('Welcome to My Basic Calculator!')
name = input('What is your name?')
print('')
print('Hello', name, 'I am happy to help you!')

#This section will confirm if User wants to start/continue calculations or end the program
def get_start():
    start = input('Would you like to do another calculation? Enter y or n: ')
    for i in range(10):
        if start == 'n':
            print('Thank you for using My Basic Calculator!')
            return False
        elif start == 'y':
            return True
        else:
            start = input('You have made an invalid choice. Please enter y for Yes or n for No')
            continue

#This section will determine what calculation the user wishes to perform
def get_operation():
    operations = ['+', '-', '*', '/', 'Avg']
    while True:
        print('')
        print('Please chose the type of calculation you wish to perform:')
        print('For Addition, enter +')
        print('For Subtraction, enter -')
        print('For Multiplication, enter *')
        print('For Division, enter /')
        print('For Averages, enter Avg')
        print('')
        input_operation = input()
        if input_operation in operations:
            return input_operation
        else:
            continue

#This section will perform the requested +. -. * or / calculations
def getCalculation(operations):
    number1 = float(input('Please enter first number:\n'))
    number2 = float(input('Please enter second number \n'))
    while True:
        if operations == '+':
            result = number1 + number2
            print('')
            print('The Result is: ', round(result, 2))
        elif operations == '-':
            result = number1 - number2
            print('')
            print('The Result is: ', round(result, 2))
        elif operations == '*':
            result = number1 * number2
            print('')
            print('The Result is: ', round(result, 2))
        elif operations == '/':
            result = number1 / number2
            print('')
            print('The Result is: ', round(result, 2))
        return

#This section will perform the Average calculation
def getAverage():
    while True:
        try:
            count = int(input('How many numbers do you want to average? \n'))
            if count == 0:
                print('Please enter a number greater than zero!')
                continue
            break
        except ValueError:
            print('')
            print('Integers Only! Try again:')
    sum_number = 0
    for i in range(0, count):
        input_number = float(input('Enter number: \n'))
        sum_number = sum_number + input_number
    average = sum_number / count

    print('')
    print('')
    print('Total of numbers entered: ', round(sum_number,2))
    print('')
    print('Average of numbers is: ', round(average, 2))

#This function is used to to activate the main program
def main():
    start = True
    while start:
        operations = get_operation()
        if operations == 'Avg':
            getAverage()
        else:
            getCalculation(operations)
        start = get_start()

if __name__ == '__main__':
    main()


