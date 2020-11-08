# DSC510
# Week 9
# Programming Assignment Week 9
# Author Ammy Theobald
# 11/1/2020

# Change#:2
# Change(s) Made: added new function process_file to replace pretty_print and set to print to output file named by user
# Date of Change: 11/1/2020
# Author: Ammy Theobald
# Change Approved by: N/A
# Date Moved to Production: 11/1/2020

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

# process_file function formats the output into a desirable format and reminds the user of the output filename
def process_file(dict, filename):
   with open(filename+'.txt','a') as wf:
       wf.write("          Word Count\n")
       wf.write('______________________________\n')
       for w in sorted(dict, key=dict.get, reverse=True):
           wf.write('%15s      %2s\n' % (str(w),    str(dict[w]).ljust(2)))
   print('Thank you! Your information has been sent to {0}.txt'.format(filename))

# main function opens input file, gets output filename from user and runs all the other functions
def main():
    dict={}
    gba_file = open('gettysburg.txt','r')
    for line in gba_file:
        process_line(line,dict)
    filename = input('Please entered desired filename for output:')
    with open(filename+'.txt','w') as wf:
        wf.write('Length of the Dictionary: %i\n' %len(dict))
    process_file(dict,filename)


main()
