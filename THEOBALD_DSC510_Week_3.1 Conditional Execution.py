#DSC510
#Week 3
#Programming Assignment Week 3
#Author Ammy Theobald
#09/20/2020

#Get Name, Company and Cable Length Required
name = input('What is your name?\n')
print('Hello',name, '! Welcome to the Fiber Optic Cost Calculator!')
company = input('Please enter your company name: ')
length = float(input('Please enter how many feet of Fiber Optic Cable you require:'))

#compute the cost of fiber optic cable and bulk discount
if length <=100:
    unit_cost = .87
else:
    if length >100 and length<=250:
        unit_cost = .80
    else:
        if length >250 and length<=500:
            unit_cost = .70
        else:
            if length >500:
                unit_cost = .50

cost = (length * unit_cost)


#print receipt for customer
print(name, 'Here are your results:\n')

print('*************** Estimate for', name, 'with', company, '***************')
print('        Cable Installation Requested (in feet):', length,)
print('        Cable Unit Cost: $ %.2f' % unit_cost)
print('        Cable Total Cost: $ %.2f' % cost)
print('*************** THANK YOU FOR YOUR BUSINESS!!! ***************')
