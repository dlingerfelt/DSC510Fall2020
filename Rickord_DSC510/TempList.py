#DSC 510
#Week 5
#Programming Assignment Week 5
#Author Jake Rickord
#10/07/2020

#prevents users from entering incorrect datatypes based on number of inputs required as errorInputnumbers, prompted by request message
def errorCheck(requestMessage, errorMessage, resultType):
    error_created = False
    #iterates through, once user entered data is able to be cast into target datatype, kick the while loop
    while error_created != True:
        try:
            #request user input
            a=input(requestMessage)
            #check if equal to sentinel value, if so, return a (which will append to end of list)
            if a=="#":
                return a
            #if not, it's a valid float so append that
            else:
                return resultType(a)
        except:
            #if datatype is incorrect, print out error message and essentially restart the process
            print(errorMessage)
            print()

#create empty List
temperatures = []

#create Sentinel Value and User Value to check against
Sentinel = "#"
UserValue = ""

#initiate base of program and continue until sentinel value is entered
while (Sentinel != UserValue):
    #check if valid float, if so then append, or if = sentinel value, this will append to temperatures list
    temperatures.append(errorCheck("Enter in a temperature, or enter # if complete: ", "You entered a non-numeric value, please try again", float))
    #check to see if we ended up appending the #, ending the while loop and stripping that last value off
    if(temperatures[len(temperatures)-1]=="#"):
        UserValue = "#"
        del temperatures[-1]
print("")
#find max temp
largest_Temp = max(temperatures)
#find min temp
smallest_Temp = min(temperatures)
#find temp count
num_Temps_Entered = len(temperatures)
#print
print("The largest temperature entered was %.2f degrees." % largest_Temp)
print("The smallest temperature entered was %.2f degrees." % smallest_Temp)
print("The number of temperatures entered was %d." %num_Temps_Entered)
