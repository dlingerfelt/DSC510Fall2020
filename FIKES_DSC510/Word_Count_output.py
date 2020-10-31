# DSC510 Week 9 Assignment - Word_Count_output.py
# Count instances of words in Gettysburg Address, output to file
# Author: Matthew Fikes
# 10/20/20

# CHANGE# : 1
# Change(s): converted print output to output to file instead, updated header
# Change(s): Moved count of directory out of print function into main
# Date of Change: 10/26/20

import string

# function for adding word or incrementing count
def add_word(word, dictionary):
    if word.lower() in dictionary:
        dictionary[word.lower()]+=1
    else:
        dictionary[word.lower()]=1

# function to clean each line of text and split it into words
def Process_line(text, dictionary):
    for i in text:
        line_nopunc = i.translate(str.maketrans("","",string.punctuation)) # removes punctuation
        isolated_words = line_nopunc.split()
        for w in isolated_words:
            add_word(w,dictionary)

# function to output results neatly
def Process_file(dictionary,filename):
    with open(filename+'.txt','a') as wf:
        wf.write("           Word    Count\n")
        wf.write("-------------------------------------\n")
        for w in sorted(dictionary, key =dictionary.get, reverse=True):
            wf.write("%15s    %2s\n" % (str(w),  str(dictionary[w]).ljust(2)))
    print("Data output to {0}.txt".format(filename))

# main function to open file, split text into lines, and run others
def main():
    gba_file = open('gettysburg.txt','r')
    gba_dict = {}
    text = gba_file.read()
    lines = text.split('\n')
    Process_line(lines, gba_dict)
    filename = input('Enter filename for output file:')
    with open(filename+'.txt','w') as wf:
        wf.write("Size of dictionary: %i\n" %len(gba_dict))

    Process_file(gba_dict,filename)

main()


