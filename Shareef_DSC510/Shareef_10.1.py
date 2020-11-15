# DSC 510
# Week 10
# Programming Assignment Week 10
# Author Adonis Shareef
# 11/08/2020

# Change#: 2
# Change(s) Made: Prettyprint function to print just the vaule attribute from the JSON data, and import and used request get
# Date of Change: 11/08/2020
# Author: Adonis Shareef
# Change Approved by: Adonis Shareef
# Date Moved to Production: 11/08/2020
import requests

def prettyPrint(repsone):
    data = repsone.json()
    print(data['value']) #print the data associated with 'value'


def main():
    url = "https://api.chucknorris.io/jokes/random"
    validinput = ['y', 'Y', 'n', 'N']  # user can type these characters
    while True:
        confirm = input("Welcome! Would you like to hear a joke? (Y/N) ")
        if confirm not in validinput:
            print("Please enter valid input(Y/N)")
            continue
        elif confirm == 'n' or confirm == 'N':  # break if user wants to stop
            print("Take care!")
            break
        r = requests.get(url)  # get request from the API
        r.raise_for_status()  # checking for errors like 404
        if r:
            prettyPrint(r)
        else:
            print('Status error: ', r.status_code)  # print out status code


if __name__ == "__main__":
    main()
