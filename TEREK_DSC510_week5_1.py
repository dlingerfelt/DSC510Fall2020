#DSC 510
#Week 5
#Programming Assignment Week 5_1
#Author Kim Terek
#10/03/2020

import math

print()
 #USER INPUTS START HERE
print('Hello. We will be performing a simple calculation against 2 values for you today.')
print()
a = float(input("Enter value a to calculate: "))
b = float(input("Enter value b to calculate against a: "))
print()
print("To add a + b, enter       1")
print("To subtract a - b, enter  2")
print("To multiply a * b, enter  3")
print("To divide a / b, enter    4")
#def get_operation(prompt)
 #   operation = input(prompt)
#    while operation not in ("+","-","*","/")
 #       operation = input(prompt)
e = int(input("Which math calculation would you like to perform on a and b (1,2,3, or 4)? "))
print()

#SECTION FOR FN1 defined:
def performCalculation():
    if e==1:
        print(a + b)
    elif e==2:
        print(a - b)
    elif e==3:
        print(a * b)
    elif e==4:
        print(a / b)
    else:
        print('0 (did not calculate)')

print("Calculation RESULTS:  (or if there was an entry error = 0 'did not calculate')")
print()
performCalculation()

 #USER INPUTS START HERE

print()
print('Next calculation or Have a good day.')
print()
print('Next Calculation will provide a running average of entered numbers.')
print('You will be allowed to enter as many values as desired to find the average against.')
print('In order to STOP entering values,')
print('Hit the "ENTER" key instead. It will end and perform the avg calculation.')
print()
CumSum = 0
count = 0
avg = 0

while True:
    num = input('Enter a value (or press "ENTER" without a value to end): ')
    if num == "":
        break
    CumSum += float(num)
    count += 1
    avg = CumSum / count
def CalculateAverage():
    print(avg)
print("The Average of your entered values is: ")
CalculateAverage()
print()
print("Thank you and Have a good day.")




