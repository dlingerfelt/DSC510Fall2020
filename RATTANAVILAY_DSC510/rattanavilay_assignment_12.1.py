# File: rattanavilay_assignment_12.1.py
# Assignment: 12.1
# Course: DSC 510
# Week 12
# Programming Assignment Week 12
# Author: Thip Rattanavilay
# DATE: 11/19/2020


"""
Create a header for your program just as you have in the past.
Create a Python Application which asks the user for their zip code or city.
Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
Display the weather forecast in a readable format to the user.
Use comments within the application where appropriate in order to document what the program is doing.
Use functions including a main function.
Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
Validate whether the user entered valid data. If valid data isn’t presented notify the user.
Use the Requests library in order to request data from the webservice.
Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
Use Python 3
Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful

"""


import sys
import requests


def main():

    print("\n")
    print("===============================")
    print("Welcome to the Weather Program!")  # Welcome header
    print("===============================")
    print("\n")
    # Display Welcome Message to customer
    Name = input("What is your name? ")
    print("")
    # Display Welcome Message to customer
    print("Welcome,", Name, "!")
    print("\n")
    print("===========================================================")
    print('You can check as many weather conditions as you would like.')
    print("===========================================================")
    print("\n")

    loop = True  # loop statement

    while loop:

        # input city or zip code here
        cityNameZip = input("\nEnter city name or Zip Code: ")

        # if statement to get correct city and country
        if isinstance(cityNameZip, int) == int:

            # API key for the weather 41e68752e5711ebcded771ca56e6561f
            apiKey = '41e68752e5711ebcded771ca56e6561f'
            url = 'http://api.openweathermap.org/data/2.5/weather?'  # URL for the API

            fullUrl = url + 'appid=' + apiKey + '&q=' + cityNameZip
        # else statement to get the correct city and country
        else:
            # API key for the weather 41e68752e5711ebcded771ca56e6561f
            apiKey = '41e68752e5711ebcded771ca56e6561f'
            url = 'http://api.openweathermap.org/data/2.5/weather?'  # URL for the API

            fullUrl = url + 'appid=' + apiKey + '&q=' + cityNameZip + ',us'

        # function to convert to usa measurements
        def convert(currentTemp, currentPressure):

            global fahrenheitTemp, inchPressure

            # float fahrenheit temp
            fahrenheitTemp = float((currentTemp - 273.15) * 9 / 5 + 32)
            inchPressure = float(currentPressure) / \
                33.863886666667  # float inch pressure
            # return fahrenheit temp and inch pressure
            return (fahrenheitTemp, inchPressure)

        # function to format and display weather to user
        def printWeather():
            print("\n")
            print("===============================")
            print('\n The weather for ' + str(currentCity) +
                  '\n Temperature is ' + str(fahrenheitTemp).split('.')[0] + '\xb0' +
                  '\n Pressure is ' + str('{:.2f}'.format(inchPressure)) + ' in' +
                  '\n Humidity is ' + str(currentHumidity) + '%' +
                  '\n Description is ' + str(weather))
            print("\n")
            print("===============================")

        # try statement to catch error if connection is not made
        try:
            # api connection
            response = requests.get(fullUrl)

        except:
            # error message for unsuccessful connection
            sys.exit("\nConnection unsuccessful. Try again later.")

        # get data from api
        x = response.json()

        # if statement to get specific data from API with error checking
        if x['cod'] != '404':
            try:
                currentCity = x['name']  # City Name

                y = x['main']

                currentTemp = y['temp']  # Temp
                currentPressure = y['pressure']  # Pressure
                currentHumidity = y['humidity']  # Humidity

                z = x['weather']
                weather = z[0]['description']  # display weather description
            except:
                # error / except
                sys.exit(print('\nError retrieving data. Please try again later.'))

            convert(currentTemp, currentPressure)

            printWeather()

            checkErrorsLoop = True

            # loop to check for user input error throughout the program
            while checkErrorsLoop:

                answer = input(
                    "\nWould you like to check another city's weather forecast? Please enter 'yes' or 'no'.\n")  # input answer
                answer = answer.lower()

                if 'yes' == answer:  # if statement for yes
                    checkErrorsLoop = False
                    loop = True

                elif 'no' == answer:  # else statement for no
                    checkErrorsLoop = False
                    print("\n")
                    print("========================================")
                    # Exit message
                    print("\nHave a lovely day and enjoy the weather!\n")
                    print("========================================")
                    loop = False

                else:
                    checkErrorsLoop = True
                    # error loop message
                    print('\n*Incorrect entry! Please enter "yes" or "no" only.*\n')

        else:
            print(
                '\nCity not found! Please enter correct format. 5 digit zip code or "city, state"')  # city not found message

            checkErrorsLoop = True

            while checkErrorsLoop:

                answer = input(
                    "\nWould you like to try again? Please enter 'yes' or 'no'.\n")  # try again message
                answer.lower()

                if 'no' == answer:  # if statement
                    checkErrorsLoop = False
                    loop = False
                    print("\n\nHave a good day!")
                    print("\n")
                elif 'yes' == answer:  # elif statement
                    checkErrorsLoop = False
                    loop = True
                else:
                    checkErrorsLoop = True  # else statement
                    print('\n*Incorrect Input! Please input "yes" or "no" only.*\n')


if __name__ == '__main__':
    main()
