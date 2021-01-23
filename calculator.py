########################################################
# Számológép                                           #
# Version: 1.0 (első működő verzió, némi hibával :))   #
# Made by: Attila Ladányi                              #
# 2020.01.22                                           #
########################################################

from tkinter import *

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

        nbutton7 = Button(nframe1, text="7", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(7))
        nbutton4 = Button(nframe1, text="4", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(4))
        nbutton1 = Button(nframe1, text="1", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(1))

        # Számok 2. Oszlop

        nbutton8 = Button(nframe2, text="8", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(8))
        nbutton5 = Button(nframe2, text="5", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(5))
        nbutton2 = Button(nframe2, text="2", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(2))

        # Számok 3. Oszlop

        nbutton9 = Button(nframe3, text="9", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(9))
        nbutton6 = Button(nframe3, text="6", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(6))
        nbutton3 = Button(nframe3, text="3", height=4, width = 6, font = ('Arial', 15), command = lambda: self.szambekeres(3))

        # Alsó sor (nulla és az egyenlő)

        ebutton0 = Button(eframe, text="0", width = 13, height = 2, font = ('Arial', 15), command = lambda: self.szambekeres(0))
        ebutton_equals = Button(eframe, text="=", width = 13, height = 2, font = ('Arial', 15), command = lambda: self.equals())

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
        self.numbers = []
        self.operators = ""
        self.veg = 0

    def szambekeres(self, n):
        self.number += str(n)

    def muveletek(self, n):
        self.operators += n
        self.numbers.append(int(self.number))
        self.t += str(self.number)
        self.t += str(n)
        self.number = ""
        self.update_text()

    def equals(self):
        self.numbers.append(int(self.number))
        self.t += str(self.number)
        self.t += "="
        self.number = ""
        self.vegeredmeny = self.numbers[0]
        i = 0

        while i != len(self.operators):
            i += 1
            if i == 0:
                self.vegeredmeny = self.numbers[0]
            else:
                if self.operators[i - 1] == "+":
                    self.vegeredmeny += self.numbers[i]
                if self.operators[i - 1] == "-":
                    self.vegeredmeny -= self.numbers[i]
                if self.operators[i - 1] == "*":
                    self.vegeredmeny *= self.numbers[i]
                if self.operators[i - 1] == "/":
                    self.vegeredmeny /= self.numbers[i]

        veg = self.vegeredmeny
        self.t += str(veg)
        self.update_text()

        self.number = ""
        self.numbers = []
        self.operators = ""
        self.t = ""

    def update_text(self):
        # A felső szöveg frissítése a bekért számok/műveletek szerint
        self.label.configure(text = self.t)

if __name__ == '__main__':
    root = Tk()
    root.geometry("300x490")
    root.title("Számológép")
    game = App(root)
    root.mainloop()
