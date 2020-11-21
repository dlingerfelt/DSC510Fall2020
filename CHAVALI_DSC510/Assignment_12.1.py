# DSC510
# Final Project - Assignment_12.1.py
# Weather App
# Author Sowmya Chavali
# 11/21/20
import requests


# requesting the weather information by zip code.
def zip_search(zip_code):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&appid=3cfb3ef209130bbc71e87da6c0f41baf'.format(
        zip_code)
        res = requests.get(url)
        data = res.json()
        pretty_print(data)
    except:
        print("Check your internet connection!")

# requesting the weather information by city name.
def city_search(city):
    try:
        url ='https://api.openweathermap.org/data/2.5/weather?q={},us&appid=3cfb3ef209130bbc71e87da6c0f41baf&units=imperial'.format(
        city)
        res = requests.get(url)
        data = res.json()
        pretty_print(data)
    except:
        print("Check your internet connection!")

# This function prints the requested weather information.
def pretty_print(data):
    temp = data['main']['temp']
    high_temp = data['main']['temp_max']
    low_temp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    humid = data['main']['humidity']
    press = data['main']['pressure']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']
    print("****************************************************")
    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(high_temp))
    print('Low Temperature : {} degree fahrenheit'.format(low_temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Humidity : {} %'.format(humid))
    print('Pressure : {} hPa'.format(press))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))
    print("****************************************************")


# This function asks user if they want to continue search
def search_again():
    print("Do you want to do another search ?")
    value = input("Type No to exit and any other key to continue search")
    if value.lower() == 'no':
        print("Thank you for using the weather app. Good Bye!")
        exit()


def main():
    print("Welcome to weather app!")
    while True:
        # Asking the user on search by city or zipcode
        choice = input("Search city or zip. Enter your choice:")
        if choice == 'city':
            while True:
                city = input('Please Enter Your City Name: ')
                city_search(city)
                search_again()
                break

        elif choice == 'zip':
            while True:
                try:
                    zip_code = int(input('Please Enter Your Zip code: '))
                    zip_search(zip_code)
                    search_again()
                    break
                except Exception:
                    print("hmm, You did not enter a valid zip code numbers. Try again")

        else:
            print("well, that is not one of the options. Try again.")
            pass

main()
