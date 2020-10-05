# DSC 510
# Week 6
# Programming Assignment Week6 - Prompt the user to input a list of temperatures. Determine the max, min, and count.
# Author: David Brehm
# 10/05/2020

# Change Log:
# No changes.

temperatures = []  # Empty list for input temperatures.
breakValue = 999  # Sentinel value.

print('Hello. Enter your list of temperatures in Fahrenheit one at a time. Enter 999 when you are finished.')  # Instruction message.

while True:  # Main loop. Gather user inputs in the temperatures list. Break if user inputs breakValue.
    try:
        inpTemp = float(input())  # User input. Only accept float values.
    except ValueError:
        print('Please enter a numerical value.')  # Display a message if the input is not a float.
        continue
    if inpTemp == breakValue:  # Break on breakValue.
        break
    temperatures.append(inpTemp)  # Add input to list if it wasn't the break value.

minTemp = min(temperatures)  # Determine smallest temperature.
maxTemp = max(temperatures)  # Determine largest temperature.
inpCount = len(temperatures)  # How many temperatures are in the list.

print("You entered %d temperatures." % inpCount)  # Results
print("Your smallest value was %0.1f Fahrenheit, your largest value was %0.1f Fahrenheit." % (minTemp, maxTemp))  # Results.
