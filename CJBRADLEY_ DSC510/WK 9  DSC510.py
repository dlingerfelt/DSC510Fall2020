# DSC 510
# Week 9
# Author Carla J Bradley
# 10/31/2020
# Change Log - Program generate a report  based on original gettysburg.txt
# Program will count the number of words from original file.

# function add the number of words to the dictionary and count it for each
# word in the list, check if the word is in the dictionary, add the word and add 1 if it exists

def add_word(wrd, ga_dict):
    for w in wrd:
        if w not in ga_dict:
            ga_dict[w] = 1
        else:
            ga_dict[w] += 1


def process_line(ga_line, ga_dict) :           # Function to process each line in the Gettysburg Address and remove the punctuation

    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    punctuation_to_remove = ga_line
    no_punctuation = ""
    for char in punctuation_to_remove:
        if char not in punctuation:
            no_punctuation = no_punctuation + char
            no_punctuation = no_punctuation.lower()
    no_punctuation = no_punctuation.split()

    add_word(no_punctuation, ga_dict)                   # Call the add_word function to add the word
                                                        # to the dictionary and count the words


def pretty_print(ga_dict):                               # Function to print and format the dictionary and word count
    print("Length of the dictionary: %i" %len(ga_dict))  # Print length of dictionary
    print("Word             Count")
    print("-------------------------")

    for w in sorted(ga_dict, key=ga_dict.get, reverse=True):
        print("%13s         %s" % ((w.ljust(13)), ga_dict[w]))

    total_words = str(sum(ga_dict.values()))            # Sum the number of words in the Gettysburg Address
    total = ['Total number of words', total_words]
    print ('\n')
    print (total[0], total[1])

def process_file (ga_dict,fname):
    f = open (fname + '.txt', 'w+')                                 # Creates file
    f.write("Length of the dictionary: %i" %len(ga_dict)+''+'\r\n') # Write the header and data to the file
    f.write("Word             Count"+'\r\n')
    f.write("-------------------------"+'\r\n')

    for w in sorted(ga_dict, key=ga_dict.get, reverse=True):
        f.write("%13s         %s" % ((w.ljust(13)), ga_dict[w])+'\r\n')

    total_words = str(sum(ga_dict.values()))          # Sum the number of words in the Gettysburg Address
    total = ['Total number of words ', total_words]
    f.write('\n')
    f.write(total[0]+ total[1])
    f.close()


def main():                                             # Main function to run the program
    ga_dict = dict()                                    # Create the dictionary
    Title = 'Welcome to your favorite report program!'
    print (Title)
    fname = input('Please enter the report name   \n')  # Prompt user for a filename to generate the report.
    try:                                                # Check for a valid file name
        report = open(fname + '.txt', 'w+')
    except:
        print('Report can not be open',fname)
        exit()
    fl = open('Gettysburg.txt', 'r')                     # Open file for reading

    for ga_line in fl:                                  # Process each line from the Gettysburg Address
        process_line(ga_line, ga_dict)

    process_file(ga_dict,fname)                         # Call the function to print formatted output


main()                                                  # Run the program
