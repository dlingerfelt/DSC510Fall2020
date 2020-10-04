# DSC 510
# Week 5
# Programming Assignment Week4
# Author: David Brehm
# 09/28/2020

# Change#:1
# Change(s) Made: Added change log
# Date of Change: 10/03/2020
# Author: David Brehm
# Change Approved by: David Brehm
# Date Moved to Production: 10/03/2020

def performCalculation(op):
    """
    Parameter: Operation to be performed.

    Prompts the user to input two numbers then evaluates based on the operation.
    The result is printed.
    """
    while True:
        print('Enter two numbers one at a time.')
        calc1 = input()
        calc2 = input()
        try:  # checks if inputs are floats.
            float(calc1)
            float(calc2)
            break
        except ValueError:
            print('Please enter numerical values.')
            continue

    result = eval(calc1 + op + calc2)  # Perform operation.
    print('Result = %s' % result)


def calculateAverage():
    """
    Prompts the user for how many numbers they would like to average, then obtains the numbers one at a time.
    The average is printed.
    """
    while True:  # Prompt the user for how many numbers they would like to average.
        try:
            numInputs = int(input('Enter how many numbers you would like to average: '))
            if numInputs <= 0:
                raise ValueError
            break
        except ValueError:
            print('Please enter a whole number.')
            continue
    print('Enter your %d numbers one at a time.' % numInputs)
    inpList = []
    for x in range(numInputs):  # Obtain the numbers to average and append them to a list.
        while True:
            try:
                inpNum = float(input())
                break
            except ValueError:
                print('Please enter a numerical value.')
                continue
        inpList.append(inpNum)
    average = sum(inpList) / numInputs  # Calculate the average.
    print('Result = %s' % average)


calcList = ['Operations', 'Average']  # List of valid calculation choices.
opList = ['+', '-', '*', '/']  # List of valid operation choices.

print('Welcome!')  # Introduction messages
print('We are going to be doing math. Type "Quit" as the calculation selection to quit.')

while True:  # Main loop.
    while True:
        func = input(
            'Which calculation would you like to perform (Operations, Average): ')  # Prompt calculation choice.
        if func == 'Quit':  # Ending the loop.
            break
        elif func in calcList:  # Proceed to running the calculation.
            break
        else:
            print('Enter a calculation from the list.')
    if func == 'Quit':  # Ending the loop.
        break
    elif func == 'Operations':  # Calculation choice is Operations.
        while True:
            inpOP = input('Which operation would you like to perform (+, -, *, /): ')
            if inpOP in opList:  # Perform calculation if operation is valid.
                performCalculation(inpOP)
                break
            else:
                print('Enter an operation from the list.')
    else:  # Calculation choice is Average.
        calculateAverage()
