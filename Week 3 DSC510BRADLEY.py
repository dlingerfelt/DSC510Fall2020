#DSC 510
#Week 3
#Programming Assignment Week 3
#Author Carla J Bradley
#09/16/2020

#Program will calculate the cost of fiber optic cable installation by multiplying the number
# of feet needed by bulk discount
FootCost = float (0.87)
FootCostb = float (0.80)
FootCostc = float (0.70)
FootCostd = float (0.50)

#Display a welcome message for your user.
print ('      Welcome   ')

#Retrieve the company name from the user
CompanyName = input('Please enter name of company\n')

#Retrieve the number of feet of fiber optic cable to be installed from the user.
Measurement = float(input('Please enter length of cable in feet\n'))
if Measurement >500 : cableprice=FootCostd
elif Measurement >250 : cableprice=FootCostc
elif Measurement >100 : cableprice=FootCostb
elif Measurement <=99 : cableprice=FootCost

#Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet

Cost = (Measurement*cableprice)
#	Display a welcome message for your program.
print ('Thank you! here is your receipt!')
print ('              ')
receipt = '   Receipt  \n'+'Blue Sea Service\n'+'789-789-7895\n'+'899 Street Road\n'+'Philadelphia\n'+'Pennsylvania \n'+ '          \n'\
          + 'CompanyName: '+ CompanyName +'\n' + 'Length: '+ str (Measurement) + ' ft'+'\n' + 'Cost ' + '$'+ str (Cost)
print (receipt)


