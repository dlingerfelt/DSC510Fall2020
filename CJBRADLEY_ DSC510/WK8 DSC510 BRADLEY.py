#DSC 510                           # Change Log
#Week 8                           # No changes
#Author Carla J Bradley
#10/25/2020

# function to add the word to the dictionary and count it
def add_word(wrd, ga_dict):
#   for each word in the list, check if the word is in the dictionary, add the word and add 1 if it exists
    for w in wrd:
        if w not in ga_dict:
            ga_dict[w] = 1
        else:
            ga_dict[w] += 1


# function to process each line in the Gettysburg Address and remove the punctuation
def process_line(ga_line, ga_dict) :

    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    punctuation_to_remove = ga_line
    no_punctuation = ""
    for char in punctuation_to_remove:
        if char not in punctuation:
            no_punctuation = no_punctuation + char
            no_punctuation = no_punctuation.lower()
    no_punctuation = no_punctuation.split()

#   call the add_word function to add the word to the dictionary and count the words
    add_word(no_punctuation, ga_dict)


# function to print and format the dictionary and word count
def pretty_print(ga_dict):
    print("Length of the dictionary: %i" %len(ga_dict))  # Print length of dictionary
    print("Word             Count")
    print("-------------------------")

    for w in sorted(ga_dict, key=ga_dict.get, reverse=True):
        print("%13s         %s" % ((w.ljust(13)), ga_dict[w]))

#   sum the number of words in the Gettysburg Address
    total_words = str(sum(ga_dict.values()))
    total = ['Total number of words', total_words]
    print ('\n')
    print (total[0], total[1])


# main function to run the program
def main():
#   create the dictionary
    ga_dict = dict()

#   open file for reading
    fl = open('Gettysburg.txt', 'r')

#   process each line from the Gettysburg Address
    for ga_line in fl:
        process_line(ga_line, ga_dict)

#   call the function to print formatted output
    pretty_print(ga_dict)


# Run the program
main()
