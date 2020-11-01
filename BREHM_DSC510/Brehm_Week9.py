# DSC 510
# Week 9
# Programming Assignment Week9 - Modify Gettysburg processing program to generate a text file output.
# Author: David Brehm
# 10/31/2020

# Change Log:
# No changes.

import os
import re
from collections import OrderedDict


def add_word(word, wordDict):
    """
    Add_word checks if an individual word is in the word dictionary and adds it as a key if it is not present. The
    occurrences of that word is then incremented by one.
    :param word: Word from the input
    :param wordDict: Dictionary to keep count of word occurrences.
    :return: No return.
    """
    if word not in wordDict.keys():  # Adds the word to the dictionary as a key if it does not exist.
        wordDict[word] = 0
    wordDict[word] += 1  # Increment the count for the word.


def Process_line(inLine, wordDict):
    """
    Process_line cleans a line of text from the input file and calls add_word() to add the words from each line to the
    word dictionary.
    :param inLine: Line of text from the input file.
    :param wordDict: Dictionary to keep count of word occurrences.
    :return: No return.
    """
    alphanum = re.sub(r'[^\w\s]', '', inLine)  # Keep alphanumeric and whitespace.
    word_list = alphanum.lower().split()  # Convert to lowercase and split words into a list.
    [add_word(i, wordDict) for i in word_list]  # Call add_word() on each word in the word list.


def process_file(wordDict,outFile):
    """
    Prints the word dictionary to an output file in the format:
    Length of the dictionary: -count-
    Word        Count
    -----------------
    word1       count1
    word2       count2
    ...         ...
    :param wordDict: Dictionary to keep count of word occurrences.
    :param outFile: Complete path for the output file.
    :return: No return.
    """
    length = len(wordDict)  # Length of dictionary.
    sorted_desc = OrderedDict(sorted(wordDict.items(), key=lambda kk: kk[1], reverse=True))  # Dictionary ordered desc.
    with open(outFile,'w') as output:
        output.write("Length of the dictionary: %d\n" % length) # Print length of dictionary
        output.write("Word                Count\n")
        output.write("-------------------------\n")
        for k in sorted_desc:
            output.write(f'{k:<20}{sorted_desc[k]}\n')  # Space the Word column out 20 characters to align the Count column.


def main():
    """
    Main function. Opens the input file and calls Process_line on each line. The output is then printed to a user
    specified output text file with the function process_file.
    :return: No return.
    """
    gba_file = open('gettysburg.txt', 'r')  # Input file.
    out_dict = {}  # Initialize output dictionary.
    for line in gba_file:
        if not line.strip():  # Don't use empty lines.
            continue
        Process_line(line, out_dict)  # Call Process_line for each line of the input text.

    print('Input the desired path for your output file:')
    while True:
        path = input()
        if os.path.isdir(path):  # Check if the file path exists.
            break
        else:
            print('Please enter a valid path.')

    print('Input the desired filename for your output text file:')
    while True:
        filename = input()
        if filename[-4:] == '.txt':  # Check if the filename is a text file.
            break
        else:
            print('Please enter a text file (.txt).')

    full_out = "{}\{}".format(path,filename)
    process_file(out_dict,full_out)  # Generate the output file.


if __name__ == "__main__":
    main()
