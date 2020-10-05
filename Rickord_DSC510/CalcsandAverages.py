#DSC 510
#Week 5
#Programming Assignment Week 5
#Author Jake Rickord
#09/30/2020

#prevents users from entering incorrect datatypes based on number of inputs required as errorInputnumbers, prompted by request message
def errorCheck(errorInputNumbers, requestMessage, errorMessage, resultType):
    error_created = False
    resultList=[]
    #iterates through, once user entered data is able to be cast into target datatype, kick the while loop
    while error_created != True:
        try:
            #for loop allows us to carry out process for multiple items in one go, returned via a list
            for x in range(errorInputNumbers):
                resultList.append(resultType(input(requestMessage)))
            error_created = True
            return resultList
        except:
            #if datatype is incorrect, print out error message and essentially restart the process
            print(errorMessage)
            resultList=[]
            print()

def performCalculation (operator):
    #spacing
    print(" ")
    #call errorcheck to grab two numbers for our calculations
    numList=errorCheck(2, "Please enter a number: ", "One of the values entered was non-numerical, please try again", float)
    #from list returned by errorcheck, grab our two numbers
    num1 = numList[0]
    num2 = numList[1]
    #perform calculation requested by user
    if(operator == '+'):
        print("The result of the addition of these two numbers is: "+ str(num1 + num2)+".")
        print()
    elif(operator == '-'):
        print("The result of the subtraction of these two numbers is: "+ str(num1 - num2)+".")
        print()
    elif(operator == '*'):
        print("The result of the multiplication of these two numbers is: "+ str(num1 * num2)+".")
        print()
    elif(operator == '/'):
        print("The result of the division of these two numbers is: "+ str(num1 / num2)+".")
        print()

def calculateAverage():
    #spacing
    print(" ")
    avgTotal=0
    #call errorCheck to grab amount of numbers we will average
    numList=errorCheck(1, "How Many Numbers Do You Wish To Average? ", "The value you entered was non-numerical, please try again", int)
    #ensure they didn't enter negative or zero value integer
    while numList[0] <= 0:
        numList=errorCheck(1, "The value you entered was negative or zero, please enter in the quantity of numbers you'd like to average: ", "The value you entered was non-numerical, please try again", int)
    #for loop iterates through and takes new value from 0 position in reset list and adds it to running total
    for x in range(numList[0]):
        newNum=errorCheck(1, "Enter in a Number to add to your Total: ", "The value you entered was non-numerical, please try again", float)
        avgTotal=avgTotal+newNum[0]
    #performs average calculation and outputs it to console
    print("The average of the numbers you entered is: " + str(avgTotal/numList[0]) + ".")
    print()


sentinelValue = '0'
userValue = 1

print("Welcome to the Arithmetic Operations Calculator!")

#provides for user input to kill program
while(userValue !=sentinelValue):
    #calls errorCheck to ensure their choice between programs
    calculationType=errorCheck(1, "Enter in 1 for simple arithmetic operations, or 2 for an average: ", "You entered in a non-numeric value, please try again", int)
    #ensures they choose an appropriate value as well
    while (calculationType[0]!=1) and (calculationType[0]!=2):
        print("You entered in a value other than 1 or 2, please try again")
        print()
        calculationType=errorCheck(1, "Enter in 1 for simple arithmetic operations, or 2 for an average: ", "You entered in a non-numeric value, please try again ", int)
    #now check if they want arithmetic operations or average function
    if(calculationType[0]==1):
        operator=input("Enter in the operator for the operation you'd like to perform (+ for addition, - for subtraction, * for multiplication, or / for division): ")
        #checks to ensure operator is valid
        while(operator!='+') and (operator!='-') and (operator!='*') and (operator!='/'):
            operator = input("You entered an incorrect operator, as a reminder, please use + for addition, - for subtraction, * for multiplication, or / for division): ")
        #calls performCalculation function
        performCalculation(operator)
    else:
        #if not the simple arithmetic operations, call average function
        calculateAverage()
    #check to see if user wants to end
    userValue = input("Enter in 0 if you would like to end the program, otherwise type anything else: ")
