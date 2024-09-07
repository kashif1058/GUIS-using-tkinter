#GUIS
import tkinter 
from tkinter import *


window = tkinter.Tk()
window.title("My first GUI program!")
window.minsize(width=500, height=300)


# Creating a label
my_label = tkinter.Label(text = "I am a label", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")
my_label.grid(column =0, row= 0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    print("Button was clicked")

button = Button(text = "click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)



# entry component
input = Entry(width=10)
# input.pack()
print(input.get())
input.grid(column=2, row=1)


# window.mainloop()