# DSC510
# Week 8 Assignment - Assignment_8.1.py
# calculating Word frequency to a file
# Author Sowmya Chavali
# 10/31/20
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

#This function prints the word frequency from the dictionary to a file
def process_file(wordDict,textfile):
    with open(textfile,'a') as tf:
        tf.write("Word           Count\n")
        tf.write("-------------------------------\n")
        for w in sorted(wordDict, key =wordDict.get, reverse=True):
            tf.write("%12s     %s\n" % (w.ljust(12), wordDict[w]))
    print("Output to {0}".format(textfile))

def main():
    gba_file = open('gettysburg.txt', 'r')  # opening the text file in read mode
    file_dict = {}
    lines = [line.rstrip('\n') for line in gba_file]  # getting rid of newline chars
    process_line(lines, file_dict)
    text_file = input('Enter the output file name with .txt extension:')
    with open(text_file,'w') as tf:
        tf.write("Size of dictionary: %i\n" %len(file_dict))  #calculating the dictionary size
    process_file(file_dict,text_file)
    gba_file.close()     #Closing files
    tf.close()
   

main()
