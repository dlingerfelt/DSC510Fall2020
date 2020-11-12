# File: rattanavilay_assignment_10.1.py
# Assignment: 10.1
# Course: DSC 510
# Week 10
# Programming Assignment Week 10
# Author: Thip Rattanavilay
# DATE: 11/8/2020

"""

We’ve already looked at several examples of API integration from a Python perspective and this week we’re going to 
write a program that uses an open API to obtain data for the end user.

Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
The program will receive a JSON response which includes various pieces of data. You should parse the JSON data 
to obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
Your program should allow the user to request a Chuck Norris joke as many times as they would like. You should make 
sure that your program does error checking at this point. If you ask the user to enter “Y” and they enter y,
is that ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. 
Think about included string functions you might be able to call.
Your program must include a header as in previous weeks.
Your program must include a welcome message for the user.
Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t
represent “pretty.”

"""

import requests
import json

# Welcoming statement
print("Welcome to Random Chuck Norris Jokes!")
print("")
# Display Welcome Message to customer
Name = input("What is your name?")
print("")
# Display Welcome Message to customer
print("Welcome,", Name, "!")


def grab_jokes():
    try:
        response = requests.get('https://api.chucknorris.io/jokes/random')
        # Currently in Json -- need to parse and convert to python object
        jokes_4days = json.loads(response.text)
        # check status: 200 show = successful
        # Get joke from API and print out
        print("The joke is : {}\t".format(jokes_4days['value']), "\n")
    except Exception as e:
        print("{}".format(e.status_code))  # print(response.status_code)
        print('Please double check API URL')  # Error exception with API


def main():
    # print program function
    print("This program will randomly output a joke from Chuck Norris Jokes.")
    print("")
    # print out next steps
    print('Would you like to hear a jokes from Chuck Norris?')
    # Define Variables
    possible_no = ['No', 'no', 'N', 'n']  # Add possible No formats
    possible_yes = ['Yes', 'yes', 'Y', 'y']  # Add possible Yes formats
    user_input = ''
    program = True  # True function
    while True:
        user_input = input("Please enter with a 'Yes' or 'No' ")
        user_input = user_input.lower()
        if user_input in possible_no:  # if statement
            break
        elif user_input in possible_yes:  # elif statement
            grab_jokes()
            # Required a response entered
            print('Do you want to hear more jokes?')
        else:
            print('Response not valid. Please enter Yes or No')  # Input invalid


if __name__ == '__main__':
    main()
