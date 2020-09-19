#DSC 510
#Week 2h
#Programming Assignment Week 2
#Author Carla J Bradley
#09/11/2020


FootCost = float (0.87)
#Display a welcome message for your user.
print ('      Welcome   ')

#Retrieve the company name from the user.
CompanyName = input('Please enter name of company\n')

#Retrieve the number of feet of fiber optic cable to be installed from the user.
Measurement = float(input('Please enter length of cable in feet\n'))

#Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87
Cost = (Measurement*FootCost)

#Print receipt for the user including the company name, number of feet of fiber to be installed,
# the calculated cost, and total cost in a legible format
print ('Thank you! here is your receipt!')
print ('              ')
receipt = '   Receipt  \n'+'Blue Sea Service\n'+'789-789-7895\n'+'899 Street Road\n'+'Philadelphia\n'+'Pennsylvania \n'+ '          \n'\
          + 'CompanyName: '+ CompanyName +'\n' + 'Length: '+ str (Measurement) + ' ft'+'\n' + 'Cost ' + '$'+ str (Cost)
print (receipt)


