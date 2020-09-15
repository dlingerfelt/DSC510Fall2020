#DSC 510#
#Week 3#
#Programming Assignment Week 3#
#Author: Brett Sutow#
#9/14/2020#
print('Hello!')
name = input('What is your company name?/n')
#Please input your company name below#
print(name)
#Please input how much feet is needed#
prompt = 'What is the length of feet fiber optic cable to be installed?/n'
feet_needed = int(input(prompt))
#Determines Discount#
if feet_needed<100:
    print('No Discount')
    Total_Cost=(int(feet_needed) * .87)
elif 250>feet_needed>99:
    print("Discount1")
    Total_Cost=(int(feet_needed)*.80)
elif 500>feet_needed>249:
    print("Discount2")
    Total_Cost=(int(feet_needed)*.70)
elif feet_needed>499:
    print("Discount3")
    Total_Cost=(int(feet_needed)*.50)
#Below are the results#
print('${:.2f}'.format(Total_Cost))
print(name,'{:.0f}ft'.format(feet_needed),'${:.2f}'.format(Total_Cost))
#Equation below will tell total installation cost#


