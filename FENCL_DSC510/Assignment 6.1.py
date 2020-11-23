# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Riley Fencl
# 10/11/2020

# This program prompts the users for however many inputs they want until they input a stop value.
# The program then outputs how many numbers were input, the highest number and the lowest number.

# Establishing the temperatureslist function
def temperatureslist():
    temperatures = []
    addtemp = int(input("Please choose a temperature value to input, use -999 to stop the input\n"))
    temperatures.append(addtemp)
    while addtemp != -999:
        addtemp = int(input("Please choose a temperature value to input, use -999 to stop the input\n"))
        temperatures.append(addtemp)
    print("Temperatures Input: ", len(temperatures[:-1]))
    print("Highest Temperature: ", max(temperatures))
    print("Lowest Temperature: ", min(temperatures[:-1]))

temperatureslist()
