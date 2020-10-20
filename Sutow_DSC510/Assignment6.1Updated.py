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
'''The following program will create a formula that will have a user input temperatures,
the list will then stop when the target number has been reached.
The formula will then tell the maximum and minimum temperature in  fahrenheit.'''

#Introduction, sets up the user to input the amount of temperatures they want to list#
list_of_input = []
number_of_temperatures = int(input('How many temperatures would you like to input: '))
#Creates loop for the temperatures  from the user input#
for n in range(number_of_temperatures):
    temperatures = float(input('Enter one temperature at a time in fahrenheit: '))
    list_of_input.append(temperatures)
#Begins the process of calculating max and min for temperature. As well as gives a total number of tempeartures#
MaximumTemperature=max(list_of_input)
MinimumTemperature=min(list_of_input)
print('The highest temperature in the list is:','{:.0f}F'.format(MaximumTemperature))
print('The lowest temperature in the list is:','{:.0f}F'.format(MinimumTemperature))
print('Total number of temperatures:',number_of_temperatures)
