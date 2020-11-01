#DSC 510#
#Week 9#
#Programming Assignment Week 8#
#Author: Brett Sutow#
#10/31/2020#
#If changes made please fill-out log#
#Change:#
#Changes Made:#
#Date of Change:#
#Author:#
#Change Approved By:#
#Date Moved to Production:#
outputfile = input("Enter the filename of the report: ")
with open(outputfile, 'r') as f:
    f.read
#The above reads the file and creates a new variable reading the file within#
import string
def add_word(word,dict):
  if word in dict:
        dict[word] += 1
  else:
        dict [word] = 1
#The above imports string and then defines add_word as a function with a dictionary within it.#
# Which counts the words. Creating the overall total times a word is said#

def process_line (line, dict):
    line = line.strip()
    linesplit = line.split()
    for word in linesplit:
        if word != '--':
            word = word.lower()
            word = word.strip(string.punctuation)
            add_word(word,dict)
#The above function defines what we should count as words within the add_word dictionary.#
# Thus, not counting punctuation or other objects that shouldn't be counted#

gba_file = open('gettysburg.txt' , 'a+')
def process_print(dict):
    resultslist=[]
    with open(outputfile, "a+") as infile:
        for letters,num in dict.items():
            resultslist.append((num,letters))
    resultslist.sort(reverse=True)
    print('{:10}{:10}'.format('Word', 'Number Said'), file=gba_file)
    print(('__'*12),file=gba_file)
    for num,letters in resultslist:
        print('{:14s} {:d}'.format(letters,num), file=gba_file)

#The above works on the formatting of the list, placing word/times said in respected areas.#
#The above also creates the underline for column titles, as well as orders them highest to lowest#
#a+ was used to append the text file without overwriting it. This is used so it does not delete the address#
def main():
    dict={}
    gba_file = open('gettysburg.txt' , 'r+')
    with open(outputfile, "a+") as output_file:
        for line in gba_file:
            process_line(line,dict)
    print(process_print(dict), file= gba_file)
    print('Length of the Address:', len(dict), file= gba_file)
print(main())
#The above main() prints everything as one. It pulls in all the functions we defined earlier in the code.#
#This also creates a new file with gba_file utilizing the r+ to read the file, it then writes the length of the address#
