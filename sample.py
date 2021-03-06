# library used
import random


def mpmain():   # initial multi player mode
    mpl = input('Multi Player Mode (Y/N): ')
    print('mp is ' + mpl)   # mpl input checker
    if mpl.lower() in ['y', 'yes']:
        print('This is Multi Player Mode')
        multipl()
    elif mpl.lower() in ['n', 'no']:
        print('This is Single Player Mode')
        guess()
        check(rd, gs, pr)
        win(rd, turn)
    else:
        print('Please Enter Yes/Y or No/N ')
        mpmain()


def multipl():
    print('This is Multi Player Mode')
    mplc = int(input('Please Enter Player Count 2 - 4: '))
    print('Player Count: ' + str(mplc))
    for i in range(mplc):
        i += 1
        print('Player ' + str(i))
        guess()
        check(rd, gs, pr)
        win(rd, turn)


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
    print('\nTurn 1')
    gs = int(input('Enter Your Guess: '))
    pr = gs
    return rd, gs, pr


def check(rd, gs, pr):  # simple logic comparator
    global turn
    turn = 1
    while rd != gs:
        if gs < rd:
            turn += 1
            print('Hint: Number is Higher Than Your Guess! (number > ' + str(pr) + ')\n')
            print('Turn ' + str(turn))
            gs = int(input("Enter Your Guess: "))
            pr = gs
        elif gs > rd:
            turn += 1
            print('Hint: Number is Lower Than Your Guess! (number < ' + str(pr) + ')\n')
            print('Turn ' + str(turn))
            gs = int(input("Enter Your Guess: "))
            pr = gs
        else:
            return turn


def win(rd, turn):    # win messages
    print('Congratulation You Guess It!')
    print('The Mystery Number is ' + str(rd) + '.')
    print('You Guess It in ' + str(turn) + ' Turn.\n')
    input('Press Any Key to Exit... \n')


def main():  # start messages
    print('Guess the Random Number Game')
    print('----------------------------')
    mpmain()


if __name__ == "__main__":
    main()
