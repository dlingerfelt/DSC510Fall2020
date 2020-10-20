#DSC 510
#Week 6
#Programming Assignment Week 6_1
#Author Kim Terek
#10/11/2020

#Change#:0
#Change(s) Made: First time code (no changes yet)
#Date of Change: 10/11/2020
#Author: Kim Terek
#Change Approved by: xxxx
#Date Moved to Production: xx/xx/xxxx

import math

print()
print('TEMPERATURE LISTINGS')
print('All entries assumed as Fahenheit degrees.')
print("This program will ask you to enter temperatures, and when done,")
print("it will read out your highest and lowest temperatures documented.")
print()
print('You will be allowed to enter as many temperature values as desired.')
print('In order to STOP entering values, write "END" and hit enter.')
print()
print()
temperature = []
count = 0

while True:
    t = input('Enter a value (or enter the word "STOP" to stop new entries: ')

    if t == "STOP":
        break
    count += 1
    try: num = float(t)
    except:
        print("invalid temperature entry")
        continue
    temperature.append(num)

temperature.sort()
print("The highest temperature is: ",temperature[-1],"degrees")
print("The lowest temperature is: ",temperature[0],"degrees")
print()
print("The number of temperatures entered was: ",count)


print()
print("Thank you and Have a good day.")


