# DSC 510
# Week 10
# Programming Assignment Week10 - Prints Chuck Norris jokes for the user upon request.
# Author: David Brehm
# 11/8/2020

# Change Log:
# No changes.

import requests


def Pretty_print(response):
    """
    Prints the joke from the API.
    :param response: Response from GET request.
    :return: No return.
    """
    json = response.json()  # Converts JSON content to dictionary.
    joke = json['value']  # The joke is located in the key 'value'.
    print(joke)  # Prints the joke portion of the JSON data.


def main():
    """
    Main function. Performs GET request. The output is then printed with the function Pretty_print.
    :return: No return.
    """
    url = 'https://api.chucknorris.io/jokes/random'
    validtot = ['Y', 'y', 'N', 'n']
    validn = ['N', 'n']
    while True:  # Main loop.
        first = input('Welcome! Would you like to hear a random Chuck Norris joke? (Y/N)')  # Introduction prompt.
        if first not in validtot:  # Checks for valid input.
            print('Please enter Y or N.')
            continue
        elif first in validn:  # Break if user enters a no value.
            print('Goodbye!')
            break

        r1 = requests.get(url)  # GET request.
        status = str(r1.status_code)  # Status code of the request
        if status.startswith(('4','5')):  # Break if there was an error with the request.
            print('There was an error with the site. Try again later.')
            break
        Pretty_print(r1)  # Print the joke.

        while True:  # Loop after first successful joke.
            second = input('Would you like to hear another random Chuck Norris joke? (Y/N)')  # Secondary prompt.
            if second not in validtot:  # Checks for valid input.
                print('Please enter Y or N.')
                continue
            elif second in validn:  # Break if user enters a no value.
                print('Goodbye!')
                break
            else:  # Print the joke.
                r2 = requests.get(url)
                Pretty_print(r2)
                continue
        break


if __name__ == "__main__":
    main()
