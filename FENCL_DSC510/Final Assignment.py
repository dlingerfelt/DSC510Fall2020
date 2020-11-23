# DSC 510
# Week 12
# Final Programming Assignment Week 12
# Author Riley Fencl
# 11/20/2020

import requests

# Defining the API and building the url objects to make the url input modular for either city and state or zip code.
API_Key = "8521c41e1adc73bcf4518cd13dad154a"
url_first_city = "http://api.openweathermap.org/data/2.5/weather?q="
url_first_zip = "http://api.openweathermap.org/data/2.5/weather?zip="
url_sep = ","
url_second = "&units=imperial&appid="
country = "US"


# The connection() function is where we establish the initial connection to the API and notify the user of the status.
def connection():
    url = "http://api.openweathermap.org/data/2.5/weather?q=spokane,wa,US&units=imperial&appid=8521c41e1adc73bcf4518cd13dad154a"
    try:
        response = requests.get(url)
        print("Connection Successful.")
    except requests.exceptions.ConnectionError as error1:
        print("Oops, it looks like we couldn't connect.", error1)
        print("Please wait a moment and try again.")
        exit()
    except requests.exceptions.RequestException as error2:
        print("Oops, it looks like something went wrong.", error2)


# main() is the primary function that links the other functions together and initiates the first user choice.
def main():
    connection()
    print("Hello! Welcome to my Weather Forecasting program!")
    user_action = {}
    while user_action != "no":
        user_action = input("Would you like a forecast?\n").lower()
        if user_action == "no":
            break
        elif user_action != "yes":
            print("Please enter either Yes or No.")
            continue
        elif user_action == "yes":
            user_input()
            break
    print("Thank you! Have a great day!")


# The city_state() function is the loop where the user enters information for city and state weather forecasts.
def city_state():
    output = {}
    while len(output) != 999:
        user_city = input("Please enter the name of your city.\n").lower()
        user_state = input("Please enter the state code for your city.\n")
        url = url_first_city + user_city + url_sep + user_state + url_sep + country + url_second + API_Key
        response = requests.get(url)
        output = response.json()
        if len(output) == 2:
            print("Oops! It looks like your city could not be found! Please try again!")
            continue
        elif len(output) > 2:
            main_obj = output["main"]
            weather_obj = output["weather"]
            weather_obj = weather_obj[0]
            print("Here is the forecast for your area!")
            print("-----------------------------------")
            print("{} {}{}".format("Average Temperature: ", main_obj["temp"], "\N{DEGREE SIGN}F"))
            print("{}    {}{}".format("High Temperature: ", main_obj["temp_max"], "\N{DEGREE SIGN}F"))
            print("{}     {}{}".format("Low Temperature: ", main_obj["temp_min"], "\N{DEGREE SIGN}F"))
            print("Weather:             ", weather_obj["main"])
            break


# The zipcode_function() is where the user enters information for zipcode weather forecasts.
def zipcode_function():
    output = {}
    while len(output) != 999:
        user_zip = input("Please enter your zip code.\n")
        url = url_first_zip + user_zip + url_sep + country + url_second + API_Key
        response = requests.get(url)
        output = response.json()
        if len(output) == 2:
            print("Oops! It looks like your city could not be found! Please try again!")
            continue
        elif len(output) > 2:
            main_obj = output["main"]
            weather_obj = output["weather"]
            weather_obj = weather_obj[0]
            print("Here is the forecast for your area!")
            print("-----------------------------------")
            print("{} {}{}".format("Average Temperature: ", main_obj["temp"], "\N{DEGREE SIGN}F"))
            print("{}    {}{}".format("High Temperature: ", main_obj["temp_max"], "\N{DEGREE SIGN}F"))
            print("{}     {}{}".format("Low Temperature: ", main_obj["temp_min"], "\N{DEGREE SIGN}F"))
            print("Weather:             ", weather_obj["main"])
            break


# user_input is where the user chooses city and state or zipcode and whether or not they choose to do a 2nd forecast.
def user_input():
    user_response = {}
    while user_response == "City and State" or "Zip Code":
        user_response = input("Would you like to select your area via City and State or Zip Code?\n").lower()
        if user_response == "city and state":
            city_state()
            user_exit = input("Would you like another forecast?\n").lower()
            if user_exit == "yes":
                continue
            elif user_exit == "no":
                break
        elif user_response == "zip code":
            zipcode_function()
            user_exit = input("Would you like another forecast?\n").lower()
            if user_exit == "yes":
                continue
            elif user_exit == "no":
                break
        elif user_response != "zip code" or "city and state":
            print("Oops! Please enter either zip code or city and state.")
            continue


main()

