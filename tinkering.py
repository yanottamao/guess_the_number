import tkinter as tk

window = tk.Tk()

num = 1


def guess_text():
    guess = int(lbl_guess["text"])
    lbl_guess["text"] = f"{guess + 1}"


# def num_1():
#     num = 1
#     return num


# def num_2():
#     num = 2
#     return num


# def num_3():
#     num = 3
#     return num


# def num_4():
#     num = 4
#     return num


# def num_5():
#     num = 5
#     return num


# def num_6():
#     num = 6
#     return num


# def num_7():
#     num = 7
#     return num


# def num_8():
#     num = 8
#     return num


# def num_9():
#     num = 9
#     return num


# def num_0():
#     num = 0
#     return num


def guess_num(num, guess):
    if num < guess:
        print("Guess higher")
    elif num > guess:
        print("Guess lower")
    else:
        print("You've got it")


window.rowconfigure([0, 1, 2, 3, 4, 5], minsize=75, weight=1)
window.columnconfigure([0, 1, 2], minsize=75, weight=1)

lbl_guess = tk.Label(master=window, text="0")
lbl_guess.grid(row=0, column=0, sticky="nsew")

# btn_clr = tk.Button(master=window, text="Clear")
# btn_clr.grid(row=1, column=3, sticky="nsew")

# btn_etr = tk.Button(master=window, text="Enter")
# btn_etr.grid(row=2, rowspan=2, column=3, sticky="nsew")

btn_1 = tk.Button(master=window, text="1", command="num=1")
btn_1.grid(row=1, column=0, sticky="nsew")

btn_2 = tk.Button(master=window, text="2", command="num=1")
btn_2.grid(row=1, column=1, sticky="nsew")

btn_3 = tk.Button(master=window, text="3", command="num=1")
btn_3.grid(row=1, column=2, sticky="nsew")

btn_4 = tk.Button(master=window, text="4", command="num=1")
btn_4.grid(row=2, column=0, sticky="nsew")

btn_5 = tk.Button(master=window, text="5", command="num=1")
btn_5.grid(row=2, column=1, sticky="nsew")

btn_6 = tk.Button(master=window, text="6", command="num=1")
btn_6.grid(row=2, column=2, sticky="nsew")

btn_7 = tk.Button(master=window, text="7", command="num=1")
btn_7.grid(row=3, column=0, sticky="nsew")

btn_8 = tk.Button(master=window, text="8", command="num=1")
btn_8.grid(row=3, column=1, sticky="nsew")

btn_9 = tk.Button(master=window, text="9", command="num=1")
btn_9.grid(row=3, column=2, sticky="nsew")

btn_0 = tk.Button(master=window, text="0", command="num=1")
btn_0.grid(row=4, column=1, sticky="nsew")

btn_clr = tk.Button(master=window, text="Clear")
btn_clr.grid(row=4, column=0, sticky="nsew")

btn_etr = tk.Button(master=window, text="Enter")
btn_etr.grid(row=4, column=2, sticky="nsew")

btn_ext = tk.Button(master=window, text="Exit")
btn_ext.grid(row=5, column=2, sticky="nsew")

btn_men = tk.Button(master=window, text="Menu")
btn_men.grid(row=5, column=0, sticky="nsew")

window.mainloop()
