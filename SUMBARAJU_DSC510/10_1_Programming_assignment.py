# DSC 510
# Week 10
# Programming Assignment Week 10 - 10_1_Programming_assignment.py
# Author Aditya Sumbaraju
# 11/08/2020
# Change Control Log: 

# Change#:1
# Change(s) Made: NA
# Date of Change: 11/08/2020
# Author: Aditya Sumbaraju
# Change Approved by: Catie Williams
# Date Moved to Production: 11/08/2020

from datetime import date
import requests
from numpy.core.defchararray import lower
from requests import HTTPError


# Color definitions
class color:
    RED = '\033[91m'
    END = '\033[0m'
    BLUE = '\033[94m'


today = date.today()
Receipt_date = today.strftime("%m/%d/%y")


# function to calls api based on the user's input in main() function.
# Once the request is made to API a response is received in JSON format.
def api_call():
    try:
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
        response.raise_for_status()
        rsp_jsn = response.json()
        pretty_print(rsp_jsn)
    except HTTPError as api_error:
        print(color.RED + "It seems there is an error while API call  : {}".format(api_error) + color.END)
        exit()
    except Exception as err:
        print(color.RED + "please check url: {}".format(err) + color.END)
        exit()


# pretty_print () function prints the joke on the output screen.
def pretty_print(in_json):
    for key in in_json:
        if key == 'value':
            print('Joke: ' + color.BLUE + in_json[key] + color.END)


# Main() function calls api function api_call() based on users request.
# check for user input and convert the request to lower case and then call api to pull jokes
# instruct user to enter correct keyword to proceed

def main():
    print(color.BLUE + 'Execution Date: ' + color.END + Receipt_date)
    while True:

        req_user = lower(input("Want to stay out of brain burns - try Chuck therapy? (y/n): "))
        if req_user == 'y':
            api_call()
        elif req_user == 'n':
            print("I hope you are normal now.. A Last Joke for you enjoy it... ")
            api_call()
            break
        else:
            print(color.RED + "Please use y or n" + color.END)
            continue


if __name__ == '__main__':
    main()
