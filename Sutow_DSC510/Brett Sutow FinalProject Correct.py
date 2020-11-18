#DSC 510#
#Final Project#
#Programming Assignment Week 12#
#Author: Brett Sutow#
#11/09/2020#
#If changes made please fill-out log#
#Change:#
#Changes Made:#
#Date of Change:#
#Author:#
#Change Approved By:#
#Date Moved to Production:#

#Introduction
name= input("Hello! First what is your name?")
print("Welcome {name}, to the Weather App!".format(name=name))
import requests
import json

# Below are weather zip function that is beting defined and connected to the website. This creates a realtionship to the site.
def weatherzip():
    zip= input("Please input the zip you would like weather on: ")
    url= 'http://api.openweathermap.org/data/2.5/weather?zip={},us&appid=da315025e20cf4a96b9a8b0f6c39556e&units=imperial&lang=en'.format(zip)
    requesting = requests.get(url)
    data= requesting.json()
    weather_data(data)

# Below asks the question whether or not more weather is wanted to be known.
    more= input("Would you like to search more weather? ")
    if more== 'Yes':
        main()
    if more== 'yes':
        main()
    if more== 'y':
        main()
    if more== 'YES':
        main()
    if more== 'Yes':
        main()
    if more== 'Y':
        main()
    if more== 'No':
        exit()
    if more== 'NO':
        exit()
    if more== 'no':
        exit()
    if more== 'N':
        exit()
    if more== 'n':
        exit()
    else:
        print('Error, follow the guidelines below.')

# Below are weather city function that is beting defined and connected to the website. This creates a realtionship to the site.

def weathercity():
    city= input("Please input the city you would like weather on: ")
    url= 'http://api.openweathermap.org/data/2.5/weather?lang=en&q={}&appid=da315025e20cf4a96b9a8b0f6c39556e&units=imperial'.format(city)
    requesting = requests.get(url)
    data= requesting.json()
    weather_data(data)


# Below asks the question whether or not more weather is wanted to be known.

    more= input("Would you like to search more weather? ")

    if more== 'Yes':
        main()
    if more== 'yes':
        main()
    if more== 'y':
        main()
    if more== 'YES':
        main()
    if more== 'Yes':
        main()
    if more== 'Y':
        main()
    if more== 'No':
        exit()
    if more== 'NO':
        exit()
    if more== 'no':
        exit()
    if more== 'N':
        exit()
    if more== 'n':
        exit()
    else:
        print('Error, follow the guidelines below.')

# Below creates a function that takes the various weather information from the site. It then displays the weather to the user.
def weather_data(data):
    cityname = data['name']
    temperature = data['main']['temp']
    high = data['main']['temp_max']
    low= data['main']['temp_min']
    feels = data['main']['feels_like']
    pressure= data['main']['pressure']
    windspeed = data['wind']['speed']
    description = data['weather'][0]['description']

    print('City: {}'.format(cityname))
    print('Current Temperature: {}F'.format(temperature))
    print('High for today: {}F'.format(high))
    print('Low for today: {}F'.format(low))
    print('Feels Like: {}F'.format(feels))
    print('Pressure: {}'.format(pressure))
    print('Wind Speed: {}MPH'.format(windspeed))
    print('Weather Description: {}'.format(description))

    # The below will throw an error when issues arise with the website. 
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    req= Request('http://api.openweathermap.org/data/2.5/weather?zip={},us&appid=da315025e20cf4a96b9a8b0f6c39556e&units=imperial&lang=en')
    try:
        response = urlopen(req)
    except HTTPError as error:
        print('HTTP error, try again')
    except URLError as error:
        print('Failed to reach website, try again')

    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    req= Request('http://api.openweathermap.org/data/2.5/weather?lang=en&q={}&appid=da315025e20cf4a96b9a8b0f6c39556e&units=imperial')
    try:
        response = urlopen(req)
    except HTTPError as error:
        print('HTTP error, try again')
    except URLError as error:
        print('Failed to reach website, try again')




# This helps determine whether or not the user is searching weather by zip code or city. It allows them to pick how they would like to search.
def main():
    while True:
        response = input('How would you like to search for weather: Zip Code or City:')
        if response == 'Zip Code':
            weatherzip()
        if response == 'ZipCode':
            weatherzip()
        if response == 'zip code':
            weatherzip()
        if response == 'zip':
            weatherzip()
        if response == 'Zip':
            weatherzip()
        if response == 'ZIP':
            weatherzip()
        if response == 'City':
            weathercity()
        if response == 'city':
            weathercity()
        if response == 'CITY':
            weathercity()
        else:
            print('Looks like an error occurred, try again and see if we can get this right! Acceptable answers are: Zip Code, ZipCode, zip code, zip, Zip, ZIP or City, city, and CITY.')
main()






