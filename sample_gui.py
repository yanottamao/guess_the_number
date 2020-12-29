import tkinter as tk
from tkinter.constants import NSEW
import random

# window = tk.Tk()
# greeting = tk.Label(text="Hello World", fg="white",
#                     bg="black", width=10, height=10)
# button = tk.Button(text="Click me!", fg="yellow",
#                    bg="blue", width=25, height=5)
# label = tk.Label(text="Name")
# entry = tk.Entry(bg="green", fg="yellow", width=50)
# greeting.pack()
# button.pack()
# label.pack()
# entry.pack()


# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"


# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"


# window = tk.Tk()

# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)

# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")

# def random_dice():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{random.randint(1, 6)}"


window = tk.Tk()

# window.rowconfigure([0, 1], minsize=50, weight=1)
# window.columnconfigure(0, minsize=50, weight=1)

# btn_roll = tk.Button(master=window, text="ROLL", command=random_dice)
# btn_roll.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=1, column=0, sticky="nsew")


def fah_cel():
    tempf = temp.get()
    value = (float(tempf) - 32) * (5/9)
    lbl_value["text"] = f"{round(value, 2)}"


window.rowconfigure([0], minsize=50, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

temp = tk.Entry(master=window, text="")
temp.grid(row=0, column=0, sticky="nsew")

btn_convert = tk.Button(master=window, text="->", command=fah_cel)
btn_convert.grid(row=0, column=1, sticky="nsew")

lbl_value = tk.Label(master=window, text="")
lbl_value.grid(row=0, column=2)

window.mainloop()
