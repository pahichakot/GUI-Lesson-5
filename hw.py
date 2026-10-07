#Mini Adder
from tkinter import *

#Set up
root = Tk()
root.title("Mini Adder")

#Directions - Label
directions = Label(root, text = "Enter two numbers:", font = ("Times New Roman", 14, "normal"))
directions.grid(row = 1, column = 1)

#Number 1 - Entry
num1 = Entry(root, width = 15)
num1.grid(row = 2, column = 1)

#Number 2 - Entry
num2 = Entry(root, width = 15)
num2.grid(row = 3, column = 1)

#Result - Function
def sum():
    number1 = num1.get()
    number2 = num2.get()
    addition = int(number1) + int(number2)

    #Result - Label
    result = Label(root, text = "Result = " + str(addition), font = ("Times New Roman", 18, "bold"))
    result.grid(row = 5, column = 1)

#Add - Button
add = Button(root, text = "Add", bg = "light green", command = sum)
add.grid(row = 4, column = 1)

root.mainloop()