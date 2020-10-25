import random

rd = random.randint(0, 99)
print('Guess the Random Number Game')
print('----------------------------')
print('Please Enter Number Beetween 0 - 99')
gs = int(input("Enter Your Guess: "))

while rd != gs:
    if gs < rd:
        print('Number is higher than your guess')
        gs = int(input("Enter Your Guess: "))
        print(rd)
    elif gs > rd:
        print('Number is lower than your guess')
        gs = int(input("Enter Your Guess: "))
        print(rd)
    elif gs == rd:
        print('Congratulation You Guess It')
        break
