from tkinter import messagebox
from tkinter import*

root=Tk()
root.title("Taschenrechner")
entry=Entry(root, width=35, borderwidth=5)
entry.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#Funktionen
var=""
def zahl1(a):
    var=entry.get()
    entry.delete(0, END)
    entry.insert(0,str(var)+ str(a))

def C():
    entry.delete(0, END)

def addieren():
    erstenummer= entry.get()
    global erst
    erst =float(erstenummer)
    entry.delete(0, END)
    global counter
    counter=1    
    
def subtrahieren():
    erstenummer= entry.get()
    global erst
    erst =float(erstenummer)
    entry.delete(0, END)
    global counter
    counter=2

def mult():
    erstenummer= entry.get()
    global erst
    erst =float(erstenummer)
    entry.delete(0, END)
    global counter
    counter=3

def div():
    erstenummer= entry.get()
    global erst
    erst =float(erstenummer)
    entry.delete(0, END)
    global counter
    counter=4
   
def gleich():
    try:
        if counter==1:
            zweitenummer=entry.get()
            zweite=float(zweitenummer)
            entry.delete(0, END)
            entry.insert(0, erst+float(zweitenummer))
        elif counter==2:
             zweitenummer=entry.get()
             zweite=float(zweitenummer)
             entry.delete(0, END)
             entry.insert(0, erst-float(zweitenummer))
        elif counter==3:
             zweitenummer=entry.get()
             zweite=float(zweitenummer)
             entry.delete(0, END)
             entry.insert(0, erst*float(zweitenummer))
        elif counter==4:
             zweitenummer=entry.get()
             zweite=float(zweitenummer)
             entry.delete(0, END)
             entry.insert(0, erst/float(zweitenummer))
    except:
        rechnung=entry.get()
        if "+" in rechnung:
            position=rechnung.find("+")
            zahl1=float(rechnung[0:(position)])
            zahl2=float(rechnung[(position+1):])
            rechnung=entry.get()
            entry.delete(0, END)
            entry.insert(0, zahl1+zahl2)
        elif "-" in rechnung:
            position=rechnung.find("-")
            zahl1=float(rechnung[0:(position)])
            zahl2=float(rechnung[(position+1):])
            rechnung=entry.get()
            entry.delete(0, END)
            entry.insert(0, zahl1-zahl2)
        elif "*" in rechnung:
            position=rechnung.find("*")
            zahl1=float(rechnung[0:(position)])
            zahl2=float(rechnung[(position+1):])
            rechnung=entry.get()
            entry.delete(0, END)
            entry.insert(0, zahl1*zahl2)
        elif "/" in rechnung:
            position=rechnung.find("/")
            zahl1=float(rechnung[0:(position)])
            zahl2=float(rechnung[(position+1):])
            rechnung=entry.get()
            entry.delete(0, END)
            entry.insert(0, zahl1/zahl2) 


#Gestaltung Buttons#  
var1=1
var2=2
var3=3
var4=4
var5=5
var6=6
var7=7
var8=8
var9=9
var13="%"
var15="="
var16="0"
a=Button(root, text=var1,padx=40, pady=20,command=lambda:zahl1(1))
b=Button(root, text=var2,padx=40, pady=20,command=lambda:zahl1(2))
c=Button(root, text=var3,padx=40, pady=20,command=lambda:zahl1(3))
d=Button(root, text=var4,padx=40, pady=20,command=lambda:zahl1(4))
e=Button(root, text=var5,padx=40, pady=20,command=lambda:zahl1(5))
f=Button(root, text=var6,padx=40, pady=20,command=lambda:zahl1(6))
g=Button(root, text=var7,padx=40, pady=20,command=lambda:zahl1(7))
h=Button(root, text=var8,padx=40, pady=20,command=lambda:zahl1(8))
i=Button(root, text=var9,padx=40, pady=20,command=lambda:zahl1(9))
j=Button(root, text=var16,padx=40, pady=20,command=lambda:zahl1(0))
k=Button(root,padx=39, pady=20, text="+", command =addieren)
l=Button(root,padx=42, pady=20, text="-",command=subtrahieren)
m=Button(root,padx=39, pady=20, text="*",command=mult)
n=Button(root,padx=39, pady=20, text="%",command=div)
o=Button(root,padx=39, pady=20, text="C",command=C)
p=Button(root,padx=180, pady=20, text=var15,command=gleich)
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
a["bg"]="#FFFFFF"
b["bg"]="#FFFFFF"
c["bg"]="#FFFFFF"
d["bg"]="#FFFFFF"
e["bg"]="#FFFFFF"
f["bg"]="#FFFFFF"
g["bg"]="#FFFFFF"
h["bg"]="#FFFFFF"
i["bg"]="#FFFFFF"
j["bg"]="#FFFFFF"
k["bg"]="#FFFFFF"
l["bg"]="#FFFFFF"
m["bg"]="#FFFFFF"
n["bg"]="#FFFFFF"
o["bg"]="#FFFFFF"
p["bg"]="#FFFFFF"
a["fg"]="#000000"
b["fg"]="#000000"
c["fg"]="#000000"
d["fg"]="#000000"
e["fg"]="#000000"
f["fg"]="#000000"
g["fg"]="#000000"
h["fg"]="#000000"
i["fg"]="#000000"
j["fg"]="#000000"
k["fg"]="#000000"
l["fg"]="#000000"
m["fg"]="#000000"
n["fg"]="#000000"
o["fg"]="#000000"
p["fg"]="#000000"
a["font"]="Arial 28 italic"
b["font"]="Arial 28 italic"
c["font"]="Arial 28 italic"
d["font"]="Arial 28 italic"
e["font"]="Arial 28 italic"
f["font"]="Arial 28 italic"
g["font"]="Arial 28 italic"
h["font"]="Arial 28 italic"
i["font"]="Arial 28 italic"
j["font"]="Arial 28 italic"
k["font"]="Arial 28 italic"
l["font"]="Arial 28 italic"
m["font"]="Arial 28 italic"
n["font"]="Arial 28 italic"
o["font"]="Arial 28 italic"
p["font"]="Arial 28 italic"
root.mainloop()
