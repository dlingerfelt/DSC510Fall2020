# DSC510 Week 8 Assignment - Word_Count.py
# Count instances of words in Gettysburg Address
# Author: Matthew Fikes
# 10/20/2020
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
def Pretty_print(dictionary):
    print("Size of dictionary: %i" %len(dictionary))
    print("           Word    Count")
    print("-------------------------------------")
    for w in sorted(dictionary, key =dictionary.get, reverse=True):
        print("%15s    %2s" % (str(w),  str(dictionary[w]).ljust(2)))

# main function to open file, split text into lines, and run others
def main():
    gba_file = open('gettysburg.txt','r')
    gba_dict = {}
    text = gba_file.read()
    lines = text.split('\n')
    Process_line(lines, gba_dict)
    Pretty_print(gba_dict)

main()


