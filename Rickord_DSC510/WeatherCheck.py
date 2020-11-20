#DSC 510
#Week 12
#Programming Assignment Week 12
#Author Jake Rickord
#11/17/2020


import warnings
import string
warnings.filterwarnings("ignore")
import requests
from requests.exceptions import HTTPError

##city object to hold each data point, enter in default values just in case
class CityWeather:
    def __init__(self):
        self.townName='unknown'
        self.description = 'sunisshiningintheskythereaintacloudinsight'
        self.currentTemp= 'median'
        self.feelsLike = 'empty'
        self.low='absolute zero'
        self.high='surface of sun'
        self.humidity='scorched'
        self.windspeed='quick'
        self.winddirection='inwards'
    ##getters and setters
    def getTownName(self):
        return self.townName
    def getDescription(self):
        return self.description
    def getCurrentTemp(self):
        return self.currentTemp
    def getFeels(self):
        return self.feelsLike
    def getLow(self):
        return self.low
    def getHigh(self):
        return self.high
    def getHumidity(self):
        return self.humidity
    def getWindSpeed(self):
        return self.windspeed
    def getWindDirection(self):
        return self.winddirection

    def setTownName(self, stownName):
        self.townName=stownName
    def setDescription(self, sDescription):
        self.description=sDescription
    def setCurrentTemp(self, sCurrentTemp):
        sCurrentTemp=TConvert(float(sCurrentTemp))
        self.currentTemp=sCurrentTemp
    def setFeels(self, sFeels):
        sFeels=TConvert(float(sFeels))
        self.feelsLike=sFeels
    def setLow(self, sLow):
        sLow=TConvert(float(sLow))
        self.low=sLow
    def setHigh(self, sHigh):
        sHigh=TConvert(float(sHigh))
        self.high=sHigh
    def setHumidity(self, sHumidity):
        self.humidity=sHumidity
    ##convert from meters/sec to mph
    def setWindSpeed(self, sWindspeed):
        self.windspeed=sWindspeed*2.237
    ##set directionality based on JSON degree
    def setWindDirection(self, sWD):
        if(sWD<=33.75 or sWD>=326.25):self.winddirection='North'
        elif(sWD>33.75 and sWD<56.25): self.winddirection='Northeast'
        elif(sWD>=56.25 and sWD<=101.25): self.winddirection='East'
        elif(sWD>101.25 and sWD<146.25): self.winddirection='Southeast'
        elif(sWD>=146.25 and sWD<=191.25): self.winddirection='South'
        elif(sWD>191.25 and sWD<236.25): self.winddirection='Southwest'
        elif(sWD>=236.25 and sWD<=281.25): self.winddirection='West'
        elif(sWD>281.25 and sWD<326.25): self.winddirection='Northwest'

##convert from Kelvin to Fahrenheit
def TConvert(temptoconvert):
    return temptoconvert * 9/5 - 459.67

def zipInput():
    quitEntry = False
    ##for constructing API call
    api_key = '&appid=064a36747b3234a752f440a9d697991f'
    url = 'http://api.openweathermap.org/data/2.5/weather?zip='
    ##as long as they don't type quit, recursively request a zip code to perform parsing on
    while(quitEntry!=True):
        ui=input("Please enter the zip code for which you'd like to pull weather data on, otherwise type 'quit': ")
        if(quitCheck(ui)==False):
            if(zipcheck(ui)==False):
                try:
                    server_response = requests.get('{}{}{}{}'.format(url, ui, ',us',api_key))
                    server_response.raise_for_status()
                    print("Connection to server successful!")
                    JSON_data = server_response.json()
                    pretty_print(JSON_data, ui)
                except HTTPError as http_err:
                    print("Zip code {} is not found in the United States, please try again!".format(ui))
                except Exception as err:
                    print("Other error occurred: {}".format(err))
            else:
                print("You entered an invalid zip code, please try again!")
        else: quitEntry = True

def quitCheck(stringtocheck):
    ##remove punctuation
    stringtocheck=stringtocheck.translate(stringtocheck.maketrans('','',string.punctuation))
    ##print to lower case if applicable
    stringtocheck=stringtocheck.lower()
    ##remove whitespace if applicable
    stringtocheck=stringtocheck.rstrip()
    ##if it says quit, quit program, else continue
    if stringtocheck=='quit':return True
    else: return False

def zipcheck(zipcode):
    ##if zip code > 5 digits, return True since API does not support international
    if(len(zipcode)>5):
        return True
    else:
        ## check 5 digit zip code to see if it's actually a list of numbers
        if(zipcode.isdigit()==False):
            return True
        else: return False

def pretty_print(json_to_parse, zip):
    ##make a CityWeather object
    newCW=CityWeather()
    ##set new object's variables by parsing JSON data for each element
    newCW.setTownName(json_to_parse.get('name'))
    newCW.setDescription(json_to_parse.get('weather')[0].get('description'))
    newCW.setCurrentTemp(json_to_parse.get('main').get('temp'))
    newCW.setFeels(json_to_parse.get('main').get('feels_like'))
    newCW.setLow(json_to_parse.get('main').get('temp_min'))
    newCW.setHigh(json_to_parse.get('main').get('temp_max'))
    newCW.setHumidity(json_to_parse.get('main').get('humidity'))
    newCW.setWindSpeed(json_to_parse.get('wind').get('speed'))
    newCW.setWindDirection(json_to_parse.get('wind').get('deg'))
    print()
    ##print out nicely using getters from CityWeather object
    print('For the zip code entered, {}, which correlates to the city of {}:'.format(zip, newCW.getTownName()))
    print('The current temperature is {:0.1f}°F. The max temp in your area is {:0.1f}°F, and the min temp is {:0.1f}°F'.format(newCW.getCurrentTemp(), newCW.getHigh(), newCW.getLow()))
    print('Currently, the conditions are {}, with winds of {:0.2f} mph to the {}. Humidity lies at {}%'.format(newCW.getDescription(), newCW.getWindSpeed(), newCW.getWindDirection(), newCW.getHumidity()))
    print()
    ##delete object so it's not taking up memory on continued calls
    del newCW

def main():
    zipInput();

if __name__ == "__main__":
    main()
