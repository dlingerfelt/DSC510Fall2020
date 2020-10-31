# DSC 510
# Week 8
# Programming Assignment Week 8 - 8_1_Programming_assignment.py
# Author Aditya Sumbaraju
# 10/10/2020
# Change Control Log:

# Change#:1
# Change(s) Made: NA
# Date of Change: 10/23/2020
# Author: Aditya Sumbaraju
# Change Approved by: Catie Williams
# Date Moved to Production: 10/23/2020

import pathlib
import re
from collections import OrderedDict
from datetime import date


# color class
class color:
    BLUE = '\033[94m'  # Color class:BLUE prints the line in blue
    BOLD = '\033[1m'  # Color class:BOLD prints the line in bold text
    END = '\033[0m'  # class:END; ends the color on a given line issued to print


def add_word(v_Word, w_Dict):
    """
    Add_word - add words to the dictionary if the occurrence of word is not in file
    and the control increments by 1 until it reaches EOF.
    :param1 v_Word: passing a word from input in main()
    :param2 w_Dict: Dictionary to maintain word and it's count.
    :return: No return value.
    """
    if v_Word not in w_Dict.keys():  # Adds the word to the dictionary as a key if it does not exist.
        w_Dict[v_Word] = 0
    w_Dict[v_Word] += 1


def Process_line(fileLineItem, w_Dict):
    """
    Process_line function applies cleansing rules
        1. removing special characters
        2. converting word to lowercase and split the words from given line
    in given line of text from the input file and calls add_word() function to add the words from each line to the
    word dictionary.
    :param fileLineItem: Line of text from the input file.
    :param w_Dict: Dictionary to keep count of word occurrences.
    function Call add_word() on each word in the word list using for loop.
    :return: No return value.
    """
    onlyText = re.sub(r'[^\w\s]', '', fileLineItem)
    word_list = onlyText.lower().split()
    for i in word_list:
        add_word(i, w_Dict)


def Pretty_print(w_Dict):
    """
    this function prints the word dictionary:
    Length of the dictionary: -count-
    :param w_Dict: Dictionary stores the count of word occurrences.
    :return: No return value.
    """
    # print(w_Dict)
    today = date.today()
    progRunDt = today.strftime("%m/%d/%y")  # The USA date Format
    v_sort_dict = sorted(w_Dict.items(), key=lambda x: x[1], reverse=True)
    sort_dict = OrderedDict(v_sort_dict)
    print(color.BLUE + 'program run date:  ' + color.END + progRunDt)
    print('{1}  {0}'.format(len(w_Dict), color.BLUE + 'Length of the dictionary:' + color.END))
    print('{word:<14} {count}'.format(word='Word', count='Count'))
    print("-------------------")
    print("\n".join("{: <14} {}".format(k, v) for k, v in sort_dict.items()))


def main():
    """
    checks for file existence.
    function main()- Opens the input file placed in the same path as of .py file
    function call: Process_line for each line of gettysburg.txt file.
    function call:Pretty_print to Print results in rows and columns format.
    :return: No return value.
    """

    file = pathlib.Path("gettysburg.txt")
    if file.exists():
        gba_file = open('gettysburg.txt', 'r')
        v_dict = {}
        for line in gba_file:
            if len(line.strip()) == 0:
                continue
            Process_line(line, v_dict)
        Pretty_print(v_dict)
    else:
        print("File not exist")


# Program starts here
if __name__ == "__main__":
    main()
