#DSC 510#
#Week 10#
#Programming Assignment Week 10#
#Author: Brett Sutow#
#11/02/2020#
#If changes made please fill-out log#
#Change:#
#Changes Made:#
#Date of Change:#
#Author:#
#Change Approved By:#
#Date Moved to Production:#

#Below does an introduction to the person and gets them ready for the joke generator#
print('Hello are you ready to laugh? Welcome to the Chuck Norris Random Joke Generator!')
import requests
import json

#Below imports the JSON from the Chuck Norris joke generator and defines the function joke with that information#
#It is pulling the jokes from the site, and assigning value to the joke(). Further down the loop also goes into the function#
def joke():
    json_data= requests.get('https://api.chucknorris.io/jokes/random').json()
    cndatavalue = json_data['value']
    print(cndatavalue)

#Below asks if the person would like another joke. It covers all the possible answers, and creates an error if incorrect#
#It is defining the another joke variable to the input from the user, so that a correct result is being created#
#If site cannot be reached it tells proper steps to try again#
    anotherjoke = input('Would you like another joke? Y or N:')
    if anotherjoke == 'Y':
            main()
    if anotherjoke == 'Yes':
            main()
    if anotherjoke == 'yes':
            main()
    if anotherjoke == 'y':
            main()
    if anotherjoke == 'N':
            print('Have A Wonderful Day!')
            exit()
    if anotherjoke == 'n':
            print('Have A Wonderful Day!')
            exit()
    if anotherjoke == 'No':
            print('Have A Wonderful Day!')
            exit()
    if anotherjoke == 'no':
            print('Have A Wonderful Day!')
            exit()


    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    req= Request('https://api.chucknorris.io/jokes/random')
    try:
        response = urlopen(req)
    except HTTPError as error:
        print('HTTP error, try again')
    except URLError as error:
        print('Failed to reach website, try again')



#Below defines the main function where the majority of the loop is held.#
#It asks if you would like to hear a joke, and then returns a joke if a form of yes is inputted.#
#If not it will callback an error or end the function with any no input.#
def main():
    while True:
        response= input('Would you like to hear a Chuck Norris Joke? Y or N:')
        if response == 'Y':
            joke()
        if response == 'y':
            joke()
        if response == 'yes':
            joke()
        if response == 'Yes':
            joke()
        if response == 'N':
            print('Thank You! Have a Great Day!')
            exit()
        if response == 'No':
            print('Thank You! Have a Great Day!')
            exit()
        if response == 'no':
            print('Thank You! Have a Great Day!')
            exit()
        if response == 'n':
            print('Thank You! Have a Great Day!')
            exit()
        else:
            print('Looks like an error occurred. Acceptable answers are: Yes, Y, y, yes or No, N, n, no. '
                  'Make sure you have no space infront of the letter or word.')

main()



