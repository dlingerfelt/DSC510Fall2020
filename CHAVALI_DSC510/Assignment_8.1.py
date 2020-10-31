# DSC510
# Week 8 Assignment - Assignment_8.1.py
# calculating Word frequency
# Author Sowmya Chavali
# 10/22/20
import string

# This function checks if an individual word is in the dictionary and adds it as a key if it is not present.
def add_word(w,dict):
    if w not in dict.keys():
        dict[w] = 0
    dict[w] += 1

# Process_line cleans a line of text from the input and calls add_word() to add the words from
# each line to the dictionary.
def process_line(text,file_dict):
    for s in text:
        # stripping punctuation
        no_punct=s.translate(str.maketrans('', '', string.punctuation))
        # Convert to lowercase and split words into a list.
        words = no_punct.lower().split()
        for word in words:
            add_word(word,file_dict)

#This function prints the word frequency from the dictionary
def pretty_print(wordDict):
    print("Length of the dictionary: %i" %len(wordDict))
    print("Word           Count")
    print("------------------------")
    for w in sorted(wordDict, key =wordDict.get, reverse=True):
        print("%12s     %s" % (w.ljust(12), wordDict[w]))

def main():
    gba_file = open('gettysburg.txt', 'r')  # opening the text file in read mode
    file_dict = {}
    lines = [line.rstrip('\n') for line in gba_file]  # getting rid of newline chars
    process_line(lines, file_dict)
    pretty_print(file_dict)

main()
