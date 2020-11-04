# File: rattanavilay_assignment_9.1.py
# Assignment: 9.1
# Course: DSC 510
# Week 9
# Programming Assignment Week 9
# Author: Thip Rattanavilay
# DATE: 11/1/2020


"""
For this week we will modify our Gettysburg processing program from week 8 in order to generate a text 
file from the output rather than printing to the screen. Your program should have a new function called 
process_file which prints to the file (this method should almost be the same as the pretty_print function 
from last week. Keep in mind that we have print statements in main as well. Your program must modify the 
print statements from main as well.

Your program must have a header. 
Create a new function called process_fie. This function will perform the same operations as pretty_print 
from week 8 however it will print to a file instead of to the screen.
Modify your main method to print the length of the dictionary to the file as opposed to the screen.
This will require that you open the file twice. Once in main and once in process_file.
Prompt the user for the filename they wish to use to generate the report.
Use the filename specified by the user to write the file.
This will require you to pass the file as an additional parameter to your new process_file function.

"""

# Welcoming statement
print("Welcome to Calculate the total words!")
print("")
# Display Welcome Message to customer
Name = input("What is your name?")
print("")
# Display Welcome Message to customer
print("Welcome,", Name, "!")

import string
def add_word(words, dictionary):  # adds the words to the dictionary and get the word counts
    for word in words:
        if word not in dictionary:
            # if the word has not occurred yet set count to 1
            dictionary[word] = 1
        else:
            dictionary[word] += 1  # if it has occurred increment by one


# strip off various characters, split out the words, and cleans the file
def process_line(line, dictionary):
    # removes all punctuation by changing to None
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()  # converts to lower case
    words = line.split()  # splits the words out
    add_word(words, dictionary)


def process_file(dictionary, user_file):  # prints the results in a cleaner way
    sort_list = list()
    # opens file as write and names it what the user input
    with open("{}.txt".format(user_file), 'w') as wf:
        # wf.write("Length of the dictionary: {} \n".format(len(dictionary))) #writes the length of dictionary
        wf.write("Count \t Word \n-------------------\n")  # header
        # changes to list to be able to sort
        for key, value in list(dictionary.items()):
            sort_list.append((value, key))
            sort_list.sort(reverse=True)
        for key, value in sort_list[:]:  # writes each item from list to file
            wf.write("{:4} \t {:10} \t \n".format(key, value))
            # print(key, value)


def main():  # main function that opens the file and creates an empty dictionary
    gba_file = open('gettysburg.txt', 'r')
    counts = dict()
    user_file = input('Please enter a a name for your report: ')
    for line in gba_file:  # for each line in the file run process_line method
        process_line(line, counts)
    process_file(counts, user_file)
    # opens the file as read/write and adds count of dictionary at the beginning
    with open("{}.txt".format(user_file), 'r+') as wf:
        lines = wf.readlines()
        wf.seek(0)
        wf.write("Length of the dictionary: {} \n \n".format(len(counts)))
        wf.writelines(lines)


main()
