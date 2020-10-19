# DSC 510
# Week 6
# Programming Assignment Week 6
# Author Adonis Shareef
# 10/11/2020

# Change#:2
# Change(s) Made: User input for list of temperatures, Returned the largest and smallest temperatures
# Date of Change: 10/11/2020
# Author: Adonis Shareef
# Change Approved by: Adonis Shareef
# Date Moved to Production: 10/11/2020

# empty list
temperatures = []
while True:
    try:
# user input which gets how many temps you want to input, must be a whole number
        numoftemps = int(input("Enter how many temperatures you wish to input "))
        break
    except ValueError:
# the user must enter a number
        print("Enter a number")
        continue
print("Enter your numbers and press Enter after each number ")
for i in range(numoftemps):
    while True:
        try:
# adds the user input to the list
            temperatures.append(float(input()))
            break
        except ValueError:
            print("Enter a valid temperature ex:(90,-30,101) ")
            continue
# using max function on the list to return the largest element
print("The Largest temperature: ", max(temperatures))
# using the min function on the list to return the smallest element
print("The Smallest temperature: ", min(temperatures))
# returning the length of the list
print("Number of temperatures entered: ", len(temperatures))
