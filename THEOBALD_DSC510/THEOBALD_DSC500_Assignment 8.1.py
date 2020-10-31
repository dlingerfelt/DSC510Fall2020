# DSC510
# Week 8
# Programming Assignment Week 8
# Author Ammy Theobald
# 10/25/2020

# Change#:1
# Change(s) Made: Initial Program
# Date of Change: 10/25/2020
# Author: Ammy Theobald
# Change Approved by: N/A
# Date Moved to Production: 10/25/2020

import string

# add_word function increments word counter by 1 if word in dict, else adds to dict with count of 1
def add_word(word,dict):
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
# process_line function strips leading characters and punctuation,splits lines into separate words, and calls the add_word function
def process_line(line, dict):
    line = line.strip()
    linesplit = line.split()
    for word in linesplit:
        if word != '--':
            word = word.lower()
            word = word.strip(string.punctuation)
            add_word(word, dict)

# pretty_print function formats the output into a desirable format
def pretty_print(dict):
    resultslist = []
    for letters,num in dict.items():
        resultslist.append((num, letters))
    resultslist.sort(reverse=True)
    print('{:13}{:13}'.format('Word','Count'))
    print('__'*12)
    for num,letters in resultslist:
        print('{:14s} {:d}'.format(letters,num))

# main function pulls all of the functions together to process and format the file
def main():
    dict={}
    gba_file = open('gettysburg.txt','r')
    for line in gba_file:
        process_line(line,dict)
    print('Length of the Dictionary:', len(dict))
    pretty_print(dict)

print(main())
