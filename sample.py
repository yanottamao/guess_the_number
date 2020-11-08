# library used
import random

# start messages
print('Guess the Random Number Game')
print('----------------------------')

# initial multi player mode
mpl = raw_input('Multi Player Mode: ')
print('mp is ' + mpl)   # mpl input checker
if mpl.lower() in ['y', 'yes']:
    print('This is Multi Player Mode')
    mplc = ('Please Enter Player Count: ')  # player count
elif mpl.lower() in ['n', 'no']:
    print('This is Single Player Mode')
else:
    print('Please Enter Yes/Y or No/N ')

# standar random 1 to 99
print('Please Enter Number Beetween 1 - 99')
rd = random.randint(1, 99)
gs = 0
gs = int(input('Enter Your Guess: '))

# simple logic comparator
while rd != gs:
    if gs < rd:
        print('Hint: Number is Higher Than Your Guess!\n')
        gs = int(input("Enter Your Guess: "))
    elif gs > rd:
        print('Hint: Number is Lower Than Your Guess!\n')
        gs = int(input("Enter Your Guess: "))
    else:
        break

# win messages
print('Congratulation You Guess It!')
print('The Mystery Number is ' + str(rd) + '.\n')
