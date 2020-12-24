import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello World", fg="white",
                    bg="black", width=10, height=10)
button = tk.Button(text="Click me!", fg="yellow",
                   bg="blue", width=25, height=5)
label = tk.Label(text="Name")
entry = tk.Entry(bg="green", fg="yellow", width=50)
greeting.pack()
button.pack()
label.pack()
entry.pack()
window.mainloop()
