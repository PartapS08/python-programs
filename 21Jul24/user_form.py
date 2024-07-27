from tkinter import *
# import tkinter

root = Tk()
root.geometry("500x500")

def form1():
    if chk.get() == 0:
        Error1=Label(root,text="Please Accept the Term")
        Error1.pack(side="top")
    else:
        DisNote1=Label(root,text="Entered Details are:")
        DisNote1.place(x=240,y=380)
        Output1=Label(root,text="name:"+name.get())
        Output1.place(x=240,y=400)
        Output2=Label(root,text=address.get())
        Output2.place(x=240,y=420)
        Output3=Label(root,text=gender.get())
        Output3.place(x=240,y=440)

Labl1=Label(root,text="Enter your Real Name")
Labl1.place(x=20,y=40)

Labl1=Label(root,text="Enter a Valid Address")
Labl1.place(x=20,y=70)

name=StringVar()
Col1=Entry(root,textvariable=name)
Col1.place(x=200,y=40)

address=StringVar()
Col2=Entry(root,textvariable=address)
Col2.place(x=200,y=70)

gender=StringVar()
Rad1=Radiobutton(root,variable=gender,text="Male",value="Male")
Rad1.place(x=20,y=100)
Rad2=Radiobutton(root,variable=gender,text="Female",value="Female")
Rad2.place(x=20,y=120)
gender.set('Male')

chk=IntVar()
Chk1=Checkbutton(root,variable=chk,onvalue=1,offvalue=0,text="Accept the Terms")
Chk1.place(x=20,y=150)

Btn1=Button(root,text="Submit",command=form1)
Btn1.place(x=250,y=250)

root.mainloop()
