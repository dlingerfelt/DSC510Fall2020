#DSC 510#
#Week 6#
#Programming Assignment Week 6#
#Author: Brett Sutow#
#10/04/2020#
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
list_of_input = []
number_of_temperatures = int(input('How many temperatures would you like to input: '))
#Creates loop for the numbers input#
for n in range(number_of_temperatures):
    temperatures = float(input('Enter one temperature at a time in fahrenheit: '))
    list_of_input.append(temperatures)
#Defines the function and begins the process of calculating sum and average#
MaximumTemperature=max(list_of_input)
MinimumTemperature=min(list_of_input)
print('The highest temperature in the list is:','{:.0f}F'.format(MaximumTemperature))
print('The lowest temperature in the list is:','{:.0f}F'.format(MinimumTemperature))
print('Total number of temperatures:',number_of_temperatures)
