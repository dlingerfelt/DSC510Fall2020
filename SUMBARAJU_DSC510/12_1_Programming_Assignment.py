# DSC 510

# Week 12

# Programming Assignment Week 12 - 12_1_Programming_Assignment.py

# Author Aditya Sumbaraju

# 11/19/2020

# Change Control Log:

# Change#:1
# Change(s) Made: Added iteration check to check with user to perform operation or exit from the program
# Date of Change: 11/19/2020
# Author: Aditya Sumbaraju
# Change Approved by: Catie Williams
# Date Moved to Production: 11/19/2020

import requests
from requests import HTTPError
import datetime


# color class
class color:
    RED = '\033[91m'
    END = '\033[0m'
    BLUE = '\033[94m'


# convert API time parameters to meaningful format
def formatTime(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%m/%d/%Y %I:%M %p')
    return converted_time


# weather_data() queries API by passing city or zip. And the respective json result will be returned to the main() function.
# Checks for the connection status and notifies user if it is successful
def weather_data(query):
    url = 'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=a991c8906f68e394a9057ad5067afa00&units=metric'
    try:
        api_resp = requests.get(url)
        rsp_jsn = api_resp.json()
        if (api_resp.ok):
            print('API connection is successful')
        else:
            api_resp.raise_for_status()
        # print(rsp_jsn)
        return rsp_jsn
    except HTTPError as api_error:
        print(color.RED + "It seems there is an error while API call  : {}".format(api_error) + color.END)

    except Exception as err:
        print(color.RED + "please check url: {}".format(err) + color.END)


# print_weather() prints weather details on output screen.
def print_weather(result):
    print('Weather Forecast at {},{} as of {}'.format(result['name'], result['sys']['country'], formatTime(result['dt'])))
    print("----------------------------------------------------")
    print("Current temperature: {}°C with {}".format(result['main']['temp'], result['weather'][0]['description']))
    print("Maximum temperature: {}°C ".format(result['main']['temp_max']))
    print("Minimum temperature: {}°C ".format(result['main']['temp_min']))
    print("Wind speed         : {} m/s".format(result['wind']['speed']))
    print("Weather condition  : {}".format(result['weather'][0]['main']))
    print('Sunrise at         : {}'.format(formatTime((result['sys']['sunrise']))))
    print('Sunset at          : {}'.format(formatTime((result['sys']['sunset']))))
    print("----------------------------------------------------")


'''
main() requests user to input zip or city
main() calls function weather_data() to pull the request from API
main() calls function print_weather() to print the results in a readable format.
'''


def main():
    while True:
        userInput = input('Please enter below keywords to search weather'
                          + color.BLUE + '\n' + '1. Enter "z" for zip'
                                                '\n' + '2. Enter "c" for city'
                                                       '\n' + '3. Enter "e" to exit' + color.END + '\n').lower()

        if userInput == 'z':
            zip = input(color.BLUE + "Please input the zip code: " + color.END)
            try:
                query = 'zip=' + zip
                w_data = weather_data(query)
                print_weather(w_data)
                # print(w_data)
            except Exception as err:
                print(color.RED + "please check url: {}".format(err) + color.END)
                exit()
            except:
                print(color.RED + 'zip name not found...' + color.END)
        elif userInput == 'c':
            city = input(color.BLUE + "Please input the City Name: " + color.END)
            try:
                query = 'q=' + city
                w_data = weather_data(query)
                print_weather(w_data)
                # print(w_data)
            except Exception as err:
                print(color.RED + "please check url: {}".format(err) + color.END)
                exit()
            except:
                print(color.RED + 'city name not found...' + color.END)

        elif userInput == 'e':
            print("----------------------------------------------------")
            print('          THANK YOU - VISIT AGAIN                   ')
            print("----------------------------------------------------")
            exit()
        else:
            print(color.RED + 'please use key words "z" for zip code or "c" for city - Try Again' + color.END)
            exit()


if __name__ == '__main__':
    main()
