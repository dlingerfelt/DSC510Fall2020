# DSC 510
# Week 5
# Programming Assignment Week 5
# Author Riley Fencl
# 10/14/2020

# This program first intakes a variable input from the user and calculates the average of the input.
# The program then intakes an operation from the user and performs that operation on two numbers provided by the user.

# Establishing the performCalculation function
def performCalculation(arg1):
    num1 = int(input("Please provide a number\n"))
    num2 = int(input("Please provide a second number\n"))
    if arg1 == "subtract":
        result = num1 - num2
        print("Your Result")
        print(result)
    elif arg1 == "add":
        result = num1 + num2
        print("Your Result")
        print(result)
    elif arg1 == "multiply":
        result = num1 * num2
        print("Your Result")
        print(result)
    elif arg1 == "divide":
        result = num1 / num2
        print("Your Result")
        print(result)


# Establishing the calculateAverage function
def calculateAverage():
    numcount = int(input("How many numbers do you wish to input?\n"))
    numlist = []
    while numcount > 0:
        numlist.append(int(input("Please Enter a Number\n")))
        numcount = numcount - 1
        numsum = 0
        for num in numlist:
            numsum += int(num)
        average = numsum / len(numlist)
    print("Your Average\n", average)


# Main Program
print("Hello User! Please follow the following prompts.")

print("First, we will calculate an average for however many numbers you wish!")
calculateAverage()

print("Next, please select an operation to perform!")
operator = str(input("You may choose either add, subtract, multiply, or divide.\n"))
performCalculation(operator)
print("\nThank You!")
