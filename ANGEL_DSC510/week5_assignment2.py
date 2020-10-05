# DSC 510
# Week 5
# Programming Assignment Week 5 : Calculator/Average Finder
# Author Daniel Angel
# 10/03/2020
import sys


def performCalculation(oper):
    a = float(input('Provide first number.'))
    b = float(input('Enter second number for arithmetic operation.'))
    if oper == '+':
        print(a, '+', b, '=')
        return a + b
    elif oper == '-':
        print(a, '-', b, '=')
        return a - b
    elif oper == 'x':
        print(a, 'x', b, '=')
        return a * b
    elif oper == '/' and b != 0:
        print(a, '/', b, '=')
        return a / b
    else:
        print('Invalid Entry')
        oper = input('Enter +, -, x, or / '
                     'to perform that operation')
        performCalculation(oper)


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


print("Welcome to Danny's calculator program!")
while True:
    choice = input('Type Calc for Calculator, Avg for Average Finder,'
                   ' or Q for Quit.')
    choice = choice.lower()
    if choice == 'calc':
        oper = input('"Calc" entered. Enter +, -, x, or / '
                     'to perform that operation')
        print(performCalculation(oper))
    elif choice == 'avg':
        calculateAverage()
    else:
        if choice == 'q':
            print('Q entered. Program will now exit.')
            sys.exit(1337)
        else:
            print('Invalid choice entered.')
            continue
