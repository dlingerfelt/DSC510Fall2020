# DSC 510
# Week 5
# Programming Assignment Week 5 : Calculator/Average Finder
# Author Daniel Angel
# 10/03/2020
import sys
print("Welcome to Danny's calculator program!")
while True:
    choice = input('Type Calc for Calculator, Avg for Average Finder,'
                   ' or Q for Quit.')
    choice = choice.lower()
    if choice == 'calc':
        a = float(input('"Calc" entered. Provide first number.'))
        b = float(input('Enter second number for arithmetic operation.'))

        def performCalculation(a, b):
            operator = input('Enter +, -, x, or / '
                             'to perform that operation')
            if operator == '+':
                return a + b
            elif operator == '-':
                return a - b
            elif operator == 'x':
                return a * b
            elif operator == '/':
                return a / b
            else:
                print('Invalid Entry')
                return

        print('Answer is', performCalculation(a, b))
    elif choice == 'avg':

        def calculateAverage():
            total = 0
            count = 0
            numbers = []
            print('This is the Average Finder. Enter your numbers. '
                  'When finished hit enter or type a non-numerical entry')
            while True:
                try:
                    num = float(input())
                    total = total + num
                    count += 1
                    numbers.append(num)
                except ValueError:
                    try:
                        print('List of numbers to be averaged complete.\n'
                              'List of numbers:', numbers, '\n'
                              'Total of numbers =', total, '\n'
                              'Amount of numbers =', count,
                              '\nAverage is =', total / count)
                    except ZeroDivisionError:
                        print('The average of nothing is nothing. Try again.')
                        calculateAverage()
                    break
            return

        calculateAverage()
    else:
        print('Q entered or choice not recognized. Program will now exit.')
        sys.exit(1337)
