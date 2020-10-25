import random

rd = random.randint(1, 99)
gs = 0

while rd != gs:
    print('Guess the Random Number Game')
    print('----------------------------')
    print('Please Enter Number Beetween 0 - 99')
    print(rd)
    gs = int(input("Enter Your Guess: "))

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
