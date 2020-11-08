# library used
import random


def main():  # start messages
    print('Guess the Random Number Game')
    print('----------------------------')
    guess()
    check(rd, gs)
    win(rd)


def mp():   # initial multi player mode
    mpl = input('Multi Player Mode: ')
    print('mp is ' + mpl)   # mpl input checker
    if mpl.lower() in ['y', 'yes']:
        print('This is Multi Player Mode')
        # mplc = ('Please Enter Player Count: ')  # player count for future
    elif mpl.lower() in ['n', 'no']:
        print('This is Single Player Mode')
    else:
        print('Please Enter Yes/Y or No/N ')


def guess():    # standar random 1 to 99
    print('Please Enter Number Beetween 1 - 99')
    global rd
    global gs
    rd = random.randint(1, 99)
    gs = 0
    gs = int(input('Enter Your Guess: '))
    return rd, gs


def check(rd, gs):  # simple logic comparator
    while rd != gs:
        if gs < rd:
            print('Hint: Number is Higher Than Your Guess!\n')
            gs = int(input("Enter Your Guess: "))
        elif gs > rd:
            print('Hint: Number is Lower Than Your Guess!\n')
            gs = int(input("Enter Your Guess: "))
        else:
            break


def win(rd):    # win messages
    print('Congratulation You Guess It!')
    print('The Mystery Number is ' + str(rd) + '.\n')
    exitcode = input('Press Any Key to Exit... ')


if __name__ == "__main__":
    main()
