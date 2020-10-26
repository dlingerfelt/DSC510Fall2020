# File: rattanavilay_assignment_8.1.py
# Assignment: 8.1
# Course: DSC 510
# Week 8
# Programming Assignment Week 8
# Author: Thip Rattanavilay
# DATE: 10/20/2020


"""

We will create a program which performs three essential operations. It will process this .txt file: Gettysburg.txt. (Click the link to download the text file).  Calculate the total words, and output the number of occurrences of each word in the file.

Open the file and process each line.
Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
Nicely print the output, in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
We want to achieve each major goal with a function (one function, one action). We can find four functions that need to be created.

add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.

Process_line: There is some work to be done to process the line: strip off various characters, split out the words, and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No return value.

Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might need to modify it later), we separated out the printing function. The parameter is a dictionary. No return value.

main: We will use a main function as the main program. As usual, it will open the file and call process_line on each line. When finished, it will call pretty_print to print the dictionary.

In the main function, you will need to open the file. We will cover more regarding opening of files next week but I wanted to provide you with the block of code you will utilize to open the file, see below.
"""

# Welcoming statement
print("Welcome to Calculate the total words!")
print("")
# Display Welcome Message to customer
Name = input("What is your name?")
print("")
# Display Welcome Message to customer
print("Welcome,", Name, "!")

import string # import string
def add_word(words, dictionary):  # adds the words to the dictionary and get the word counts
    for word in words:
        if word not in dictionary:
            dictionary[word] = 1 # if the word has not occurred yet set count to 1
        else:
            dictionary[word] += 1  # if it has occurred increment by one


# strip off various characters, split out the words, and cleans the file
def process_line(line, dictionary):
    line = line.translate(str.maketrans('', '', string.punctuation)) # removes all punctuation by changing to None
    line = line.lower()  # converts to lower case
    words = line.split()  # splits the words out
    add_word(words, dictionary) #add word dictionary


def pretty_print(dictionary):  # prints the results in a cleaner way
    print("Length of the dictionary: ", len(dictionary))
    print("Word \t \t \t \t Count \n--------------------------")
    for key, value in dictionary.items():
        print("{:15} \t {:4} \t".format(key, value))


def main():  # main function that opens the file and creates an empty dictionary
    gba_file = open('gettysburg.txt', 'r') # Open the gettysburg text file
    counts = dict() # count equals dic
    for line in gba_file:  # for each line in the file run process_line method
        process_line(line, counts)
    pretty_print(counts) # print pretty for counts


main()
