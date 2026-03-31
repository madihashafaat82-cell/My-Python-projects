#Imports
from tkinter import * 
import random

#System
root = Tk()
root.title('RPS Arena')
root.geometry('200x250')

#Choices
choices = ['Rock','Paper','Scissor']

#Conditions
def play(user):
     computer = random.choice(choices)
     if user == computer:
          result =  'Draw'
     elif(user == 'Rock' and computer == 'Scissor') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissor' and computer == 'Paper'):
         result = 'You Win😊'     
     else:
          result = 'You Lose😞'

     label.config(text="You: " + user + "\nComputer: " + computer + "\n" + result)

# Buttons
Button(root, text="Rock",  width=15, command=lambda: play("Rock")).pack(pady=10)
Button(root, text="Paper"  , width=15, command=lambda: play("Paper")).pack(pady=10)  
Button(root, text="Scissors" , width=15, command=lambda: play("Scissors")).pack(pady=10)

#Results          
label = Label(root, text="",font=("Arial", 25))
label.pack(pady=25)

root.mainloop()