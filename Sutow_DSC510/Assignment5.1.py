#DSC 510#
#Week 5#
#Programming Assignment Week 5#
#Author: Brett Sutow#
#9/28/2020#
#If changes made please fill-out log#
#Change:#
#Changes Made:#
#Date of Change:#
#Author:#
#Change Approved By:#
#Date Moved to Production:#
'''The following program will create a mathemtical equation where the user can input
the numbers and the operation that is needed. This eqution will return the correct total'''
#Introduction#
print('Hello!')
name = input('What is your name?')
print("Welcome {name}! Let's begin the mathematical equation!".format(name = name))
#Defines first number#
num1 = float(input('Enter the first number: '))
#Defines second number#
num2 = float(input('Enter the second number: '))
#Defines which operator the user chooses
operator = input('Choose a mathematical operator: ')
#Below performs and defines calculation#
def performCalculation(opeartor):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
performCalculation(operator)

#The following function will allow the user to input a list, and then get the total sum and average#
#User inputs how many numbers they would like to list#
list_of_input = []
how_many_numbers = int(input('How many numbers would you like to input: '))
#Creates loop for the numbers input#
for n in range(how_many_numbers):
    numbers = int(input('Enter the list'))
    list_of_input.append(numbers)
#Defines the function and begins the process of calculating sum and average#
def calculateAverage():
   total=sum(list_of_input)
   average=(sum(list_of_input))/(len(list_of_input))
   return(total,average)
calculateAverage()
print('Total sum and average an of list:', calculateAverage())

