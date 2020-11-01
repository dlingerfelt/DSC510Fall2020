#DSC 510
#Week 9
#Programming Assignment Week 9
#Author Jake Rickord
#10/28/2020

import string
import os

##removes whitespace and changes case to check again invalid naming types
def stringProcess(str_fix):
    str_fix=str_fix.rstrip()
    str_fix=str_fix.lower()
    return str_fix

def errorCheck(filename):
    file_name_is_valid = False

    #list of characters that can't be used
    invalid_chars=[]
    invalid_chars.append('<')
    invalid_chars.append('>')
    invalid_chars.append(':')
    invalid_chars.append('"')
    invalid_chars.append('/')
    invalid_chars.append(' \ ')
    invalid_chars.append('|')
    invalid_chars.append('?')
    invalid_chars.append('*')

    #list of full file names (even with spaces, hence need for .rstrip()) that are invalid on Windows
    invalid_names=[]
    invalid_names.append('con.txt')
    invalid_names.append('prn.txt')
    invalid_names.append('aux.txt')
    invalid_names.append('nul.txt')
    invalid_names.append('com1.txt')
    invalid_names.append('com2.txt')
    invalid_names.append('com3.txt')
    invalid_names.append('com4.txt')
    invalid_names.append('com5.txt')
    invalid_names.append('com6.txt')
    invalid_names.append('com7.txt')
    invalid_names.append('com8.txt')
    invalid_names.append('com9.txt')
    invalid_names.append('lpt1.txt')
    invalid_names.append('lpt2.txt')
    invalid_names.append('lpt3.txt')
    invalid_names.append('lpt4.txt')
    invalid_names.append('lpt5.txt')
    invalid_names.append('lpt6.txt')
    invalid_names.append('lpt7.txt')
    invalid_names.append('lpt8.txt')
    invalid_names.append('lpt9.txt')

    ##iterative in case user repeats error
    while(file_name_is_valid==False):
        edited_file_name=stringProcess(filename)

        ##character limit for Windows file name
        if(len(edited_file_name)>255):
            print('File Name is too long, please try again')
            filename=input('Enter File Name: ')

        ##requires ending in .txt
        if(edited_file_name.endswith('.txt')==False):
            print('File Name does not end in .txt, please try again')
            filename=input('Enter File Name: ')

        ##if they don't enter a name, since .txt is already length 4
        elif(len(filename)<5):
            print('File Name length is too short, please try again')
            filename=input('Enter File Name: ')

        else:
            #used to check that neither invalid names nor invalid characters are used
            count1=0
            count2=0
            ##iterate through list of banned file names, if user typed in invalid name, then print error message and break the for loop, else count1 = len(invalid_names)
            for i in range(len(invalid_names)):
                if(filename==invalid_names[i]):
                    print('File Name is invalid due to file naming conventions, cannot be con, prn, aux, nul, com1 - com9, or lpt1 - lpt9, please try again')
                    filename=input('Enter File Name: ')
                    break
                else: count1=i
            ##iterate through list of banned characters, if user type in invalid char, then print error message and break the for loop, else count2=len(invalid_chars)
            for i in range(len(invalid_chars)):
                if(invalid_chars[i] in filename):
                    print('File name is invalid due to file naming conventions, cannot include <, >, :, ", \, /, |, ?, nor *. Please try again')
                    filename=input('Enter File Name: ')
                    break
                else: count2=i
            ##if both for loops completed successfully, then no invalid names nor chars were found, and filename is valid! Kick out the update file name for later use
            if((count1 == 21) & (count2 == 8)):
                return filename



def add_word(newWord, wordDict):
    ##if word has not been repeated yet, create new entry for it, else increase it's existing counter by 1
    if newWord not in wordDict:
        ##increase word total for next word of text
        wordDict[newWord]=1
    else:
        wordDict[newWord] += 1

def Process_line(newLine, wordDict):
    ##removes trailing characters
    newLine=newLine.rstrip()
    ##removes punctuation
    newLine=newLine.translate(newLine.maketrans('','',string.punctuation))
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
    dict_length=len(sort_Dict)
    #prints total word count
    print("Total # of words: {}".format(dict_length))
    print("Word              Count")
    print("-----------------------")
    #ensures correct spacing from word to value under banner
    for keyValue in sort_Dict:
        numSpaces=16-len(keyValue[0])
        print(keyValue[0],' '*numSpaces, keyValue[1])

def process_file(wordDict, file_name):
    #reopen file, this time just for appending
    fout=open(file_name, 'a')
    ##sorts dictionary based on values, largest to smallest
    sort_Dict=sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
    #ensures correct spacing from word to value under banner, using existing open file
    for keyValue in sort_Dict:
        numSpaces=18-len(keyValue[0])
        fout.write(str(keyValue[0]))
        for i in range(numSpaces):
            fout.write(' ')
        fout.write(str(keyValue[1]))
        fout.write('\n')
    ##close the file now that it's all set
    fout.close()

def main():
    ##grab current directory
    dir_path = os.getcwd()
    print(dir_path)
    #preset variables and create dictionary
    wordcount=dict()
    #file reading
    gba_file = open('C:\gettysburg.txt')
    for line in gba_file:
        Process_line(line, wordcount)
    gba_file.close()

    ##error check to get File Name
    file_name=errorCheck(input('Enter File Name: '))
    #conjoin directory with file name
    file_name=os.path.join(dir_path,file_name)

    ##grab num of unique words
    dict_list=wordcount.items()
    dict_length=len(dict_list)
    #open file
    fout=open(file_name, 'w')
    num_line="Total # of words: {} \n".format(dict_length)
    #write out number of unique words
    fout.write(num_line)
    fout.write("Word            Count\n")
    fout.write("---------------------\n")
    #close the file
    fout.close()
    ##call process file to write out descending order of most common words to existing file by passing file name
    process_file(wordcount, file_name)

if __name__ == "__main__":
    main()


