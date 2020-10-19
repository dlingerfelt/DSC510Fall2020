# DSC510 Week 6 Assignment - Temp_List.py
# Temperature Lists
# Author: Matthew Fikes
# 10/6/2020

# create empty lists, one for inputs including degree scale and one for calculation
inputTemps = []
calcTemps = []

# function to find high and low values
def TempCompare(valueTemps,tempsWithScale):

# find the index of the high and low temperatures in the list
    maxTempIndex = valueTemps.index(max(valueTemps))
    minTempIndex = valueTemps.index(min(valueTemps))

# print the high and low with original scale, using the indices from the calculation
    print("The lowest temperature in the range is %s" %(tempsWithScale[minTempIndex]))
    print("The highest temperature in the range is %s" %(tempsWithScale[maxTempIndex]))

    print("There were %i temperatures entered" %len(valueTemps))
    return

# function for scaling all input temps to Kelvin for comparison
def TempEval(temp):
    convertTemp = temp[:-1] # strip degree scale from string for calculation
    if temp[-1] == "K":
        if float(convertTemp) < 0:
            print("Values below zero are not valid in Kelvin scale")
            return
        else:
            return float(convertTemp), temp
    elif temp[-1] == "C":
        if (float(convertTemp) <-273.15):
            print("Values below 273.15 are not valid in Celsius scale")
        else:
            convertTemp = float(convertTemp) + 273.15 # Convert Celsius to Kelvin
            return float(convertTemp), temp
    elif temp[-1] == "F":
        if (float(convertTemp) <-459.67):
            print("Values below 459.67 are not valid in Fahrenheit scale")
        else:
            convertTemp = (float(convertTemp)-32)*5/9+273.15 # Convert Fahrenheit to Kelvin
            return float(convertTemp), temp


print("Enter temperatures to compare, enter \"done\" to quit")
print("Format temperatures as follows: #F for Fahrenheit, #C for Celsius, #K for Kelvin")

degTypes = ["C", "F", "K"] # create list of valid degree ranges to check against

while True:
    userTemp = input("Input temperature: ")

    if userTemp == "done":
        TempCompare(calcTemps, inputTemps)
        break
    else:
        try:
            if any(x == userTemp[-1] for x in degTypes): # check input for valid degree scales
                try:
                    tempInK, originalTemp = TempEval(userTemp) # check input for valid value in corresponding scale

                    calcTemps.append(tempInK)
                    inputTemps.append(originalTemp)
                except:
                    pass
            else: raise ValueError
        except ValueError:
            print("Invalid input - please ensure format is correct.")

