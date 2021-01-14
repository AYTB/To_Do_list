from tkinter import *
from tkinter import ttk


class Box:

    def btp(self):
        self.text = Text(root, width=23, height=1)
        print("kelly")
        self.text.insert(INSERT, "Hello")
        self.text.grid(row=self.Plus_row, column=1)
        self.Plus_row += 1
        print(self.Plus_row)

    def __init__(self):
        self.Plus_row = 0
        print(self.Plus_row)
        root.title("To-Do List")
        self.add_text = ttk.Button(root, text="+",
                                   command=lambda: self.btp()).grid(row=self.Plus_row, column=6)

        style = ttk.Style()
        style.configure("TButton",
                        width=2)
        style.configure("TText",
                        font="Times 8",
                        padding=100)
        # self.add_text.grid(row=0, column=0)
        # self.text = Text(root)
        # self.text.insert(INSERT, "Hello")
        # self.text.grid(row=1, column=0)

        # hello


root = Tk()
Box()
mainloop()
