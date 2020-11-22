#DSC510
#Week 12
#Programming Assignment Week 12 - Final Project
#Author Ammy Theobald
#11/21/2020

#Change#:1
#Change(s) Made: Initial Program
#Date of Change: 11/21/2020
#Author: Ammy Theobald
#Change Approved by: N/A
#Date Moved to Production: 11/21/2020

import requests

# webcall to openweather.com and get data
def get_weather(zip=None, city=None):
    weatherUrl='http://api.openweathermap.org/data/2.5/weather?units=imperial'
    apiid='2411b867ad8af3a119409b12dcc8b1f0'

    if zip is not None:
        weatherUrl+= '&zip='+str(zip)+',us'
    else:
        weatherUrl+= '&q='+str(city)+',us'

    weatherUrl += '&appid='+str(apiid)
    r = requests.get(weatherUrl)
    return r

# present data in readable format
def weather(resp):
    if resp.status_code == 200:
        data = resp.json()
        print(f"""{data['name']} Weather Forecast:
        Current Conditions: {data['weather'][0]['description']}
        Windspeed: {data['wind']['speed']} Miles/Hr
        Visibility: {data['visibility']}Miles
        Min. Temp: {data['main']['temp_min']} F
        Max. Temp: {data['main']['temp_max']} F
        """)
    else:
        print('Your request failed due to Reason Code:', resp.status_code)

# main program
def main():
    print('Welcome to My Weather Forecast!')
    print('')
    while True:
        search_type = int(input('Please choose a search type:\n1. Zip Code\n2. City Name\n3. Quit Program\n'))
        print('')
        if search_type == 1:
            try:
                zipcode = int(input('Please enter zip code:'))
                print('')
                # get data from openweather.com
                resp = get_weather(zipcode, None)
                weather(resp)
            except Exception as exception_code:
                print('Error:', exception_code)

        elif search_type == 2:
            try:
                cityname = input('Please enter city name:')
                # get data from openweather.com
                resp = get_weather(None, cityname)
                weather(resp)
            except Exception as exception_code:
                print('Error:', exception_code)
        elif search_type == 3:
            print('OK, Goodbye!')
            break

        else:
            print("Oops! I don't understand that! Please try again.")

if __name__=='__main__':
    main()

