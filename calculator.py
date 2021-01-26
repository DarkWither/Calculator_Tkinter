#############################
# Számológép                #
# Version: 2.0              #
# Made by: Attila Ladányi   #
# 2020.01.26                #
#############################

from tkinter import *
import re
import math

class App:

    def __init__(self, root):
        self.main_menu(root)

    def main_menu(self, root):

        #Framek

        topframe = Frame(root, height=100, width=300)
        botframe = Frame(root, height=400, width=300)
        nframe1 = Frame(botframe, bg='blue', height=320, width=75)
        nframe2 = Frame(botframe, bg='red', height=320, width=75)
        nframe3 = Frame(botframe, bg='orange', height=320, width=75)
        mframe = Frame(botframe, bg='green', height=320, width=75)
        eframe = Frame(root, bg='yellow', height=80, width=300)

        #Számok 1. oszlop

        nbutton_square = Button(nframe1, text="^", height=3, width = 6, font = ('Arial', 15), command = lambda: self.muveletek("^"))
        nbutton7 = Button(nframe1, text="7", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(7))
        nbutton4 = Button(nframe1, text="4", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(4))
        nbutton1 = Button(nframe1, text="1", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(1))

        # Számok 2. Oszlop

        nbutton_square_root = Button(nframe2, text="GY", height=3, width = 6, font = ('Arial', 15), command = lambda: self.muveletek("|"))
        nbutton8 = Button(nframe2, text="8", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(8))
        nbutton5 = Button(nframe2, text="5", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(5))
        nbutton2 = Button(nframe2, text="2", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(2))

        # Számok 3. Oszlop
        nbutton_delete = Button(nframe3, text="<-", height=3, width = 6, font = ('Arial', 15), command = lambda: self.delete())
        nbutton9 = Button(nframe3, text="9", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(9))
        nbutton6 = Button(nframe3, text="6", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(6))
        nbutton3 = Button(nframe3, text="3", height=3, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(3))

        # Alsó sor (nulla és az egyenlő)

        ebutton0 = Button(eframe, text="0", width = 13, height = 3, font = ('Arial', 15), command = lambda: self.szambekeres(0))
        ebutton_equals = Button(eframe, text="=", width = 13, height = 3, font = ('Arial', 15), command = lambda: self.equals())

        # mframe

        button_plus = Button(mframe, text="+", width = 13, height = 3, font = ('Arial', 15), command = lambda: self.muveletek("+"))
        button_minus = Button(mframe, text="-", width = 13, height = 3, font = ('Arial', 15), command = lambda: self.muveletek("-"))
        button_times = Button(mframe, text="*", width = 13, height = 3, font = ('Arial', 15), command = lambda: self.muveletek("*"))
        button_divide = Button(mframe, text="/", width = 13, height = 3, font = ('Arial', 15), command = lambda: self.muveletek("/"))

        # Számok szövegként

        self.t = ""

        self.label = Label(topframe, text = self.t, font = ('Arial', 20), height = 2)

        #Frame packing

        topframe.pack()
        botframe.pack()
        nframe1.pack(side=LEFT)
        nframe2.pack(side=LEFT)
        nframe3.pack(side=LEFT)
        mframe.pack(side=LEFT)
        eframe.pack(side=BOTTOM)

        # packing
        nbutton_square.pack()
        nbutton_square_root.pack()
        nbutton_delete.pack()
        nbutton9.pack()
        nbutton8.pack()
        nbutton7.pack()
        nbutton6.pack()
        nbutton5.pack()
        nbutton4.pack()
        nbutton3.pack()
        nbutton2.pack()
        nbutton1.pack()

        ebutton0.pack(side=LEFT)
        ebutton_equals.pack(side=RIGHT)

        button_plus.pack()
        button_minus.pack()
        button_times.pack()
        button_divide.pack()

        self.label.pack(side = RIGHT)

        self.number = ""
        self.operators = ""
        self.veg = 0



        def egy(event):
            self.szambekeres(1)

        def ketto(event):
            self.szambekeres(2)

        def harom(event):
            self.szambekeres(3)

        def negy(event):
            self.szambekeres(4)

        def ot(event):
            self.szambekeres(5)

        def hat(event):
            self.szambekeres(6)

        def het(event):
            self.szambekeres(7)

        def nyolc(event):
            self.szambekeres(8)

        def kilenc(event):
            self.szambekeres(9)

        def nulla(event):
            self.szambekeres(0)

        def plusz(event):
            self.muveletek("+")

        def minusz(event):
            self.muveletek("-")

        def szorzas(event):
            self.muveletek("*")

        def osztas(event):
            self.muveletek("/")

        def egyenlo(event):
            self.equals()

        def torles(event):
            self.delete()

        root.bind("1", egy)
        root.bind("2", ketto)
        root.bind("3", harom)
        root.bind("4", negy)
        root.bind("5", ot)
        root.bind("6", hat)
        root.bind("7", het)
        root.bind("8", nyolc)
        root.bind("9", kilenc)
        root.bind("0", nulla)
        root.bind("+", plusz)
        root.bind("-", minusz)
        root.bind("*", szorzas)
        root.bind("/", osztas)
        root.bind("<Return>", egyenlo)
        root.bind("<BackSpace>", torles)


    def szambekeres(self, n):
        self.t += str(n)
        self.update_text()

    def muveletek(self, n):
        self.operators += n
        self.t += str(self.number)
        self.t += str(n)
        self.number = ""
        self.update_text()

    def equals(self):
        self.t += str(self.number)
        self.t += "="
        self.number = ""
        self.numbers = re.findall(r"[\w']+", self.t)


        for i in range(len(self.operators)):
            if self.operators[i] == "|":
                self.numbers[i] = self.square_root(int(self.numbers[i]))

        for i in range(len(self.operators)):
            if self.operators[i] == "^":
                self.numbers[i] = self.square(int(self.numbers[i]), int(self.numbers[i + 1]))
                self.numbers.pop(i + 1)

        for i in range(len(self.operators)):
            if self.operators[i] == "*":
                self.numbers[i] = int(self.numbers[i]) * int(self.numbers[i + 1])
                self.numbers.pop(i + 1)

        for i in range(len(self.operators)):
            if self.operators[i] == "/":
                self.numbers[i] = int(self.numbers[i]) / int(self.numbers[i + 1])
                self.numbers.pop(i + 1)

        self.vegeredmeny = float(self.numbers[0])

        i = 0

        while i != len(self.operators):
            i += 1
            if i == 0:
                self.vegeredmeny = float(self.numbers[0])
            else:
                if self.operators[i - 1] == "+":
                    self.vegeredmeny += float(self.numbers[i])
                if self.operators[i - 1] == "-":
                    self.vegeredmeny -= float(self.numbers[i])

        veg = round(self.vegeredmeny, 3)
        self.t += str(veg)
        self.update_text()

        self.number = ""
        self.numbers = []
        self.operators = ""
        self.t = ""

    def update_text(self):
        # A felső szöveg frissítése a bekért számok/műveletek szerint
        self.label.configure(text = self.t)

    def delete(self):
        van = False
        for i in self.t:
            if i == "+" or i == "-" or i == "*" or i == "/":
                van = True
        muv = "/*-+"
        if van:
            for i in muv:
                if self.t[len(self.t) - 1] == i:
                    self.operators = self.operators[:-1]
                    self.t = self.t[:-1]
        else:
            self.t = self.t[:-1]

        self.update_text()

    def square_root(self, n):
        return math.sqrt(n)

    def square(self, n, y):
        return n ** y

if __name__ == '__main__':
    root = Tk()
    root.geometry("300x490")
    root.title("Számológép")
    game = App(root)
    root.mainloop()
