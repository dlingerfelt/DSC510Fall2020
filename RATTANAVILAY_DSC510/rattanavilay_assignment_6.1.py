# File: rattanavilay_assignment_6.1.py
# Assignment: 6.1
# Course: DSC 510
# Week 6
# Programming Assignment Week 6
# Author: Thip Rattanavilay
# DATE: 10/10/2020

"""

Your program must have a header. 
Create an empty list called temperatures.
Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
Evaluate the temperature list to determine the largest and smallest temperature.
Print the largest temperature.
Print the smallest temperature.
Print a message tells the user how many temperatures are in the list.

"""


print("Welcome to Temperature World!")  # Welcoming statement
print("")

Name = input("What is your name?")  # Display Welcome Message to customer
print("")
# Display Welcome Message to customer
print("Welcome,", Name, "!")


temperatures = []


def getNumber():
    # Gets a number from an end user
    while True:
        try:
            # Input temperature integer
            num = float(input("Please enter a temperature number:"))
            break
        except ValueError:
            # Input error notice to enter an integer
            print("You need to enter a number")
    return num


def getTemperature():
    # Gets a number of temperature

    while True:
        try:
            length = int(
                # Input a series of temperatures
                input("Please input a series of temperatures, How many number of temperature do you want to enter: "))
            if isinstance(length, int) and length >= 1:
                break
            else:
                # Input is incorrect, need integer
                print("Your input is incorrect, Please enter a positive integer.")
        except ValueError:
            # Input an integer greater than 0
            print("Please enter a positive integer greater than 0.")

    for i in range(length):
        temperatures.append(getNumber())


def main():
    getTemperature()
    # print high temperature (Print the largest temperature)
    print("The highest temperature is {} degree.".format(max(temperatures)))
    # print low temperature (Print the smallest temperature)
    print("The lowest temperature is {} degree.".format(min(temperatures)))
    # Print a message tells the user how many temperatures are in the list
    print("There are {} temperatures in the list".format(len(temperatures)))


if __name__ == '__main__':
    main()
