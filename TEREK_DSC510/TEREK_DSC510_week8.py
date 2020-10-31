#DSC 510
#Week 8
#Programming Assignment Week 8
#Author Kim Terek
#10/25/2020

#Change#:0
#Change(s) Made: First time code (no changes yet)
#Date of Change: 10/25/2020
#Author: Kim Terek
#Change Approved by: xxxx
#Date Moved to Production: xx/xx/xxxx
import string

print()
f = "C:/Users/kim.terek/PycharmProjects/pythonProject1/gettysburg.txt"
f = open(f,"r")

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
        # print(di[w])
print('Length of the dictionary: ',len(di))
print()
print('{:^8}{:^8}'.format('Word','Count'))
for k,v in di.items():
    print('{:^8}{:^8}'.format(k,v))







print("")





