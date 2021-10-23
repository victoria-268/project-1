from tkinter import *
from tkcalendar import Calendar

root = Tk()

root.geometry("400x400")

cal = Calendar(root, selectmode='day',
               year=2021, month=10,
               day=23)

cal.pack(pady=20)


def grad_date():
    date.config(text="Selected Date is: " + cal.get_date())

Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

date = Label(root, text="")
date.pack(pady=20)

root.mainloop()