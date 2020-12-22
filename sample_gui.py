import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello World", fg="white",
                    bg="black", width=10, height=10)
button = tk.Button(text="Click me!", fg="yellow",
                   bg="blue", width=25, height=5)
greeting.pack()
button.pack()
window.mainloop()
