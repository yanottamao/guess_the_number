import tkinter as tk
from tkinter.constants import NSEW
import random
from tkinter.filedialog import askopenfilename, asksaveasfilename
from typing import Text

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


# window = tk.Tk()

# window.rowconfigure([0, 1], minsize=50, weight=1)
# window.columnconfigure(0, minsize=50, weight=1)

# btn_roll = tk.Button(master=window, text="ROLL", command=random_dice)
# btn_roll.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=1, column=0, sticky="nsew")


# def fah_cel():
#     tempf = temp.get()
#     value = (float(tempf) - 32) * (5/9)
#     lbl_value["text"] = f"{round(value, 2)}"


# window.rowconfigure([0], minsize=50, weight=1)
# window.columnconfigure([0, 1], minsize=50, weight=1)

# temp = tk.Entry(master=window, text="")
# temp.grid(row=0, column=0, sticky="nsew")

# btn_convert = tk.Button(master=window, text="->", command=fah_cel)
# btn_convert.grid(row=0, column=1, sticky="nsew")

# lbl_value = tk.Label(master=window, text="")
# lbl_value.grid(row=0, column=2)

# window.mainloop()

# def open_file():
#     """Open a file for editing."""
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete(1.0, tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")


# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension="txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get(1.0, tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")


# window = tk.Tk()
# window.title("Simple Text Editor")
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)

# txt_edit = tk.Text(window)
# fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
# btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")

# window.mainloop()

# window = tk.Tk()

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)

#     for j in range(0, 3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )

#         frame.grid(row=i, column=j, padx=5, pady=5)

#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)

# window.mainloop()

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0)

label2 = tk.Label(text="B")
label2.grid(row=1, column=0)

window.mainloop()
