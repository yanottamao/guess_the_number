import random

print('Guess the Random Number Game')
print('----------------------------')
print('Please Enter Number Beetween 0 - 99')
rd = random.randint(1, 99)
gs = 0
gs = int(input("Enter Your Guess 1: "))
print(rd)

while rd != gs:
    if gs < rd:
        print('Hint: Number is higher than your guess!\n')
        gs = int(input("Enter Your Guess 2: "))
    elif gs > rd:
        print('Hint: Number is lower than your guess\n')
        gs = int(input("Enter Your Guess 3: "))
    else:
        break

print('Congratulation You Guess It\n')
