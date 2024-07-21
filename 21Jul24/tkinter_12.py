from queue import Full
from tkinter import *
from tkinter import ttk

root=Tk()
root.geometry("500x500")
#root.resizable(False,False)
style = ttk.Style()
style.theme_use('classic')
#l=Label(root,text=" ")
#l.pack(side=LEFT)
#l.grid(row=0,column=0)

e=Entry(root)
e.place(x=20,y=20)
#l1=Label(root,text="Hello")
#l1.grid(row=0,column=4)

#l2=Label(root,text="Holiday",font=("",40,"bold"))

#l2.place(x=50,y=100)

def newb():
    if gender.get() == "":
        ll = Label(root, text="Please enter some text", fg="red")
        ll.pack(side="top")
    else:
        l = Label(root, text=gender.get())
        l.pack(side="top")

gender=StringVar()
m=Radiobutton(root,variable=gender,text="Male",value="Male")
m.place(x=50,y=100)
n=Radiobutton(root,variable=gender,text="FeMale",value="Female")
n.place(x=50,y=120)
c=Checkbutton
gender.set('Female')

    
def newa():
    root.quit()
        
b=Button(root,text="ButtonNo1",font=("",20,"bold"),command=newb)
b.place(x=100,y=450)

a=Button(root,text="Close",font=("",20,"bold"),command=newa)
a.place(x=300,y=450)


root.mainloop()

