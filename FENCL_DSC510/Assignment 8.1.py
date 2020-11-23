# DSC 510
# Week 8
# Programming Assignment Week 8
# Author Riley Fencl
# 10/25/2020


def main():
    gba_file = open("Gettysburg.txt", "r")
    Process_line()
    gba_file.close()


def Process_line():
    word_dictionary = dict()
    text_file = 'Gettysburg.txt'
    import string
    with open(text_file) as tf:
        for line in tf:
            line = line.rstrip()
            line = line.translate(line.maketrans('', '', string.punctuation))
            add_word(line.split(), word_dictionary)
    pretty_print(word_dictionary)


def add_word(words, word_dictionary):
    for word in words:
        word = word.lower()
        if word != '':
            if word in word_dictionary:
                word_dictionary[word.lower()] += 1
            else:
                word_dictionary[word.lower()] = 1


def pretty_print(word_dictionary):
    print("Length of the Dictionary: ", sum(word_dictionary.values()))
    print("{}             {}".format('Word', 'Count'))
    print("______________________________")
    for key, value in sorted(word_dictionary.items(), key=lambda p: p[1], reverse=True):
        print('{:18} {}'.format(key, value))


main()
