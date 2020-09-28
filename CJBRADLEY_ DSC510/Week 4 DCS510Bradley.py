#DSC 510
#Week 4
#Programming Assignment Week 3
#Author Carla J Bradley
#09/23/2020

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
Measurement = float(input('Please enter numeric character value for length of cable \n'))

#Retrieve discount of fiber optic cableiNTEL
if Measurement >500 : fibercost=FootCostd
elif Measurement >250 : fibercost=FootCostc
elif Measurement >100 : fibercost=FootCostb
elif Measurement <=99 : fibercost=FootCost

#Function reflect cost of calculation
def calcfiber (fiberlen, cost):
#Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet
    Finalcost = (fiberlen*cost)
    return Finalcost

#Call function and calculate final cost
total = calcfiber (Measurement,fibercost)

#	Display a welcome message for your program.
print ('Thank you! here is your receipt!')
print ('              ')
receipt = '   Receipt  \n'+'Blue Sea Service\n'+'789-789-7895\n'+'899 Street Road\n'+'Philadelphia\n'+'Pennsylvania \n'+ '          \n'\
          + 'CompanyName: '+ CompanyName +'\n' + 'Length: '+ str (Measurement) + ' ft'+'\n' + 'Cost ' + '$'+ str (total)
print (receipt)


