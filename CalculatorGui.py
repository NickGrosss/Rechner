from tkinter import *
from calculator.service.CalculatorService import CalculatorService


class CalculatorGui:

    def __init__(self, calculation_service):
        self.calculation_service = calculation_service
        self.operators = {
            "+": self.calculation_service.add,
            "-": self.calculation_service.sub,
            "*": self.calculation_service.mul,
            "/": self.calculation_service.div
        }
        self.first_num = 0
        self.second_num = 0
        self.operator = ""
        self.setup_Gui()

    def num1(self, number, textblock):
        self.num = textblock.get()
        textblock.delete(0, END)
        textblock.insert(0, str(self.num) + str(number))

    def saveFirst(self, operator, textblock):
        self.first_num = float(textblock.get())
        textblock.delete(0, END)
        self.operator = operator

    def clear(self, textblock):
        textblock.delete(0, END)

    def equal(self, textblock):
        try:
            self.second_num = float(textblock.get())
            textblock.delete(0, END)
            textblock.insert(0, self.operators[self.operator](self.first_num, self.second_num))
        finally:
            self.first_num = 0
            self.second_num = 0
            self.operator = ""

    def setup_Gui(self):
        root = Tk()
        root.title("Calculator")
        root.configure(background="black")
        textblock: Entry = Entry(root, width=35, borderwidth=5)
        textblock.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        a = Button(root, text=1, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(1, textblock))
        b = Button(root, text=2, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(2, textblock))
        c = Button(root, text=3, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(3, textblock))
        d = Button(root, text=4, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(4, textblock))
        e = Button(root, text=5, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(5, textblock))
        f = Button(root, text=6, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(6, textblock))
        g = Button(root, text=7, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(7, textblock))
        h = Button(root, text=8, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(8, textblock))
        i = Button(root, text=9, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(9, textblock))
        j = Button(root, text=0, bg="white", fg="black", font="Arial 28 italic", padx=40, pady=20,
                   command=lambda: self.num1(0, textblock))
        k = Button(root, padx=39, bg="white", fg="black", font="Arial 28 italic", pady=20, text="+",
                   command=lambda: self.saveFirst('+', textblock))
        l = Button(root, padx=45, bg="white", fg="black", font="Arial 28 italic", pady=20, text="-",
                   command=lambda: self.saveFirst('-', textblock))
        m = Button(root, padx=43, bg="white", fg="black", font="Arial 28 italic", pady=20, text="*",
                   command=lambda: self.saveFirst('*', textblock))
        n = Button(root, padx=34, bg="white", fg="black", font="Arial 28 italic", pady=20, text="%",
                   command=lambda: self.saveFirst("/", textblock))
        o = Button(root, padx=37, bg="white", fg="black", font="Arial 28 italic", pady=20, text="C",
                   command=lambda: self.clear(textblock))
        p = Button(root, padx=172, bg="white", fg="black", font="Arial 28 italic", pady=18, text="=",
                   command=lambda: self.equal(textblock))
        a.grid(row=1, column=0, columnspan=1)
        b.grid(row=1, column=1, columnspan=1)
        c.grid(row=1, column=2, columnspan=1)
        d.grid(row=2, column=0, columnspan=1)
        e.grid(row=2, column=1, columnspan=1)
        f.grid(row=2, column=2, columnspan=1)
        g.grid(row=3, column=0, columnspan=1)
        h.grid(row=3, column=1, columnspan=1)
        i.grid(row=3, column=2, columnspan=1)
        j.grid(row=4, column=0, columnspan=1)
        k.grid(row=4, column=1, columnspan=1)
        l.grid(row=4, column=2, columnspan=1)
        m.grid(row=5, column=0, columnspan=1)
        n.grid(row=5, column=1, columnspan=1)
        o.grid(row=5, column=2, columnspan=1)
        p.grid(row=6, column=0, columnspan=3)

        root.mainloop()
