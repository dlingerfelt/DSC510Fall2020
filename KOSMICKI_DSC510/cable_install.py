#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Sherry Kosmicki
#09/7/2020

#factor used to calculate cost
cablefactor = .87

print('Welcome to my invoice generator!')

#Prompt user for their name
username = input('Please enter your name\n')

#Prompt user for company name
usercompany = input ('Enter your company name\n')

#Prompt user for number of feet of cable to be installed to calculate cost
userfeet = input('How many feet of cable will be installed?\n')

#Calculate userfeet prompt times cablefactor variable
cost = (int(userfeet) * cablefactor)

#Generate Invoice
print('')
print('Please print invoice below - due in 30 days')
print('==================================================')
print('INVOICE')
print('TO:',username)
print('COMPANY:',usercompany)
print('')
print('Amount of cable installed =',userfeet)
print('Cost per feet =',cablefactor)
print('Total Due= $',round(cost,2))
print('==================================================')
