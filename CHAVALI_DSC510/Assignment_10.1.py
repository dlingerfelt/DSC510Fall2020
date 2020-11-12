# DSC510
# Week 10 Assignment - Assignment_10.1.py
# Getting Chuck Norris jokes
# Author Sowmya Chavali
# 11/08/20


import requests
import simplejson as json
import getpass

# function to call api and get the joke
def getJoke():
    try:
        chuck = requests.get('https://api.chucknorris.io/jokes/random')
        chuck_json = chuck.json()
        print(chuck_json['value'])
    except:
        print("Cannot reach Chuck Norris. Check your connection!")

def main():
    # gets the username to display it in the welcome message
    UserName = getpass.getuser()
    print('------------******************************------------')
    print("Welcome " + UserName)
    print("To get jokes input YES/yes/Y/n and NO/no/N/n to exit")
    print('------------******************************------------')
    while True:
        choice = input("Enter your choice:")
        if choice.upper() == 'YES' or choice.upper() == 'Y':
            getJoke()
        elif choice.upper() == 'NO' or choice.upper() == 'N':
            print("Come again! Bye!")
            break
        else:
            print("Enter a valid input")
            continue
main()