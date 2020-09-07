# DSC_510 Assignment 1.1
# Hello World Assignment
# Python 3.8
# Author : Danny Angel

greeting = 'Hello cruel world'                          # This section is defining phrases to be used later
initial_farewell = 'This is the end of my program'
final_farewell = 'Goodbye cruel world'
undead_cpu = 'I am not really dead or alive. I am a computer program.'
print('Hello there.')                                                    # Program says hi
print('What do people call you?')                                        # Program asks your name
name = input()                                                           # Definition and prompt for answer
print('That is a funny name ' + name)                                    # Program teases you
print('Are you alive or dead ' + name + '?')                             # Program asks another question
status = input()                                 # Hopefully, you're alive but the program asks anyway
print(status + ' huh. Me too, in a sense')                               # Program acts relatable
if status == 'dead' or status == 'Dead' or status == 'DEAD':             # Dead branch (includes different capitlizations)
    print('Well, technically if you are typing you are not dead')
    print(undead_cpu)
elif status == 'alive' or status == 'Alive' or status == 'ALIVE':        # Living branch
    print(undead_cpu)
else:                                                                    # Zombie branch
    print('So you are not dead and you are not alive, huh?')
    print(undead_cpu)
print('I do not meet the classical definition of alive but I can do things if I am programmed to, like this:')
print(greeting)                                                          # Emo program says hi
print(initial_farewell)
print(final_farewell)                                                    # Emo program says bye
