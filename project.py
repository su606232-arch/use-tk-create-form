from tkinter import *
root = Tk()
root.geometry ("500x300")

def getvals():
    print("Accepted")



#heading

Label (root, text="collage program   ", font="arial 15 bold").grid(row=0 ,column=3)
name = Label ( root , text="Name")
phone = Label ( root , text="phone")
gender= Label ( root , text="gender")
emergency= Label ( root , text="emergency")
paymentmode = Label ( root , text="payment mode")

name.grid(row=1, column=2)
phone .grid(row=2, column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)
#varible for storing data 
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar
#creating entry field
nameEntry = Entry(root ,textvariable=namevalue)
phoneEntry = Entry(root, textvariable=phonevalue)
genderEntry = Entry(root, textvariable=gendervalue)
emergencyEntry = Entry(root, textvariable=emergencyvalue)
paymentmodeEntry = Entry(root, textvariable=paymentmodevalue)
#packing entry filed
nameEntry .grid(row=1, column=3)
phoneEntry .grid(row=2, column=3)
genderEntry .grid(row=3, column=3)
emergencyEntry .grid(row=4, column=3)
paymentmodeEntry .grid(row=5, column=3)

#creating check box
Checkbutton = Checkbutton(text="rember me ?", variable= checkvalue)
Checkbutton.grid(row=6, column=3)

#sumbit buttom

Button( text="submit" , command=getvals).grid(row=7, column=3)


root.mainloop()