# library used
import random


def main():  # start messages
    print('Guess the Random Number Game')
    print('----------------------------')
    guess()
    check(rd, gs, pr)
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
    print('Guessing Range Input')
    # first number range
    first = int(input('Please Enter Initial Number Range: '))
    # max number range
    last = int(input('Please Enter Maximum Number Range: '))
    print('Please Enter Number Beetween ' + str(first) + ' - ' + str(last))
    global rd
    global gs
    global pr
    rd = random.randint(first, last)
    gs = 0
    gs = int(input('Enter Your Guess: '))
    pr = gs
    return rd, gs, pr


def check(rd, gs, pr):  # simple logic comparator
    while rd != gs:
        if gs < rd:
            print('Hint: Number is Higher Than Your Guess! (' + str(pr) + ')\n')
            gs = int(input("Enter Your Guess: "))
            pr = gs
        elif gs > rd:
            print('Hint: Number is Lower Than Your Guess! (' + str(pr) + ')\n')
            gs = int(input("Enter Your Guess: "))
            pr = gs
        else:
            break


def win(rd):    # win messages
    print('Congratulation You Guess It!')
    print('The Mystery Number is ' + str(rd) + '.\n')
    input('Press Any Key to Exit... ')


if __name__ == "__main__":
    main()
