# DSC 510
# Week 8
# Programming Assignment Week8 - Prompt the user to input a list of temperatures. Determine the max, min, and count.
# Author: David Brehm
# 10/19/2020

# Change Log:
# No changes.

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


def Pretty_print(wordDict):
    """
    Prints the word dictionary in the format:
    Length of the dictionary: -count-
    Word        Count
    -----------------
    word1       count1
    word2       count2
    ...         ...
    :param wordDict: Dictionary to keep count of word occurrences.
    :return: No return.
    """
    length = len(wordDict)  # Length of dictionary.
    sorted_desc = OrderedDict(sorted(wordDict.items(), key=lambda kk: kk[1], reverse=True))  # Dictionary ordered desc.
    print("Length of the dictionary: %d" % length)  # Print length of dictionary
    print("Word                Count")
    print("-------------------------")
    for k in sorted_desc:
        print(f'{k:<20}{sorted_desc[k]}')  # Space the Word column out 20 characters to align the Count column.


def main():
    """
    Main function. Opens the input file and calls Process_line on each line. The output is then printed with the
    function Pretty_print.
    :return: No return.
    """
    gba_file = open('gettysburg.txt', 'r')  # Input file.
    out_dict = {}  # Initialize output dictionary.
    for line in gba_file:
        if not line.strip():  # Don't use empty lines.
            continue
        Process_line(line, out_dict)  # Call Process_line for each line of the input text.
    Pretty_print(out_dict)  # Print results.


if __name__ == "__main__":
    main()
