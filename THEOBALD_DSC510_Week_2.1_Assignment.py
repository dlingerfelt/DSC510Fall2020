#DSC510
#Week 2
#Programming Assignment Week 2
#Author Ammy Theobald
#09/13/2020

#Get Name, Company and Cable Length Required
name = input('What is your name?\n')
print('Hello', name, '! Welcome to the Fiber Optic Cost Calculator!')
company = input('Please enter your company name: ')
length = float(input('Please enter how many feet of Fiber Optic Cable you require:'))

#compute the cost of fiber optic cable
unit_cost = .87
cost = (length * unit_cost)

#print receipt for customer
print(name, 'Here are your results:\n')

print('*************** Estimate for', name, 'with', company, '***************')
print('        Cable Installation Requested (in feet):', length,)
print('        Cable Unit Cost: $.87')
print('        Cable Total Cost: $ %.2f' % cost)
print('*************** THANK YOU FOR YOUR BUSINESS!!! ***************')
