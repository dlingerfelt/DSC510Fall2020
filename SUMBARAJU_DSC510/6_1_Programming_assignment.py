# DSC 510

# Week 6

# Programming Assignment Week 6 - 6_1_Programming_assignment.py

# Author Aditya Sumbaraju

# 10/10/2020

# Change Control Log:

# Change#:1
# Change(s) Made: NA
# Date of Change: 10/10/2020
# Author: Aditya Sumbaraju
# Change Approved by: Catie Williams
# Date Moved to Production: 10/10/2020


from datetime import date


# Color definitions
class color:
    RED = '\033[91m'
    END = '\033[0m'
    BLUE = '\033[94m'


today = date.today()
executionDate = today.strftime("%m/%d/%y")
# empty list to capture temperatures with scale
temperatures = []
# List to sort temperature values
conval_far_lists = []


# function to find min and max temperature values by providing suffixed input and non suffixed input arguments
def validateMinMaxTemp(tempList, f_c_suffix):
    # find the index of min and max temperature values
    tempIndexMax = tempList.index(max(tempList))
    tempIndexMin = tempList.index(min(tempList))

    # print min and max temperature values from user input
    print(color.BLUE + "Minimum temperature is %s" % (f_c_suffix[tempIndexMin]) + color.END)
    print(color.BLUE + "Maximum temperature is %s" % (f_c_suffix[tempIndexMax]) + color.END)
    print(color.BLUE + "There were %i valid temperatures entered" % len(tempList) + " and the valid temperature list is -> " + str(
        f_c_suffix) + color.END)
    return


# function to check for fahrenheit minimum scale value.
def fahrLimitCheck(temp):
    var_Temp = temp[:-1]  # strip fahrenheit scale from string for calculation
    if temp[-1] == "F" or temp[-1] == "f":
        if (float(var_Temp) < -459.67):
            print(color.RED + "Below -459.67 is not a valid Fahrenheit value " + color.END)
            return
        else:
            return float(var_Temp), temp


# function to print program banner
def print_banner():
    prompt1 = "*  Enter value suffixed by F/f -> Fahrenheit *\n"
    prompt2 = "*  Type 'q' to quit                          *\n"
    example = "*  Here's an example of input: 30F           *\n"
    prompt3 = color.BLUE + '  Execution Date: ' + executionDate + color.END + '                  *\n'
    stars = ("*" * 58) + "\n"
    print(stars + prompt1 + prompt2 + example + '*' + prompt3 + "\n" + stars)


# main function to accept the values from user and calls fahrenheit limit check function before appending the values to the list.
# allows only one character F or f
def main():
    while True:
        inpvalTemp = input(
            color.BLUE + "Please enter temperatures suffixed with F or f one by one" + " :")

        if inpvalTemp == "q":  # sentinel value as q to stop user input
            validateMinMaxTemp(conval_far_lists, temperatures)
            break
        else:
            try:
                if any(i == inpvalTemp[-1] for i in ["F", "f"]):  # check input for fahrenheit scale
                    a = float(inpvalTemp[0:-1]) # a check to identify if there are any other characters along with F
                    try:
                        conval_far, inputval = fahrLimitCheck(
                            inpvalTemp)  # value and suffix are separated and assigned to variables
                        conval_far_lists.append(conval_far)  # appends float values to list
                        temperatures.append(inputval)  # appends input values to the list
                    except:
                        pass
                else:
                    raise ValueError
            except ValueError:
                print(color.RED + "Invalid input - please enter correct format as per instructions." + color.END)


if __name__ == '__main__':
    print_banner()  # function call to print banner.
    main()  # function call to main function
