#DSC 510
#Week 10
#Programming Assignment Week 10
#Author Kim Terek
#11/09/2020

#Change#:0
#Change(s) Made: First time code (no changes yet)
#Date of Change: 11/09/2020
#Author: Kim Terek
#Change Approved by: xxxx
#Date Moved to Production: xx/xx/xxxx

import requests
import pprint
import json

r = requests.get('https://api.chucknorris.io/jokes/random')
#https://api.chucknorris.io/jokes/random is endpoint

pkg = r.json()
#print(pkg)
joke = input('Hello. Do you want to see another Chuck Norris joke?: (type y or n):')


for value in pkg:
    #print(joke)
    if value =='value':
        print(pkg[value])
    #yelif value +=  :
        newjoke = input('Do you want to see another Chuck Norris joke?: (type y or n):')
        if newjoke == 'y':
            print(pkg[value])
        if newjoke == 'n':
            print("Thank you and Have a good day.")


