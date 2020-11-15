#DSC510
#Week 10
#Programming Assignment Week 10
#Author Ammy Theobald
#11/08/2020

#Change#:1
#Change(s) Made: Initial Program
#Date of Change: 11/08/2020
#Author: Ammy Theobald
#Change Approved by: N/A
#Date Moved to Production: 11/08/2020

import requests
import json

def joke():
    try:
        cj = requests.get('https://api.chucknorris.io/jokes/random')
        cj_json = cj.json()
        print('Thanks! Here is your joke:')
        print('')
        print(cj_json['value']+'\n')
    except:
        print('Chuck broke the internets. Try again later!')

# Determines if the user want another joke
    again = input('Would you like another joke? (y/n):')
    print('')
    if again.lower()=='y':
        joke()
    elif again.lower()=='n':
        print('OK. Goodbye!')
    else:
        print('Invalid response. Goodbye!')

def main():
        user_input = input('Hello! Welcome to the Chuck Norris Chuckle Generator! Would you like a joke? (y/n):')
        if user_input.lower()=='y':
            print('')
            joke()
        elif user_input.lower()=='n':
            print('OK, goodbye!')
        else:
            print('Invalid Response, goodbye!')

main()


