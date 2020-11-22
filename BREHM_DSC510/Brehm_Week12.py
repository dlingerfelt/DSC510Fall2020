# DSC 510
# Week 12
# Programming Assignment Week12 - Weather Program
# Author: David Brehm
# 11/16/2020

# Change Log:
# No changes.

import requests

api = '18e9ca33c285444f45cda0859f960763'  # API access


def pretty_print(req, units):
    """
    Prints the data from the API get in a nicer format.
    :param req: The API get
    :param units: C or F for Celsius or Fahrenheit
    :return: No return.
    """
    j = req.json()
    if units == 'C':
        print('Name: {}'.format(j['name']))  # Name of city.
        print('Lat: {}, Lon: {}'.format(j['coord']['lat'], j['coord']['lon']))  # Coordinates.
        print('Current temperature: {} C'.format(j['main']['temp']))  # Current temperature.
        print('Feels like: {} C'.format(j['main']['feels_like']))  # Feels like temperature.
        print('High temperature: {} C'.format(j['main']['temp_max']))  # High temperature.
        print('Low temperature: {} C'.format(j['main']['temp_min']))  # Low temperature.
        print('Humidity: {} %'.format(j['main']['humidity']))  # Humidity percentage.
        print('Weather description: {}'.format(j['weather'][0]['description']))  # Weather description.
        print('Wind: {} kmph, {} degrees'.format(j['wind']['speed'], j['wind']['deg']))  # Wind data.
        print('')
    else:
        print('Name: {}'.format(j['name']))  # Name of city.
        print('Lat: {}, Lon: {}'.format(j['coord']['lat'], j['coord']['lon']))  # Coordinates.
        print('Current temperature: {} F'.format(j['main']['temp']))  # Current temperature.
        print('Feels like: {} F'.format(j['main']['feels_like']))  # Feels like temperature.
        print('High temperature: {} F'.format(j['main']['temp_max']))  # High temperature.
        print('Low temperature: {} F'.format(j['main']['temp_min']))  # Low temperature.
        print('Humidity: {} %'.format(j['main']['humidity']))  # Humidity percentage.
        print('Weather description: {}'.format(j['weather'][0]['description']))  # Weather description.
        print('Wind: {} mph, {} degrees'.format(j['wind']['speed'], j['wind']['deg']))  # Wind data.
        print('')


def main():
    """
    Main function. Prompts the user for inputs then prints the item count and total cost when complete.
    :return: No return.
    """
    print("Welcome to this weather data service!")
    print("Enter C or F for Celsius or Fahrenheit.")
    while True:  # Loop to get units.
        u = input()
        if u not in ['C', 'F']:
            print('Please enter C or F.')
            continue
        if u == 'C':  # Celsius
            unit = 'metric'
        else:  # Fahrenheit
            unit = 'imperial'
        break

    print('')
    print("Enter a location by zip code or city to obtain its weather forecast. Enter 'Quit' when you are finished.")
    while True:  # Main loop to get location.
        s = input('Location: ')
        if s == 'Quit':
            break
        s1 = [i.strip() for i in s.split(',')]
        if s1[0][0].isdigit():  # Loop if input is zip code.
            if len(s1) > 2:  # Check for valid format.
                print('Zip code entry method must be either [zip code] or [zip code, country code].\n')
                continue
            elif len(s1) == 1:  # Zip code without country is US.
                r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units={}'.format(s1[0],'us',api,unit))
            else:  # Zip code with specified country.
                r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units={}'.format(s1[0],s1[1],api,unit))
            if r.status_code == 404:  # Error on input.
                print('Input results in 404 error.\n')
                continue
        else:  # Loop if input is city.
            if len(s1) > 3:  # Check for valid format.
                print('City entry method must be either [city], [city, state/country], or [city, state, country].\n')
                continue
            elif len(s1) == 1:  # Input is just the city.
                r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}'.format(s1[0],api,unit))
            elif len(s1) == 2:  # Input is city and state/country.
                r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}&units={}'.format(s1[0],s1[1],api,unit))
            else:  # Input is city, state, and country.
                r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={},{},{}&appid={}&units={}'.format(s1[0],s1[1],s1[2],api,unit))
            if r.status_code == 404:  # Error on input.
                print('Input results in 404 error.\n')
                continue
        pretty_print(r, u)  # Call pretty_print for our GET and units.



if __name__ == "__main__":
    main()
