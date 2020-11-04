#DSC 510
#Week 9
#Programming Assignment Week 9
#Author Kim Terek
#11/01/2020

#Change#:0
#Change(s) Made: First time code (no changes yet)
#Date of Change: 11/01/2020
#Author: Kim Terek
#Change Approved by: xxxx
#Date Moved to Production: xx/xx/xxxx
import string

print()
g = "C:/Users/kim.terek/PycharmProjects/pythonProject1/gettysburg.txt"
f = open(g,"r")

wds = []
di = dict()
for l in f:
    l = l.split()
    for w in l:
        wds.append(w)
    table = str.maketrans("","",string.punctuation)
    stripped = [w.translate(table) for w in wds]

# print(stripped)
    for w in stripped:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
        #print(di[w])
lenth = len(di)
import operator
name_file = input('Please title a filename for the results of this word count list: ')
new_file = "C:/Users/kim.terek/PycharmProjects/pythonProject1/"+name_file+".txt"
process_file = open(new_file, 'w')

process_file.write("This is a list of the words and their count used in the Gettysburg Address by Abraham Lincoln:")
process_file.write('\nNumber of words (ie Length of the dictionary): '+str(lenth))
process_file.write('\n{:^8}{:^8}'.format('Word','Count'))

word_freq =[]
for key,value in di.items():
    word_freq.append((value,key))
#print(word_freq)
word_freq.sort(reverse=True)

for k,v in word_freq:
    process_file.write('\n{:^8}{:^8}'.format(v,k))
process_file.close()
f.close()















