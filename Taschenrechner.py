from tkinter import messagebox
from tkinter import*
from tkinter import ttk
root=Tk()
root.title("Calculator")
entry=Entry(root, width=35, borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
root.configure(background="black")
#Funktionen
var=""
def num1(a):
    var=entry.get()
    entry.delete(0, END)
    entry.insert(0,str(var)+ str(a))
def C():
    entry.delete(0, END)
def add():
    firstnum= entry.get()
    global first
    first =float(firstnum)
    entry.delete(0, END)
    global counter
    counter=1        
def sub():
    firstnum= entry.get()
    global first
    first =float(firstnum)
    entry.delete(0, END)
    global counter
    counter=2
def mult():
    firstnum= entry.get()
    global first
    first =float(firstnum)
    entry.delete(0, END)
    global counter
    counter=3
def div():
    firstnum= entry.get()
    global first
    first =float(firstnum)
    entry.delete(0, END)
    global counter
    counter=4   
def equal():
    try:
        if counter==1:
            secondnum=entry.get()
            second=float(secondnum)
            entry.delete(0, END)
            entry.insert(0, first+float(secondnum))
        elif counter==2:
             secondnum=entry.get()
             second=float(secondnum)
             entry.delete(0, END)
             entry.insert(0, first-float(secondnum))
        elif counter==3:
             secondnum=entry.get()
             second=float(secondnum)
             entry.delete(0, END)
             entry.insert(0, first*float(secondnum))
        elif counter==4:
             secondnum=entry.get()
             second=float(secondnum)
             entry.delete(0, END)
             entry.insert(0, first/float(secondnum))
    except:
        calculation=entry.get()
        if "+" in calculation:
            position=calculation.find("+")
            num1=float(calculation[0:(position)])
            num2=float(calculation[(position+1):])
            calculation=entry.get()
            entry.delete(0, END)
            entry.insert(0, num1+num2)
        elif "-" in calculation :
            position=calculation.find("-")
            num1=float(calculation[0:(position)])
            num2=float(calculation[(position+1):])
            calculation=entry.get()
            entry.delete(0, END)
            entry.insert(0, num1-num2)
        elif "*" in calculation:
            position=calculation.find("*")
            num1=float(calculation[0:(position)])
            num2=float(calculation[(position+1):])
            calculation=entry.get()
            entry.delete(0, END)
            entry.insert(0, num1*num2)
        elif "/" in calculation:
            position=calculation.find("/")
            num1=float(calculation[0:(position)])
            num2=float(calculation[(position+1):])
            calculation=entry.get()
            entry.delete(0, END)
            entry.insert(0, num1+num2)
#Gestaltung Buttons#  
a=Button(root, text=1,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(1))
b=Button(root, text=2,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(2))
c=Button(root, text=3,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(3))
d=Button(root, text=4,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(4))
e=Button(root, text=5,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(5))
f=Button(root, text=6,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(6))
g=Button(root, text=7,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(7))
h=Button(root, text=8,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(8))
i=Button(root, text=9,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(9))
j=Button(root, text=0,bg="white",fg="black",font="Arial 28 italic",padx=40, pady=20,command=lambda:num1(0))
k=Button(root,padx=39,bg="white",fg="black",font="Arial 28 italic", pady=20, text="+", command =add)
l=Button(root,padx=45,bg="white",fg="black",font="Arial 28 italic", pady=20, text="-",command=sub)
m=Button(root,padx=43,bg="white",fg="black",font="Arial 28 italic", pady=20, text="*",command=mult)
n=Button(root,padx=34,bg="white",fg="black",font="Arial 28 italic", pady=20, text="%",command=div)
o=Button(root,padx=37,bg="white",fg="black",font="Arial 28 italic", pady=20, text="C",command=C)
p=Button(root,padx=172,bg="white",fg="black",font="Arial 28 italic", pady=18, text="=",command=equal)
a.grid(row=1, column=0,columnspan=1)
b.grid(row=1, column=1,columnspan=1)
c.grid(row=1, column=2,columnspan=1)
d.grid(row=2, column=0,columnspan=1)
e.grid(row=2, column=1,columnspan=1)
f.grid(row=2, column=2,columnspan=1)
g.grid(row=3, column=0,columnspan=1)
h.grid(row=3, column=1,columnspan=1)
i.grid(row=3, column=2,columnspan=1)
j.grid(row=4, column=0,columnspan=1)
k.grid(row=4, column=1,columnspan=1)
l.grid(row=4, column=2,columnspan=1)
m.grid(row=5, column=0,columnspan=1)
n.grid(row=5, column=1,columnspan=1)
o.grid(row=5, column=2,columnspan=1)
p.grid(row=6,column=0,columnspan=3)

root.mainloop()