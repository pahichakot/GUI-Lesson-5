#Calendar App
from tkinter import *
import calendar

#Setup
root = Tk()
root.title("Calendar App")

#Calendar Display - Function
def display_calendar():
    new_root = Tk()
    new_root.title("Calendar")
    new_root.config(background = "light blue")
    new_root.geometry("600x600")
    
    year = int(year_entry.get())
    content = calendar.calendar(year)

    cal_year = Label(new_root, text = content, font = ("Consolas", 10, "bold"))
    cal_year.grid(row = 5, column = 0, padx = 20)

    new_root.mainloop()


#Calender - Label
calendar_label = Label(root, text = "Calendar", bg = "grey", font = ("times", 28, "bold"))
calendar_label.grid(row = 1, column = 1)

#Enter Year - Label
enter_year = Label(root, text = "Enter Year", bg = "light green", fg = "purple", font = ("times", 12, "normal"))
enter_year.grid(row = 2, column = 1)

#Entry
year_entry = Entry(root, width = 15)
year_entry.grid(row = 3, column = 1)

#Show Calendar - Button
show_calendar = Button(root, text = "Show Calendar", bg = "red", command = display_calendar)
show_calendar.grid(row = 4, column = 1)

#Exit - Button
exit_button = Button(root, text = "Exit", bg = "red", command = root.destroy)
exit_button.grid(row = 6, column = 1)

root.mainloop()