#gui classes

#includes
import tkinter as tk # python 3 import


class Keypad(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        #start text display
        self.newWindow = tk.Toplevel(self.master)
        self.app = Display(self.newWindow)

        #temporary
        self.button_labels = [1,2,3,4,5,6,7,8,9]
        
        
        self.items = list()
        #buttons
        b1 = tk.Button(self, text=str(self.button_labels[0]), command=self.button1, height = 10, width = 20).grid(row=0, column=0)
        b2 = tk.Button(self, text=str(self.button_labels[1]), command=self.button2, height = 10, width = 20).grid(row=0, column=1)
        b3 = tk.Button(self, text=str(self.button_labels[2]), command=self.button3, height = 10, width = 20).grid(row=0, column=2)
        b4 = tk.Button(self, text=str(self.button_labels[3]), command=self.button4, height = 10, width = 20).grid(row=1, column=0)
        b5 = tk.Button(self, text=str(self.button_labels[4]), command=self.button5, height = 10, width = 20).grid(row=1, column=1)
        b6 = tk.Button(self, text=str(self.button_labels[5]), command=self.button6, height = 10, width = 20).grid(row=1, column=2)
        b7 = tk.Button(self, text=str(self.button_labels[6]), command=self.button7, height = 10, width = 20).grid(row=2, column=0)
        b8 = tk.Button(self, text=str(self.button_labels[7]), command=self.button8, height = 10, width = 20).grid(row=2, column=1)
        b9 = tk.Button(self, text=str(self.button_labels[8]), command=self.button9, height = 10, width = 20).grid(row=2, column=2)
        #special functions
        bspecial = tk.Button(self, text="Special", command=self.special, height = 10, width = 20).grid(row=3, column=0)
        badmin = tk.Button(self, text="Admin", command=self.admin, height = 10, width = 20).grid(row=3, column=1)
        bfinalize = tk.Button(self, text="Finalize", command=self.finalize, height = 10, width = 20).grid(row=3, column=2)
    def button1(self):
        self.app.update("1\n")
        return
    def button2(self):
        self.app.update("2\n")
        return
    def button3(self):
        self.app.update("3\n")
        return
    def button4(self):
        self.app.update("4\n")
        return
    def button5(self):
        self.app.update("5\n")
        return
    def button6(self):
        self.app.update("6\n")
        return
    def button7(self):
        self.app.update("7\n")
        return
    def button8(self):
        self.app.update("8\n")
        return
    def button9(self):
        self.app.update("9\n")
        return
    def special(self):
        self.app.update("SPECIAL\n")
        self.sinputWindow = tk.Toplevel(self.master)
        self.specialInput = Special(self.sinputWindow)
        return
    def admin(self):
        self.app.update("ADMIN\n")
        return
    def finalize(self):
        self.app.update("FIN\n")
        self.app.clear()
        return

#slave window to display text
class Display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.RIGHT)
        self.disp = tk.Text(self.frame, state='disabled', width=60, height=40)
        self.disp.pack()
    def update(self, stuff):
        self.disp.configure(state='normal')
        self.disp.insert('end', stuff)
        self.disp.configure(state='disabled')
    def clear(self):
        #have to figure out how to clear box
        return

#special input
class Special():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.entry = tk.Entry(self.master, text="Amount: ").grid(row=0, column=0)
        self.taxed = tk.Button(self.master, text="Taxed", command=self.retTaxed, height = 2, width = 10).grid(row=0, column=1)
        self.untaxed = tk.Button(self.master, text="Non-Taxed", command=self.retNonTaxed, height=2, width=10).grid(row=0, column=2)
    def retTaxed(self):
        return
    def retNonTaxed(self):
        return
