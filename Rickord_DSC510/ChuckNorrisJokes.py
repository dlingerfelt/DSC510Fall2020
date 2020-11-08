#DSC 510
#Week 10
#Programming Assignment Week 10
#Author Jake Rickord
#11/05/2020

##dependencies
import string
import requests
from requests.exceptions import HTTPError

def pull_joke():
    try:
        ##requests input from API and returns it
        server_response=requests.get('https://api.chucknorris.io/jokes/random')
        ##immediately raise exception if request is unsuccessful
        server_response.raise_for_status()
        ##grab JSON_data into dictionary
        JSON_data = server_response.json()
        #print out joke element of pulled JSON data
        pretty_print(JSON_data)
    ##cover both types of errors with display message
    except HTTPError as http_err:
        print("Http error occurred: {}".format(http_err))
    except Exception as err:
        print("Other error occurred: {}".format(err))

def pretty_print(json_to_parse):
    ##find value piece which is actual joke
    print()
    for key in json_to_parse:
        if key=='value':
            print(json_to_parse[key])

def word_processor(word_to_process):
    ##remove punctuation
    word_to_process = word_to_process.translate(word_to_process.maketrans('', '', string.punctuation))
    ##brings to lower case
    word_to_process = word_to_process.lower()
    ##removes trailing characters
    word_to_process = word_to_process.rstrip()

    return word_to_process

def input_check(message, check_against):
    #get user input
    user_input = input(message)
    #get in comparable form
    user_input = word_processor(user_input)
    #check it
    if(user_input == check_against):
        return True
    else: return False

def main():
    ##establish sentinel value for recurring status check
    sentinel_value = False

    ##welcome message
    print("Welcome to the Chuck Norris Joke Generator, we hope you're prepared to laugh!")



    ##recursively check if user would like another joke
    if(input_check("Would you like to hear a joke? If so, type 'Ready', otherwise, feel free to type anything else: ", "ready")):
        pull_joke()
        while (sentinel_value != True):
            if(input_check("Would you like to hear another? If so, type 'LOL', else type anything else: ", "lol")):
                pull_joke()
            else: sentinel_value=True


if __name__ == "__main__":
    main()
