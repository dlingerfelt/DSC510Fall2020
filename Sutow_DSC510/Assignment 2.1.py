#DSC 510#
#Week 2#
#Programming Assignment Week 2#
#Author: Brett Sutow#
#9/07/2020#
print('Hello!')
name = input('What is your company name?/n')
#Please input your company name below#
print(name)
#Please input how much feet is needed#
prompt = 'What is the length of feet fiber optic cable to be installed?/n'
feet_needed = input(prompt)
int(feet_needed)
print(feet_needed)
#Equation below will tell total installation cost#
Total_Cost = (int(feet_needed) * .87)
print(Total_Cost)

print(name,feet_needed,Total_Cost)


