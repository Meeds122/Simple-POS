#gui classes

#includes
import tkinter as tk # python 3 import
import configparser as cp
#import cart functions
from cart import *

#TODO:
#    Finish special input
#    close app if Keypad OR Display closes
#    Create Admin class and hook into Keypad.admin()


configFile = "config.ini" # Config file location

buttons = [] # structure [[('name', 'item 1'), ('price', '1.0'), ('istaxed', 'true')],...]
taxRate = 0.0
recieptPrinter = "blah"
paperPrinter = "blah"


def init_config(configFile):
    global buttons
    global taxRate
    global recieptPrinter
    global paperPrinter
    parser = cp.ConfigParser()
    parser.read(configFile)
    #fill buttons list
    for section in parser.sections():
        if "Button" in section:
            buttons.append(parser.items(section))
        elif "Tax" in section:
            for name, value in parser.items(section):
                taxRate = value
    return

class Keypad(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        
        #start text display
        self.newWindow = tk.Toplevel(self.master)
        self.app = Display(self.newWindow)

        #get config
        global buttons
        global taxRate
        
        init_config(configFile)
        
        self.button = buttons
        self.taxRate = taxRate
        self.cart = Cart(float(self.taxRate))
        #buttons
        b1 = tk.Button(self, text=str(buttons[0][0][1]), command=self.button1, height = 10, width = 20).grid(row=0, column=0)
        b2 = tk.Button(self, text=str(buttons[1][0][1]), command=self.button2, height = 10, width = 20).grid(row=0, column=1)
        b3 = tk.Button(self, text=str(buttons[2][0][1]), command=self.button3, height = 10, width = 20).grid(row=0, column=2)
        b4 = tk.Button(self, text=str(buttons[3][0][1]), command=self.button4, height = 10, width = 20).grid(row=1, column=0)
        b5 = tk.Button(self, text=str(buttons[4][0][1]), command=self.button5, height = 10, width = 20).grid(row=1, column=1)
        b6 = tk.Button(self, text=str(buttons[5][0][1]), command=self.button6, height = 10, width = 20).grid(row=1, column=2)
        b7 = tk.Button(self, text=str(buttons[6][0][1]), command=self.button7, height = 10, width = 20).grid(row=2, column=0)
        b8 = tk.Button(self, text=str(buttons[7][0][1]), command=self.button8, height = 10, width = 20).grid(row=2, column=1)
        b9 = tk.Button(self, text=str(buttons[8][0][1]), command=self.button9, height = 10, width = 20).grid(row=2, column=2)
        #special functions
        bspecial = tk.Button(self, text="Special", command=self.special, height = 10, width = 20).grid(row=3, column=0)
        badmin = tk.Button(self, text="Admin", command=self.admin, height = 10, width = 20).grid(row=3, column=1)
        bfinalize = tk.Button(self, text="Finalize", command=self.finalize, height = 10, width = 20).grid(row=3, column=2)
    def button1(self):
        item = Item(self.button[0][0][1], self.button[0][1][1], self.button[0][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button2(self):
        item = Item(self.button[1][0][1], self.button[1][1][1], self.button[1][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button3(self):
        item = Item(self.button[2][0][1], self.button[2][1][1], self.button[2][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button4(self):
        item = Item(self.button[3][0][1], self.button[3][1][1], self.button[3][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button5(self):
        item = Item(self.button[4][0][1], self.button[4][1][1], self.button[4][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button6(self):
        item = Item(self.button[5][0][1], self.button[5][1][1], self.button[5][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button7(self):
        item = Item(self.button[6][0][1], self.button[6][1][1], self.button[6][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button8(self):
        item = Item(self.button[7][0][1], self.button[7][1][1], self.button[7][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def button9(self):
        item = Item(self.button[8][0][1], self.button[8][1][1], self.button[8][2][1])
        self.app.update(item.print())
        self.cart.add(item)
        self.update_total()
        return
    def special(self):
        self.sinputWindow = tk.Toplevel(self.master)
        self.specialInput = Special(self.sinputWindow)
        return
    def admin(self):
        self.adminWindow = tk.Toplevel(self.master)
        self.admin = Admin(self.adminWindow)
        return
    def finalize(self):
        self.app.update("FIN\n")
        self.app.clear()
        self.cart.clear()
        self.update_total()
        return
    def update_total(self):
        status = self.cart.maketotal()
        self.app.update_total("Subtotal: $" + str(status[0]) + "    Tax: $" + str(status[1]) + "    Total: $" + str(status[2]))
        return

#slave window to display text
class Display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.RIGHT)
        self.disp = tk.Text(self.frame, state='disabled', width=60, height=40)
        self.disp.pack()
        self.dispTotal = tk.Text(self.frame, state='disabled', width=60, height=1)
        self.dispTotal.pack()
    def update(self, stuff):
        self.disp.configure(state='normal')
        self.disp.insert('end', stuff)
        self.disp.configure(state='disabled')
    def clear(self):
        self.disp.configure(state='normal')
        self.disp.delete('1.0', tk.END)
        self.disp.configure(state='disabled')
        return
    def update_total(self, newTotal):
        self.dispTotal.configure(state='normal')
        self.dispTotal.delete('1.0', tk.END)
        self.dispTotal.insert('end', newTotal)
        self.dispTotal.configure(state='disabled')

#special input
class Special():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.entry = tk.Entry(self.master, text="Amount: ")
        self.entry.grid(row=0, column=0)
        self.taxed = tk.Button(self.master, text="Taxed", command=self.retTaxed, height = 2, width = 10).grid(row=0, column=1)
        self.untaxed = tk.Button(self.master, text="Non-Taxed", command=self.retNonTaxed, height=2, width=10).grid(row=0, column=2)
    def retTaxed(self):
        self.kill((self.entry.get(), 'true'))
    def retNonTaxed(self):
        self.kill((self.entry.get(), 'false'))
    def kill(self, ret):
        # I need to pass the values from entry to Keypad() somehow
        self.master.destroy() # Seems to work for the objective. More testing needed

#admin section
class Admin():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        #define buttons to do admin things.














