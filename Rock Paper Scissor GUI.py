from tkinter import *
import random

# System
root = Tk()
root.title('RPS Arena')
root.geometry('300x350')
root.configure(bg="red")   # Background color

# Choices
choices = ['Rock', 'Paper', 'Scissors']

# Function
def play(user):
    computer = random.choice(choices)

    if user == computer:
        result = 'Draw'
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissors' and computer == 'Paper'):
        result = 'You Win 😊'
    else:
        result = 'You Lose 😞'

    label.config(
        text="You: " + user + "\nComputer: " + computer + "\n" + result
    )

# Buttons
btn_style = {
    "width": 15,
    "bg": "yellow",
    "fg": "black",
    "bd": 4,
    "relief": "solid",
    "highlightbackground": "darkblue"
}

Button(root, text="Rock", command=lambda: play("Rock"), **btn_style).pack(pady=10)
Button(root, text="Paper", command=lambda: play("Paper"), **btn_style).pack(pady=10)
Button(root, text="Scissors", command=lambda: play("Scissors"), **btn_style).pack(pady=10)

# Result Label
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