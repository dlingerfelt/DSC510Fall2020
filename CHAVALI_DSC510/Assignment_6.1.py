# DSC510
# Week 6 Assignment - Assignment_6.1.py
# Temperature lists
# Author Sowmya Chavali
# 10/10/20

import getpass
# Function to calculate the min max temperatures
def TempDetails(templist):
    print("Temperature list entered:")
    print(templist)
    print("The largest temperature entered : %.2f degrees." % max(templist))
    print("The smallest temperature entered : %.2f degrees." % min(templist))
    print("The number of temperatures entered : %d" % len(templist))
    print("Good bye!")


# gets the username to display it in the welcome message
UserName = getpass. getuser()
print("Welcome "+UserName)

flag = 999
TemperatureList = []

print("Enter list of temperatures and press 999 when you are done")
# looping through until the sentinal value is entered
while True:
    try:
        TemperatureVal = float(input())
    # validating the input values
    except ValueError:
        print('Please enter a valid input in numbers')
        continue
    if TemperatureVal == flag:
        break        # stop looping once the sentinel input is given
    else:
        TemperatureList.append(TemperatureVal)

if not TemperatureList:   # If no inputs are given
    print("The list is empty! Try again! Goodbye!")
else:
    TempDetails(TemperatureList)
