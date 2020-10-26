#DSC 510
#Week 8
#Programming Assignment Week 8
#Author Jake Rickord
#10/24/2020

import string
##since this was not a listed parameter, using a global variable to keep track of wordcount
global wordtotal

def add_word(newWord, wordDict):
    global wordtotal
    ##increase word total for next word of text
    wordtotal+=1
    ##if word has not been repeated yet, create new entry for it, else increase it's existing counter by 1
    if newWord not in wordDict:
        wordDict[newWord]=1
    else:
        wordDict[newWord] += 1

def Process_line(newLine, wordDict):
    ##removes trailing characters
    newLine=newLine.rstrip()
    ##removes punctuation
    newLine=newLine.translate(line.maketrans('','',string.punctuation))
    #turned line to lowercase
    newLine=newLine.lower()
    #breaks code into words by themselves
    wordList = newLine.split()
    #iterates word by word through line and calls add_word function
    for word in wordList:
        add_word(word, wordDict)

def Pretty_print(wordDict):
    ##sorts dictionary based on values, largest to smallest
    sort_Dict=sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
    #prints total word count
    print("Total # of words: {}".format(wordtotal))
    print("Word              Count")
    print("-----------------------")
    #ensures correct spacing from word to value under banner
    for keyValue in sort_Dict:
        numSpaces=16-len(keyValue[0])
        print(keyValue[0],' '*numSpaces, keyValue[1])

#preset variables and create dictionary
global wordtotal
wordtotal=0
wordcount=dict()
#file reading
gba_file = open('C:\gettysburg.txt')
for line in gba_file:
    Process_line(line, wordcount)
Pretty_print(wordcount)
