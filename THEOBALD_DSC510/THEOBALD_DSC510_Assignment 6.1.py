#DSC510
#Week 6
#Programming Assignment Week 6
#Author Ammy Theobald
#10/11/2020

#Change#:1
#Change(s) Made: Initial Program
#Date of Change: 10/11/2020
#Author: Ammy Theobald
#Change Approved by: N/A
#Date Moved to Production: 10/11/2020

#Initial Greeting
name = input('What is your Name? \n')
print('Hello %s! Welcome to my Temperature Program!'%name)

#List Creation and Input


temperatures = [] #Empty List for Temperatures
stop_value = 999

print('')
print('Please enter your list of temperatures one at a time. Once finished, please enter 999.')
while True:
    try:
        user_input = float(input())
    except ValueError:
        print('Oops!!! You must enter a number. Try again.')
        continue
    if user_input == stop_value: #Finish program if stop_value is entered
        break
    temperatures.append(user_input) #Add user input to list if not the stop_value

minTemperature = min(temperatures) #Identify Min Temp
maxTemperature = max(temperatures) #Identify Min Temp
countTemp = len(temperatures) #Count number of Temps Entered

#Provide User with Output Results
print('')
print('The number of temperatures you entered was %d.' %countTemp)
print('')
print('The hottest (largest) temperature is %d. The coldest (smallest) temperature is %d.' %(maxTemperature, minTemperature))
print('')
print('Thank you for using my fun little Temperature Program. Have a nice day, %s!' %name)
