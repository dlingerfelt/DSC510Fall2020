# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Riley Fencl
# 11/7/2020

import requests


def main():
    print("Howdy! Welcome to the Chuck Norris Joke Program!")
    user_action = {}
    while user_action != "no":
        user_action = input("Would you like to hear a Chuck Norris joke? Please use either yes or no.\n").lower()
        if user_action == "no":
            break
        elif user_action != "yes":
            print("Please enter either yes or no")
            continue
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        joke = response.json()
        print("Your Joke:")
        print("----------")
        print(joke["value"])
        print("----------")
    print("Okay, have a great day! Thank you!")


main()
