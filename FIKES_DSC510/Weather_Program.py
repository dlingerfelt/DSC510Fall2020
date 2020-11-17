# DSC510 Term Project - Weather_Program.py
# Pull weather from API and display results
# Author: Matthew Fikes
# 10/20/2020

import json
import requests
from datetime import datetime
import os
import gzip
import shutil
import sys
import re

# Main function
def main():
    userLocation = input("Please enter your location as a 5-digit zip code or City, State:")
    currentLocation = SearchLocation()
    Evaluate_Input(userLocation,currentLocation)
# Class to store data about search location with methods to update and get values
class SearchLocation():
    def __init__(self):
        self.zip = None
        self.lat = None
        self.long = None
        self.id = None
        self.city = None
        self.state = None
        self.country = None
    def UpdateZip(self,zip):
        self.zip = zip
    def UpdateCoords(self,lat,long):
        self.lat = lat
        self.long = long
    def UpdateID(self,id):
        self.id = id
    def UpdateCity(self,city):
        self.city = city
    def UpdateState(self,state):
        self.state = state
    def UpdateCountry(self,country):
        self.country = country
    def GetZip(self):
        return self.zip
    def GetCoords(self):
        return [self.lat,self.long]
    def GetCity(self):
        return self.city
    def GetState(self):
        return self.state
    def GetCountry(self):
        return self.country
    def GetID(self):
        return self.id
    def GetLocationString(self):
        loc_string = ("{city}, {state}, {country}".format(city=self.city,state=self.state,country=self.country))
        return loc_string
# Pull city list if not found and save to disk. This is for validating cities against user input
def Get_City_List():
    if not os.path.exists('city_list.json'):
        print("Downloading city list...")
        city_url = "http://bulk.openweathermap.org/sample/city.list.json.gz"
        city_zip = requests.get(city_url,stream=True)
        with open('city_list.json.gz','wb') as f:
            for chunk in city_zip.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            with gzip.open('city_list.json.gz','rb') as z_in:
                with open('city_list.json','wb') as z_out:
                    shutil.copyfileobj(z_in,z_out)
        print("Download complete!")
        os.remove('city_list.json.gz')
    else: pass
# Find city coordinates based on city/state/country
def Find_City(city,state,country):
    with open('city_list.json', encoding='utf-8') as city_JSON:
        city_in = json.load(city_JSON)
        for i in city_in:
            if city == i['name']:
                if state == i['state']:
                    if country == i['country']:

                        return [i['coord']]

            else: continue
    city_JSON.close()
# return location string based on city ID
def City_by_ID(id):
    with open('city_list.json', encoding='utf-8') as city_JSON:
        city_in = json.load(city_JSON)
        for i in city_in:
            if id == i['id']:
                loc_string = ("{0}, {1}, {2}".format(i['name'],i['state'],i['country']))
                return loc_string
    city_JSON.close()
    return
# return city id based on coordinates
def City_by_Coords(lat,long):
    with open('city_list.json', encoding='utf-8') as city_JSON:
        city_in = json.load(city_JSON)
        for i in city_in:
            if round(long,1) == round(i['coord']['lon'],1) and round(lat,1) == round(i['coord']['lat'],1):
                return i['id']
# check recent search info, allow user to reuse last search in attempt to mitigate API call limit
def Recent_Search(lat,long,location):
    current_time = datetime.utcnow()
    if os.path.exists("current_weather"):
        with open('current_weather','r') as cw:
            weather = json.load(cw)
            last_run_time = datetime.utcfromtimestamp(weather['current']['dt']) # find out date requested based on stored API data
            elapsed = current_time - last_run_time
            refresh = input("Last data retrieved {0} minutes ago. Are you sure you want to refresh? (Y/N): ".format(int(elapsed.seconds/60),))
            if refresh == "Y" or refresh == "y":
                print("\nRefreshing...")
                cw.close()
                Weather_by_Coords(lat,long,location)
            elif refresh == "N" or refresh == "n":
                print("Using existing data...")
                cw.close()
                Show_Forecast(Open_Forecast(location),location)
            else:
                print("Invalid entry - using existing data")
                cw.close()
                Show_Forecast(Open_Forecast(location),location)
                return

    else: Weather_by_Coords(lat,long,location)
# check user inputs - validate zips or city/state
def Evaluate_Input(userLocation,location):
    if len(userLocation) == 5 and userLocation.isnumeric():
        try:
            api_string = "https://www.zipcodeapi.com/rest/HhMI17FqhbvjpxazqCe9w8ecj4bQsepcA5O9EyXC10TVFbVPJj5Xt6O279AnUSmX/info.json/{zip}/degrees".format(
                zip=userLocation)
        except:
            print("Network Error - Unable to verify zipcode")
            return
        zipcode_get = requests.get(api_string)
        zip_json = zipcode_get.json()
        try:
            print(zip_json['error_msg'])
        except:
            lat = zip_json['lat']
            long = zip_json['lng']
            Recent_Search(lat, long, location)

    elif ',' in userLocation:
        try:
            input = re.compile(r'\w+,\w{2}(,\w{2})?')
        except:
            print("Invalid entry")
            return

        loc_string = re.split(r',',userLocation)
        city = loc_string[0]
        try:
            state = loc_string[1]
        except:
            state = ''
        try:
            country = loc_string[2]
        except:
            country = 'US'
        coords = Find_City(city,state,country)
        try:
            lat = round(coords[0]['lat'],2)
            long = round(coords[0]['lon'],2)
        except:
            print("Location not found")
            return
        Recent_Search(lat,long,location)
    elif userLocation == "exit":
        sys.exit()
    else:
        print("Invalid input")
# display forecast, set variables for display
def Show_Forecast(forecast,location):
# current weather variables
    weather_id = forecast['current']['weather'][0]['id']
    weather_desc = forecast['current']['weather'][0]['description'].capitalize()
    wind_speed = forecast['current']['wind_speed']
    wind_direction = forecast['current']['wind_deg']
    curr_temp = forecast['current']['temp']
    feels_like = forecast['current']['feels_like']
    cloud_cover = forecast['current']['clouds']
    icon_curr = Format_Icons(weather_id)
    try:
        rain = forecast['current']['rain']['1h']
    except:
        rain = 0
    try:
        snow = forecast['current']['snow']['1h']
    except:
        snow = 0
    loc_string = location.GetLocationString()
# 5 day forecast variables
    icon_day1 = Format_Icons(forecast['daily'][0]['weather'][0]['id'])
    icon_day2 = Format_Icons(forecast['daily'][1]['weather'][0]['id'])
    icon_day3 = Format_Icons(forecast['daily'][2]['weather'][0]['id'])
    icon_day4 = Format_Icons(forecast['daily'][3]['weather'][0]['id'])
    icon_day5 = Format_Icons(forecast['daily'][4]['weather'][0]['id'])
    temp_day1 = (" {0:.0f}°F/{1:.0f}°F".format(forecast['daily'][0]['temp']['max'],forecast['daily'][0]['temp']['min']))
    temp_day2 = (" {0:.0f}°F/{1:.0f}°F".format(forecast['daily'][1]['temp']['max'],forecast['daily'][1]['temp']['min']))
    temp_day3 = (" {0:.0f}°F/{1:.0f}°F".format(forecast['daily'][2]['temp']['max'],forecast['daily'][2]['temp']['min']))
    temp_day4 = (" {0:.0f}°F/{1:.0f}°F".format(forecast['daily'][3]['temp']['max'],forecast['daily'][3]['temp']['min']))
    temp_day5 = (" {0:.0f}°F/{1:.0f}°F".format(forecast['daily'][4]['temp']['max'],forecast['daily'][4]['temp']['min']))
    date1 = datetime.fromtimestamp(forecast['daily'][0]['dt'])
    date2 = datetime.fromtimestamp(forecast['daily'][1]['dt'])
    date3 = datetime.fromtimestamp(forecast['daily'][2]['dt'])
    date4 = datetime.fromtimestamp(forecast['daily'][3]['dt'])
    date5 = datetime.fromtimestamp(forecast['daily'][4]['dt'])
    wind1 = ("{0}mph, {1}".format(forecast['daily'][0]['wind_speed'],Wind_Direction(forecast['daily'][0]['wind_deg'])))
    wind2 = ("{0}mph, {1}".format(forecast['daily'][1]['wind_speed'],Wind_Direction(forecast['daily'][0]['wind_deg'])))
    wind3 = ("{0}mph, {1}".format(forecast['daily'][2]['wind_speed'],Wind_Direction(forecast['daily'][0]['wind_deg'])))
    wind4 = ("{0}mph, {1}".format(forecast['daily'][3]['wind_speed'],Wind_Direction(forecast['daily'][0]['wind_deg'])))
    wind5 = ("{0}mph, {1}".format(forecast['daily'][4]['wind_speed'],Wind_Direction(forecast['daily'][0]['wind_deg'])))
# layout for displaying forecast
    headline="\nWeather for {0} - last refreshed: {1}".format(loc_string,datetime.utcfromtimestamp(forecast['current']['dt']))
    print(headline)
    print("-"*86)
    print("|{0} |  Current Weather: {1}".format(icon_curr[0],weather_desc))
    print("|{0} |  Temperature: {1}°F, Feels Like: {2}°F".format(icon_curr[1],curr_temp,feels_like))
    print("|{0} |  Wind: {1}mph, {2}".format(icon_curr[2],wind_speed,Wind_Direction(wind_direction)))
    print("|{0} |  Cloud Cover: {1}%".format(icon_curr[3],(cloud_cover)))
    print("|{0} |  Precipitation last hour:    Rain: {1}mm    Snow: {2}mm".format(icon_curr[4],rain,snow))
    print("-"*86)
    print("|{0} |{1} |{2} |{3} |{4} |".format(icon_day1[0],icon_day2[0],icon_day3[0],icon_day4[0],icon_day5[0] ))
    print("|{0} |{1} |{2} |{3} |{4} |".format(icon_day1[1],icon_day2[1],icon_day3[1],icon_day4[1],icon_day5[1] ))
    print("|{0} |{1} |{2} |{3} |{4} |".format(icon_day1[2], icon_day2[2], icon_day3[2], icon_day4[2], icon_day5[2]))
    print("|{0} |{1} |{2} |{3} |{4} |".format(icon_day1[3], icon_day2[3], icon_day3[3], icon_day4[3], icon_day5[3]))
    print("|{0} |{1} |{2} |{3} |{4} |".format(icon_day1[4], icon_day2[4], icon_day3[4], icon_day4[4], icon_day5[4]))
    print("-" * 86)
    print("|{0:^16}|{1:^16}|{2:^16}|{3:^16}|{4:^16}|".format(date1.strftime('%b %d'),date2.strftime('%b %d'), date3.strftime('%b %d'), date4.strftime('%b %d'), date5.strftime('%b %d')))
    print("|{0:^16}|{1:^16}|{2:^16}|{3:^16}|{4:^16}|".format(temp_day1, temp_day2, temp_day3, temp_day4,temp_day5))
    print("|{0:^16}|{1:^16}|{2:^16}|{3:^16}|{4:^16}|".format(wind1,wind2,wind3,wind4,wind5))
    print("-" * 86)
# function to change wind degree to cardinal direction and arrow
def Wind_Direction(degrees):
    dirs = ['N','NE','E','SE','S','SW','W','NW']
    arrows = ['⬆','↗','➡','↘','⬇','↙','⬅','↖']
    cardinal_direction = round(degrees/(350. / len(dirs)))

    direction = dirs[cardinal_direction % len(dirs)]
    arrow = arrows[cardinal_direction % len(arrows)]
    wind_string = ("{0} {1}".format(arrow,direction))

    return wind_string
# function to create ASCII art for weather using ID code groups from OpenWeather API
def Format_Icons(curr_weather):
# Partly Cloudy
    if curr_weather in [801,802,803]:
        line1 = r"    \  /       "
        line2 = r'  _ /"".-.     '
        line3 = r"    \_(   ).   "
        line4 = r"    /(___(__)  "
        line5 = r'               '
        icon = [line1,line2,line3,line4,line5]
# Rainy
    elif (str(curr_weather)).startswith('5') or (str(curr_weather)).startswith('3'):
        line1 = r"    .---.      "
        line2 = r'   (     ).    '
        line3 = r"  (_____(__)   "
        line4 = r"   ‚‘‚‘‚‘‚‘    "
        line5 = r"   ‚’‚’‚’‚’    "
        icon = [line1,line2,line3,line4,line5]
# Cloudy
    elif curr_weather==804:
        line1 = r"               "
        line2 = r'      .--.     '
        line3 = r"   .-(    ).   "
        line4 = r"  (___.__)__)  "
        line5 = r"               "
        icon = [line1,line2,line3,line4,line5]
# Clear
    elif curr_weather == 800:
        line1 = r"     \   /     "
        line2 = r'      .-.      '
        line3 = r" --  (   ) --  "
        line4 = r"      `-’      "
        line5 = r"     /   \     "
        icon = [line1,line2,line3,line4,line5]
# Snow
    if (str(curr_weather)).startswith('6'):
        line1 = r"    .---.      "
        line2 = r'   (     ).    '
        line3 = r"  (_____(__)   "
        line4 = r"   ‚*‚‘*‘*‘    "
        line5 = r"   ‚’*’‚*‚’    "
        icon = [line1,line2,line3,line4,line5]
# Lightning
    elif (str(curr_weather)).startswith('2'):
        line1 = r"               "
        line2 = r'      .--.     '
        line3 = r"   .-(    ).   "
        line4 = r"  (___.__)__)  "
        line5 = r"    ⚡ ⚡ ⚡ ⚡     "
        icon = [line1,line2,line3,line4,line5]
# Atmospheric
    elif (str(curr_weather)).startswith('7'):
        line1 = r"               "
        line2 = r'   ~~*   ~~  ~~'
        line3 = r"~~* ~~  ~~* ~~ "
        line4 = r"   ~~ *  ~~  ~~"
        line5 = r"               "
        icon = [line1,line2,line3,line4,line5]
# pass correct iconset back as a list
    return icon
# function to open forecast data saved to save bandwidth
def Open_Forecast(Location):
    with open('current_weather','r') as cw:
        weather = json.load(cw)
        city_id = City_by_Coords(weather['lat'],weather['lon'])
        Location.UpdateCoords(weather['lat'],weather['lon'])
        Location.UpdateID(city_id)
        loc_string = re.split(',',City_by_ID(city_id))
        Location.UpdateCity(loc_string[0])
        Location.UpdateState(loc_string[1])
        Location.UpdateCountry(loc_string[2])
        return weather
# Function to write weather JSON to an external file for limiting needed API calls
def Weather_Storage(weather):
    with open('current_weather','w') as wf:
        wf.write(json.dumps(weather))
# Function to write api string based on latitude + longitude
def Weather_by_Coords(lat,long,location):
    lat = lat
    long = long

    city_id = City_by_Coords(lat,long)
    api_string = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lng}&exclude=minutely,hourly,alerts&appid=5ff26c643836bbab24edf9ce7e27c232&units=imperial".format(lat=lat,lng=long)
    try:
        weather_data = requests.get(api_string)
        weather_json = weather_data.json()
    except:
        print("Unable to contact weather API. Check internet connection")
        return
    Weather_Storage(weather_json)
    Show_Forecast(Open_Forecast(location),location)
# welcome splash screen
def Welcome():
    print("***************************************************************************")
    print(r"  _____       _   _             __          __        _   _               ")
    print(r" |  __ \     | | | |            \ \        / /       | | | |              ")
    print(r" | |__) |   _| |_| |__   ___  _ _\ \  /\  / /__  __ _| |_| |__   ___ _ __ ")
    print(r" |  ___/ | | | __| '_ \ / _ \| '_ \ \/  \/ / _ \/ _` | __| '_ \ / _ \ '__|")
    print(r" | |   | |_| | |_| | | | (_) | | | \  /\  /  __/ (_| | |_| | | |  __/ |   ")
    print(r" |_|    \__, |\__|_| |_|\___/|_| |_|\/  \/ \___|\__,_|\__|_| |_|\___|_|   ")
    print(r"         __/ |                                                            ")
    print(r"        |___/                                                             ")
    print("***************************************************************************")
    print("Enter location as 5-digit zipcode or City,State,Country")
    print("If location is in the US, Country can be left blank")
    print("if location is outside the US, State can be left blank")
    print("ex. '13502'; 'Syracuse,NY'; 'Paris,,FR'")
    print("To quit, type 'exit'\n")

Get_City_List()
Welcome()
while True:

    main()
