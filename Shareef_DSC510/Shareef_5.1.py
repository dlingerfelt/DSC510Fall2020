# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Adonis Shareef
# 10/04/2020

# Change#:1
# Change(s) Made: Created calculation functions
# Date of Change: 10/04/2020
# Author: Adonis Shareef
# Change Approved by: Adonis Shareef
# Date Moved to Production: 10/04/2020

def promptUserforInput():
    while True:
        print("Enter the first number")
        num1 = input()
        print("Enter the second number")
        num2 = input()
        try:
            float(num1)
            float(num2)
            break
        except ValueError:
            print("Please Enter a valid number ex:(1,2,3,3,5)")
    return num1, num2


def performCalculation(operator):
    num1, num2 = promptUserforInput()
    print(eval(num1 + operator + num2))


def calculateAverage():
    while True:
        try:
            numofnums = int(input("Enter how many numbers you wish to input"))
            if numofnums <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a positive number")
            continue
    print("Enter your numbers and press Enter after each number")
    numlist = []
    for i in range(numofnums):
        while True:
            try:
                numlist.append(float(input()))
                break
            except ValueError:
                print("Enter a valid number ex:(1,2,3,3.5)")
                continue
    average = sum(numlist) / numofnums
    print(average)


# Main
print("Welcome!")
operationlist = ["+", "-", "/", "*"]
while True:
    choice = input("Which calculation would you like to use: (operations, average, or quit)")
    if choice == "operations":
        while True:
            operation = input("Choose an operation (+, -, /, *)")
            if operation in operationlist:
                performCalculation(operation)
                break
            else:
                print("Enter a valid operation")
    elif choice == "average":
        calculateAverage()
    elif choice == "quit":
        print("Goodbye!")
        break
    else:
        continue
