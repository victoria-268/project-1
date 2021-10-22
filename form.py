from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

Label(root, text="PYTHON REGISTRATION  FORM", font= "arial 15 bold").grid(row=0,column=1)
firstname = Label(root, text=" first name")
lastname = Label(root, text="Last name")
mailid = Label(root, text="Mail Id")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")

Label(text="first name").grid(row=1, column=1, padx=90)
Label(text="lastname").grid(row=2, column=1)
Label(text="mailid").grid(row=3, column=1)
Label(text="phone").grid(row=4, column=1)
Label(text="gender").grid(row=5, column=1)

firstnamevalue = StringVar()
lastnamevalue = StringVar()
mailidvalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
checkvalue = IntVar()


nameentry= Entry(root, textvariable =firstnamevalue)
lastnameentry= Entry(root, textvariable =lastnamevalue)
mailidentry= Entry(root, textvariable =mailidvalue)
phoneentry= Entry(root, textvariable =phonevalue)
genderentry= Entry(root, textvariable =gendervalue)

nameentry.grid(row=1, column=2, pady=10)
lastnameentry.grid(row=2, column=2, pady=10)
mailidentry.grid(row=3, column=2, pady=10)
phoneentry.grid(row=4, column=2, pady=10)
genderentry.grid(row=5, column=2, pady=10)

checkbtn= Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=6, column=2)
Button(text="submit", command=getvals).grid(row=7, column=2)
Button(text="Return", command=getvals).grid(row=8,column=2)

root.mainloop()