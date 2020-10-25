import random

print('Guess the Random Number Game')
print('----------------------------')
print('Please Enter Number Beetween 0 - 99')
rd = random.randint(1, 99)
gs = 0
gs = int(input('Enter Your Guess: '))

while rd != gs:
    if gs < rd:
        print('Hint: Number is Higher Than Your Guess!\n')
        gs = int(input("Enter Your Guess: "))
    elif gs > rd:
        print('Hint: Number is Lower Than Your Guess!\n')
        gs = int(input("Enter Your Guess: "))
    else:
        break

print('Congratulation You Guess It!')
print('The Mystery Number is ' + str(rd) + '.\n')
