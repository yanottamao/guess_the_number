import tkinter as tk
import sys

window = tk.Tk()


def enter():
    lbl_guess["text"] = "ENTER"
    lbl_guess = tk.Label(master=window, text="0")
    lbl_guess.grid(row=0, column=0, sticky="nsew")


def menu():
    lbl_guess["text"] = "MENU"


def clear():
    lbl_guess["text"] = "CLEAR"


def submit():
    lbl_guess["text"] = "SUBMIT"


def entnum(nume):
    num = int(nume)
    guess_text(num)


def guess_text(num):
    # # num = int(lbl_guess["text"])
    # tes = int(num)
    lbl_guess["text"] = f"{num}"


def exit():
    sys.exit()


def guess_num(num, guess):
    if num < guess:
        print("Guess higher")
    elif num > guess:
        print("Guess lower")
    else:
        print("You've got it")


def main():
    window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=75, weight=1)
    window.columnconfigure([0, 1, 2], minsize=75, weight=1)

    # lbl_guess = tk.Label(master=window, text="0")
    # lbl_guess.grid(row=0, column=0, sticky="nsew")

    btn_1 = tk.Button(master=window, text="1", command=entnum(1))
    btn_1.grid(row=1, column=0, sticky="nsew")

    btn_2 = tk.Button(master=window, text="2", command=entnum(2))
    btn_2.grid(row=1, column=1, sticky="nsew")

    btn_3 = tk.Button(master=window, text="3", command="num=3")
    btn_3.grid(row=1, column=2, sticky="nsew")

    btn_4 = tk.Button(master=window, text="4", command="num=4")
    btn_4.grid(row=2, column=0, sticky="nsew")

    btn_5 = tk.Button(master=window, text="5", command="num=5")
    btn_5.grid(row=2, column=1, sticky="nsew")

    btn_6 = tk.Button(master=window, text="6", command="num=6")
    btn_6.grid(row=2, column=2, sticky="nsew")

    btn_7 = tk.Button(master=window, text="7", command="num=7")
    btn_7.grid(row=3, column=0, sticky="nsew")

    btn_8 = tk.Button(master=window, text="8", command="num=8")
    btn_8.grid(row=3, column=1, sticky="nsew")

    btn_9 = tk.Button(master=window, text="9", command="num=9")
    btn_9.grid(row=3, column=2, sticky="nsew")

    btn_0 = tk.Button(master=window, text="0", command="num=0")
    btn_0.grid(row=4, column=1, sticky="nsew")

    btn_clr = tk.Button(master=window, text="Clear", command=clear)
    btn_clr.grid(row=4, column=0, sticky="nsew")

    btn_etr = tk.Button(master=window, text="Enter", command=enter)
    btn_etr.grid(row=4, column=2, sticky="nsew")

    btn_ext = tk.Button(master=window, text="Exit", command=exit)
    btn_ext.grid(row=5, column=2, sticky="nsew")

    btn_men = tk.Button(master=window, text="Menu", command=menu)
    btn_men.grid(row=5, column=0, sticky="nsew")

    window.mainloop()


if __name__ == "__main__":
    main()
