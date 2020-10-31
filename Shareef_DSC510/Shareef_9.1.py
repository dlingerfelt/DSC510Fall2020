# DSC 510
# Week 9
# Programming Assignment Week 9
# Author Adonis Shareef
# 10/29/2020

# Change#:
# Change(s) Made: Process_File() writing to a file instead of console
# Date of Change: 10/29/2020
# Author: Adonis Shareef
# Change Approved by: Adonis Shareef
# Date Moved to Production: 10/29/2020

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

# function to output results neatly
def Process_file(dict,filename):
      #context manager has to append here because in main we write first
    with open(filename+'.txt','a') as cm:
        cm.write("           Word    Count\n")
        cm.write("--"*12+"\n")
        for w in sorted(dict, key =dict.get, reverse=True):
            cm.write("%15s    %2s\n" % (str(w),  str(dict[w]).ljust(2)))
    print("Processed in {0}.txt".format(filename))


def main():
    gba_file = open('gettysburg.txt', 'r')  # Input file.
    dict = {}
    lines = [line.rstrip('\n') for line in gba_file]  # getting rid of newline chars
    Process_line(dict, lines)
    filename = input("Enter a filename to write to") #ask user for filename
     #context manager is writing here
    with open(filename+'.txt','w') as cm:
        cm.write("Length of the dictionary: %i" %len(dict)+"\n") #length of dict
    Process_file(dict,filename)  # Print results.

if __name__ == "__main__":
    main()
