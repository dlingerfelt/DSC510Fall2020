# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Sherry Kosmicki
# 09/17/2020

# factor used to calculate cost
cablefactor1 = .87  # factor for less than 100 feet installed
cablefactor2 = .80  # factor for 100-250 feet installed
cablefactor3 = .70  # factor for 251-500 feet installed
cablefactor4 = .50  # factor for greater than 501 feet installed

# bulkrate variable
bulkrate=''

print('Welcome to my cable installation cost generator!')

# Prompt user for company name
usercompany = input('Enter your Company Name:\n')

# Prompt user for number of feet of cable to be installed to calculate cost
userfeet = input('How many feet of cable will be installed?\n')

if int(userfeet) <= 100:
    cost = int(userfeet) * cablefactor1
elif 100 <= int(userfeet) <= 250:
    cost = int(userfeet) * cablefactor2
elif 251 <= int(userfeet) <= 500:
    cost = int(userfeet) * cablefactor3
else:
    cost = int(userfeet) * cablefactor4

if int(userfeet) <= 100:
    bulkrate = cablefactor1
elif 100 <= int(userfeet) <= 250:
    bulkrate = cablefactor2
elif 251 <= int(userfeet) <= 500:
    bulkrate = cablefactor3
else:
    bulkrate = cablefactor4

print(usercompany,'bulk rate is $%.2f' % bulkrate)
print(usercompany,'total cost is $%.2f' % cost)
