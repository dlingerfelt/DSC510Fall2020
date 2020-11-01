# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Adonis Shareef
# 10/23/2020

# Change#:
# Change(s) Made: add_word(dict,word) function to add word to dictionary, Process_Line to remove punc , and Pretty_print to print
# Date of Change: 10/23/2020
# Author: Adonis Shareef
# Change Approved by: Adonis Shareef
# Date Moved to Production: 10/23/2020

import string
def add_word(dict,word):
    #check if word is already in dictionary
    if word not in dict:
        dict[word] = 0
    dict[word] += 1 #increment word by 1 if in dictionary

def Process_line(dict,text):
    for t in text:
        nopunc = t.translate(str.maketrans("","",string.punctuation)) # remove punctuation
        words = nopunc.lower().split()
        for w in words:
            add_word(dict,w)

def pretty_print(dict):
    print("Length of the dictionary: %i" %len(dict))
    print("Word           Count")
    print("--"*12)
    #sort the dictionary
    for w in sorted(dict, key = dict.get, reverse=True):
         print("%15s    %2s" % (str(w),  str(dict[w]).ljust(2)))


def main():
    gba_file = open('gettysburg.txt', 'r')  # Input file.
    dict = {}
    lines = [line.rstrip('\n') for line in gba_file]  # getting rid of newline chars
    Process_line(dict, lines)
    pretty_print(dict)  # Print results.

if __name__ == "__main__":
    main()
