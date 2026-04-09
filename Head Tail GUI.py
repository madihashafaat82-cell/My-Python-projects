# Library importing
from tkinter import *
import random

# System setting
root = Tk()
root.title('Tossing Game')
root.geometry('200x250')
root.configure(bg='Red')

#Selection
comp = 'Tail'
you = 'Head'

# Choices
choices = ['head','tail']

def play(you):
  comp = random.choice(choices)
  you = random.choice(choices)
  

# Button style
btn_style = {
    "width": 15,
    "bg": "yellow",
    "fg": "black",
    "bd": 4,
    "relief": "solid",
    "highlightbackground": "darkblue"
}

Button(root, text="Head", command=lambda: play("head"), **btn_style).pack(pady=10)
Button(root, text="Tail", command=lambda: play("tail"), **btn_style).pack(pady=10)

label = Label(
    root,
    text="",
    font=("Arial", 14),
    bg="red",
    fg="yellow",
    bd=4,
    relief="solid",
    highlightbackground="darkblue",
    width=25,
    height=4
)
label.pack(pady=20)

root.mainloop()