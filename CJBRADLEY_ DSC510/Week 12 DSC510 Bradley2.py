#DSC 510                           # Change Log
#Week 12                          # No changes
#Author Carla J Bradley
#11/20/2020


import requests
import json
import datetime

class WeatherInfo:
    def __init__(self, city, state, zipcode, country):
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country

    def weather_request(self, by_this: str):
        do_response = True
        while do_response is True:
            baseurl = 'https://api.openweathermap.org/data/2.5/weather'

            if by_this == 'zipcode':
                parameters = {'zip': self.zipcode, 'units': 'imperial', 'appid': '7fe138653bd58ab16453ed2c91021bf0'}

                try:
                    try_baseurl = 'https://api.openweathermap.org/data/2.5/weather?zip=' + self.zipcode \
                                  + '&appid=7fe138653bd58ab16453ed2c91021bf0'
                    response = requests.get(baseurl, params=parameters)
                except:
                    print('submitted url:', baseurl, parameters)
                    print('error on response', response.status_code, response.url)
                    exit()


            elif by_this == 'city':
                parameters = {'q': {self.city, self.state, self.country}, 'units': 'imperial',\
                              'appid': '7fe138653bd58ab16453ed2c91021bf0'}

                try:
                    try_baseurl = 'https://api.openweathermap.org/data/2.5/weather?q=' + self.city \
                                  + ',' + self.state + ',' + self.country + '&units=imperial'+\
                                    '&appid=7fe138653bd58ab16453ed2c91021bf0'
                    response = requests.get(try_baseurl) # changed to only baseurl from try_baseurl
                except:
                    print('submitted url:', baseurl, parameters)
                    print('error on response', response.status_code, response.url)
                    exit()

            # next 4 commented lines are for testing and verification to display on-screen
            # print('our url:', baseurl, parameters)
            # print(response.url)
            do_response = False

        content = response.content
        info = json.loads(content)
        # print(type(info))
        # print(info)
        #json_info = json.dumps(info, indent=4)
        #print(json_info)
        return info

    def zip_code_request(self):
        pass

    def set_weather_history(self):
        global hist_id

        # increment id number and add the item to the weather history
        hist_id += 1
        weather_history[hist_id] = [self.city, self.state, self.zipcode, self.country]
        return weather_history


    # method to check for wind, clouds, rain, and snow
    def set_weather_conditions(self, info):
        cond_id = 0
        conditions_dict = {}
        for condition in info.keys():
            if condition == 'wind':
                cond_data_wind = info[condition]
                conditions_dict[condition] = [cond_data_wind]
                wind_direction(conditions_dict)
            elif condition == 'clouds':
                # percent cloudiness
                cond_data_clouds = info[condition]
                conditions_dict[condition] = [cond_data_clouds]
            elif condition == 'rain':
                cond_data_rain = info[condition]
                conditions_dict[condition] = {conditions_dict.update(cond_data_rain)}
            elif condition == 'snow':
                cond_data_snow = info[condition]
                conditions_dict[condition] = {conditions_dict.update(cond_data_snow)}

        return conditions_dict

    def pretty_print(self, info, conditions):
        current_datetime = datetime.datetime.now()
        current_date = current_datetime.strftime("%B %d, %Y")
        current_time = current_datetime.strftime("%I:%M:%S")
        current_day = current_datetime.strftime("%A")
        print("Thank you for visiting Sashi's Weather Forecast\n")
        print("Today is {}, {} and the time is {}.\n".format(current_day, current_date, current_time))
        print('The weather in {} shows {} with a temperature of {}\u00b0F.'.format(info['name'], \
                                                                            str(info['weather'][0]['main']).lower(), \
                                                                            info['main']['temp']))
        print('Feels like {}\u00b0F.\n'.format(info['main']['feels_like']))

        for cond in conditions.keys():
            if cond == 'wind':
                for wind_attr in conditions['wind']:
                    print('Wind speed: {:3}'.format(wind_attr['speed']))
                    print('Wind direction: {:3}\u00b0'.format(wind_attr['deg']))
                    print('Wind coming from the: {:3}'.format(wind_attr['cardinal_dir']))
            elif cond == 'clouds':
                for cloud_attr in conditions['clouds']:
                    print('Cloudiness: {:3}%'.format(cloud_attr['all']))
            elif cond == 'rain':
                for rain_attr in conditions['rain']:
                    print('Rain volume last hour: {:3}'.format(rain_attr['1h']))
                    print('Rain volume last three hours: {:3}'.format(rain_attr['3h']))
            elif cond == 'snow':
                for snow_attr in conditions['rain']:
                    print('Snow volume last hour: {:3}'.format(snow_attr['1h']))
                    print('Snow volume last three hours: {:3}'.format(snow_attr['3h']))
        print('\n')

        # messages to you
        if float(info['main']['feels_like']) < 45.0:
            print("Baby it's cold outside! Bundle up!")
        elif float(info['main']['feels_like']) > 90.0:
            print("Go to the beach!")
        elif float(info['main']['feels_like']) > 55.0:
            print("Nice and warm day ahead.")
        elif float(info['main']['feels_like']) > 46.0:
            print("It's a great day for a warm sweater and a hot cocoa.")

        print('\n')

def wind_direction(conditions):
    wind_deg = conditions['wind'][0]['deg']

    if wind_deg <= 0:
        wind_dir = 'Error: below the limit'
    elif wind_deg <= 11.25:
        wind_dir = 'N'
    elif wind_deg <= 33.75:
        wind_dir = 'NNE'
    elif wind_deg <= 56.25:
        wind_dir = 'NE'
    elif wind_deg <= 78.75:
        wind_dir = 'ENE'
    elif wind_deg <= 101.25:
        wind_dir = 'E'
    elif wind_deg <= 123.75:
        wind_dir = 'ESE'
    elif wind_deg <= 146.25:
        wind_dir = 'SE'
    elif wind_deg <= 168.75:
        wind_dir = 'SSE'
    elif wind_deg <= 191.25:
        wind_dir = 'S'
    elif wind_deg <= 213.75:
        wind_dir = 'SSW'
    elif wind_deg <= 236.25:
        wind_dir = 'SW'
    elif wind_deg <= 258.75:
        wind_dir = 'WSW'
    elif wind_deg <= 281.25:
        wind_dir = 'W'
    elif wind_deg <= 303.75:
        wind_dir = 'WNW'
    elif wind_deg <= 326.25:
        wind_dir = 'NW'
    elif wind_deg <= 348.75:
        wind_dir = 'NNW'
    elif wind_deg <= 360:
        wind_dir = 'N'
    else:
        wind_dir = 'Error: above the wind limit'
    conditions['wind'][0]['cardinal_dir'] = wind_dir

def menu_error_check(menu_choice, last_menu_option: int):
    last_menu_option = int(last_menu_option)
    # begin error checking routine for the menu
    try:
        int(menu_choice)
    except:
        print('Please select a numeric choice from the menu')
        menu_choice = 0

    menu_choice = int(menu_choice)

    if type(menu_choice) == str:
        print('You entered an invalid input')
        menu_choice = 0
    elif menu_choice > last_menu_option:
        print('Please select a numeric choice from the menu')
        menu_choice = 0
    elif type(menu_choice) == int and menu_choice <= last_menu_option and menu_choice != 0 and menu_choice > 0:
        pass
        #print('menu choice acceptable')
    elif menu_choice < 0:
        print('Please select a numeric choice from the menu')
        menu_choice = 0
    elif menu_choice == 0:
        print('Please select a numeric choice from the menu')
    else:
        print('then what kind of value is menu choice?!')
        exit()
    # end error checking routine for the menu
    return menu_choice


def main():

    menu = True
    menu_choice = 0
    prev_menu_choice = 0

    while menu is True:

        # display menu
        print("{:12} WELCOME TO SASHI'S WEATHER FORECAST\n\n".format(' '),
              '{:11} 1. Request Weather by Zip Code\n'.format(' '),
              '{:11} 2. Request Weather by City\n'.format(' '),
              '{:11} 3. Request Weather History\n'.format(' '),
              '{:11} 4. Display last weather city requested\n'.format(' '),
              '{:11} 5. Exit'.format(' '))

        # request selection from menu
        menu_choice = input('Please select a choice from the menu: ')


        # error check menu choice
        choice = menu_error_check(menu_choice, 5)
        menu_choice = int(choice)

        if menu_choice == 1:
            print('menu choice 1')
            # Weather by Zip Code

            zipcode = input('Enter the zip code: ')

            the_weather_dict = {}
            weathercall = WeatherInfo("", "", zipcode, "")
            the_weather_dict = weathercall.weather_request('zipcode')
            weathercall.set_weather_history()  # testing this with zip code

            # get weather conditions
            conditions = weathercall.set_weather_conditions(the_weather_dict)


            if int(the_weather_dict['cod']) == 200:
                weathercall.pretty_print(the_weather_dict, conditions)
            else:
                print('Zip Code does not exist in database.\n')

            prev_menu_choice = 1

            # end menu option 1

        if menu_choice == 2:
            print('menu choice 2')
            # Weather by City, State and Country

            city, state, country = '', '', ''
            while city == '':

                city = input('Please enter a city name: ')
                state = input('Please enter a state (2-letter code): ')
                country = input('Please enter a country (2-letter code): \n')
                if city == '':
                    print('Enter a value for City and State or City and Country, or All-three.\n')
                    break


                weathercall_bycity = WeatherInfo(city, state, "", country)
                the_weather_dict = {}
                the_weather_dict = weathercall_bycity.weather_request('city')
                weathercall_bycity.set_weather_history()

                # get weather conditions
                conditions = weathercall_bycity.set_weather_conditions(the_weather_dict)

                if int(the_weather_dict['cod']) == 200:
                    weathercall_bycity.pretty_print(the_weather_dict, conditions)
                else:
                    print('City does not exist in database.\n')
            prev_menu_choice = 2

        # end menu option 2

        if menu_choice == 3:
            print('Menu choice 3')
            # Weather History
            if len(weather_history) == 0:
                print('Please choose option 1 or 2 to request weather and add to history.')
                menu_choice = 0

            if len(weather_history) >=1:
                print('This is your weather history... ')
                # header
                print('{:2} {:15} {:5} {:10} {:10}'.format('ID', 'City', 'State', 'Zip Code', 'Country'))
                for attr, values in weather_history.items():
                    print('{:2} {:15} {:5} {:10} {:10}'.format(attr, values[0], values[1], values[2], values[3]))
            print('\n')
            prev_menu_choice = 2

        # End menu option 3

        if menu_choice == 4:
            print('Menu choice 4')
            # Last weather item object entered
            print('This is the last weather site requested:\n')
            if prev_menu_choice == 2:
                for attr, items in weathercall_bycity.__dict__.items():
                    print(attr, items)
            else:
                print('No weather for city selected. Please select menu option 1 or 2 to view the weather.\n')
        # end menu choice 4

        if menu_choice == 5:
            print('menu choice 5')
            # Exit
            menu = False


# start the program
weather_history = {}
hist_id = 0

main()
print("\n** Thank you for visiting Sahi's weather Forecast**\n")
print('\n** Program has Completed **\n')

