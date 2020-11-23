# DSC 510
# Week 8
# Programming Assignment Week 9
# Author Riley Fencl
# 10/25/2020

# Change Control Log
# Change(s) Made: Replaced all code from assignment 8 with proper functioning code for assignment 9.
# Changed functionality to direct output to a text file with a user generated name. Lines: 51 - 61 added.
# Data of Change: 10/25/2020
# Author: Riley Fencl

import string
import os
import sys


def process_line(line, word_count_dict):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)


def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


def pretty_print(word_count_dict):
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    print('{:11s}{:11s}'.format('Word', 'Count'))
    print(' ' * 21)
    for val, key in value_key_list:
        print('{:12s} {:<3d}'.format(key, val))


def main():
    word_count_dict = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count_dict)
    file_name = input("Please specify a name for your file.\n"
                      "Your file name should contain a .txt at the end.\n"
                      "Example: New Text.txt\n")
    process_file(word_count_dict, file_name)


def process_file(word_count_dict, file_name):
    with open(file_name, 'w') as f:
        sys.stdout = f
        print('Length of the dictionary:', len(word_count_dict))
        pretty_print(word_count_dict)


if __name__ == "__main__":
    main()
