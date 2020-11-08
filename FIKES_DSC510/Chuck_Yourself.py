# DSC510 Week 10 Assignment - Chuck_Yourself.py
# Get Chuck Norris jokes using an API and JSON
# Author: Matthew Fikes
# 11/2/20

import requests


# function to call api and get the joke
def GetAJoke():
    try:
        cn = requests.get('https://api.chucknorris.io/jokes/random')
        cn_json = cn.json()
        print(cn_json['value']+'\n')
    except:
        print("The internet can't reach Chuck! He could reach you, but he won't")


# joke loop

def main():
    while True:

        user_input = input("Do you want to get Chucked? (Y/N): ")
# check input for y or yes, n or no
        if user_input.lower()=='y' or user_input.lower()=='yes':
            GetAJoke()
        elif user_input.lower()=='n' or user_input.lower()=='no':
            print("Too bad, you can't stop the Chuck")
            GetAJoke()
            break
# anything else entered
        else:
            print("Wrong answer!")
            continue
main()
