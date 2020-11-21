# DSC 510
# Week 12
# Programming Assignment Week 12
# Author Adonis Shareef
# 11/21/2020

# Change#: 3
# Change(s) Made: zip code adn city search function to request by zip code and city also pretty print function for displaying the data
# Date of Change: 11/21/2020
# Author: Adonis Shareef
# Change Approved by: Adonis Shareef
# Date Moved to Production: 11/21/2020
import requests


def prettyPrint(data):
    print("--"*12)
    print('Current Temperature : {} degrees fahrenheit'.format(data['main']['temp']))
    print('High Temperature : {} degrees fahrenheit'.format(data['main']['temp_max']))
    print('Low Temperature : {} degrees fahrenheit'.format(data['main']['temp_min']))
    print('Wind Speed : {} m/s'.format(data['wind']['speed']))
    print('Humidity : {} %'.format(data['main']['humidity']))
    print('Pressure : {} hPa'.format(data['main']['pressure']))
    print('Latitude : {}'.format(data['coord']['lat']))
    print('Longitude : {}'.format(data['coord']['lon']))
    print('Description : {}'.format(data['weather'][0]['description']))
    print("--"*12)

def zipCodeSearch(zipCode):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=99b3dfa06a12574f5e27bb96eece7963'.format(zipCode) #api call for zip code with api key
        r = requests.get(url)
        data = r.json()
        prettyPrint(data)
    except:
        print('Bad Request: ', r.status_code) #if bad request show status code

def citySearch(city):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&units=imperial&appid=99b3dfa06a12574f5e27bb96eece7963'.format(city) #api call for city 'q' with api key
        r = requests.get(url)
        data = r.json()
        prettyPrint(data)
    except:
        print('Bad Request: ', r.status_code) #if bad request show status code

def main():
    print('Welcome!')

    while True:
        zipOrCity = input('Would you like to look up by city,zip or exit?')
        if zipOrCity.lower() == 'zip':
            try:
                zipCode = input('Enter zip code')
                zipCodeSearch(zipCode)
            except Exception:
                print('Please enter a valid zip code')
        elif zipOrCity.lower() == 'city':
            try:
                c = input('Enter a City')
                citySearch(c)
            except Exception:
                print('Please enter a valid city')
        elif zipOrCity.lower() == 'exit':
            print('Goodbye!')
            break
        else:
            print('Enter zip code, city or exit')

if __name__ == "__main__":
    main()
