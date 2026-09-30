#Quiz game
from tkinter import *
from tkinter import messagebox

#Setup
root = Tk()
root.config(background = "light blue")
root.geometry("600x600")
root.title("Quiz Game")

#Quiz Game - Label
quiz_game = Label(root, text = "Quiz Game !", bg = "pink")
quiz_game.pack(pady = 10)

#Question - Label
q1 = Label(root, text = "What is the slope intercept formula?", bg = "light green", fg = "purple", font = ("Times", 24, "bold"))
q1.pack(pady = 20)

#Answer boxes - Buttons
a1 = Button(root, text = "(y2 - y1) / (x2 - x1)", bg = "white", fg = "red")
a1.pack(side = RIGHT, padx = 20)

a2 = Button(root, text = "(a*a) + (b*b) = (c*c)", bg = "white", fg = "red")
a2.pack(side = LEFT, padx = 20)

a3 = Button(root, text = "To Be Entered", bg = "white", fg = "red")
a3.pack(side = RIGHT, padx = 20)

a4 = Button(root, text = "y = mx + b", bg = "white", fg = "red")
a4.pack(side = LEFT, padx = 20)

root.mainloop()