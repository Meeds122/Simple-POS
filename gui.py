#Simple-POS/gui.py

#includes
import tkinter as tk # python 3 import
import configparser as cp
#import cart functions
from cart import Cart, Item
#import records functions
import records as records
#import printing functions
import printing as printing

configFile = "config.ini" # Config file location

buttons = [] # structure [[('name', 'item 1'), ('price', '1.0'), ('istaxed', 'true')],...]
taxRate = 0.0


"""
This file defines the structures and relationships of the point and click bits. 

Keypad() called initially

Keypad().__init__() calles Display

Keypad.special() calles Special()

Keypad.admin() calls Admin()

Keypad.finalize() calls Finalize()
"""

def init_config(configFile):
    global buttons
    global taxRate
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

        self.sinputItem = None
        
        self.button = buttons
        self.taxRate = taxRate
        self.cart = Cart(float(self.taxRate))
        #buttons
        tk.Button(self, text=str(buttons[0][0][1]), command=self.button1, height = 10, width = 20).grid(row=0, column=0)
        tk.Button(self, text=str(buttons[1][0][1]), command=self.button2, height = 10, width = 20).grid(row=0, column=1)
        tk.Button(self, text=str(buttons[2][0][1]), command=self.button3, height = 10, width = 20).grid(row=0, column=2)
        tk.Button(self, text=str(buttons[3][0][1]), command=self.button4, height = 10, width = 20).grid(row=1, column=0)
        tk.Button(self, text=str(buttons[4][0][1]), command=self.button5, height = 10, width = 20).grid(row=1, column=1)
        tk.Button(self, text=str(buttons[5][0][1]), command=self.button6, height = 10, width = 20).grid(row=1, column=2)
        tk.Button(self, text=str(buttons[6][0][1]), command=self.button7, height = 10, width = 20).grid(row=2, column=0)
        tk.Button(self, text=str(buttons[7][0][1]), command=self.button8, height = 10, width = 20).grid(row=2, column=1)
        tk.Button(self, text=str(buttons[8][0][1]), command=self.button9, height = 10, width = 20).grid(row=2, column=2)
        #special functions
        tk.Button(self, text="Special", command=self.special, height = 10, width = 20).grid(row=3, column=0)
        tk.Button(self, text="Admin", command=self.admin, height = 10, width = 20).grid(row=3, column=1)
        tk.Button(self, text="Finalize", command=self.finalize, height = 10, width = 20).grid(row=3, column=2)
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
        self.specialInput = Special(self.sinputWindow, self)
        return
    def admin(self):
        self.adminWindow = tk.Toplevel(self.master)
        self.admin = Admin(self.adminWindow, self)
        return
    def finalize(self):
        if len(self.cart.cart) < 1:
            #if cart is empty, ignore request to finalize
            return
        # Need to make payment_method settable by user
        self.finalize_window = tk.Toplevel(self.master)
        self.finalize = Finalize(self.finalize_window, self, self.cart)
        return
    def check_special_input(self):
        if(self.sinputItem):
            self.cart.add(self.sinputItem)
            self.app.update(self.sinputItem.print())
            self.sinputItem = None
            self.update_total()
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
        self.disp = tk.Text(self.frame, state='disabled', width=60, height=39)
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
    def __init__(self, master, caller):
        self.master = master
        self.caller = caller
        self.frame = tk.Frame(self.master)
        self.entry = tk.Entry(self.master, text="Amount: ")
        self.entry.grid(row=0, column=0)
        self.taxed = tk.Button(self.master, text="Taxed", command=self.retTaxed, height = 2, width = 10).grid(row=0, column=1)
        self.untaxed = tk.Button(self.master, text="Non-Taxed", command=self.retNonTaxed, height=2, width=10).grid(row=0, column=2)
        self.quit = tk.Button(self.master, text="Exit Menu", command=self.kill, height=2, width=8).grid(row=0, column=3)
    def retTaxed(self):
        self.kill((self.entry.get(), 'true'))
    def retNonTaxed(self):
        self.kill((self.entry.get(), 'false'))
    def kill(self, ret=None):
        if(ret == None):
            self.master.destroy() # exit button kill needs to catch before trying to subscript it
        elif(ret[1] == 'true'):
            self.caller.sinputItem = Item("Special Input - Taxed", ret[0], ret[1])
        elif(ret[1] == 'false'):
            self.caller.sinputItem = Item("Special Input - NonTaxed", ret[0], ret[1])
        self.master.destroy() # Seems to work for the objective. More testing needed

#admin section
class Admin():
    def __init__(self, master, caller):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.caller = caller

        #define buttons to do admin things.
        tk.Button(self.master, text="Clear Cart", command=self.clearCart, height=2, width=10).grid(row=0, column=0)
        tk.Button(self.master, text="Refund\n(Trans ID Req.)", command=self.refundCart, height=2, width=10).grid(row=0, column=1)
        tk.Button(self.master, text="Print Dayfile", command=self.printDay, height=2, width=10).grid(row=0, column=2)

        tk.Button(self.master, text="View History", command=self.history, height=2, width=10).grid(row=1, column=0)
        tk.Button(self.master, text="Save and Quit", command=self.saveQuit, height=2, width=10).grid(row=1, column=1)
        tk.Button(self.master, text="Exit Menu", command=self.kill, height=2, width=10).grid(row=1, column=2)

    def clearCart(self):
        self.caller.cart.clear()
        self.caller.app.clear()
        self.caller.update_total()
        self.kill()
        return
    def refundCart(self):
        return
    def printDay(self):
        printing.printDayFile()
        return
    def history(self):
        return
    def saveQuit(self):
        self.caller.master.destroy()
        return
    def kill(self):
        self.master.destroy()

class Finalize():
    def __init__(self, master, caller, cart):
        self.caller = caller
        self.master = master
        self.cart = cart
        

        self.frame = tk.Frame(self.master)

        self.button1 = tk.Button(self.master, text="Cash", command=self.cashCheckout, height=2, width=10)
        self.button1.grid(row=0, column=0)
        
        self.button2 = tk.Button(self.master, text="Credit/Debit", command=self.plasticCheckout, height=2, width=10)
        self.button2.grid(row=0, column=1)
        
        self.button3 = tk.Button(self.master, text="Check", command=self.checkCheckout, height=2, width=10)
        self.button3.grid(row=0, column=2)
    def cashCheckout(self):
        self.cart.payment_method = "cash"
        self.makeChange()
        return
    def plasticCheckout(self):
        self.cart.payment_method = "card"
        self.kill()
        return
    def checkCheckout(self):
        self.cart.payment_method = "check"
        self.kill()
        return
    #Clearing up the cart needs to go here because mainloop is non blocking and will execute while checking out if in Keypad.finalize()
    def kill(self):
        self.cart.transID = records.saveRecord(self.cart)
        printing.printReceipt(self.cart)
        self.caller.app.clear()
        self.caller.cart.clear()
        self.caller.update_total()
        self.master.destroy()
    def makeChange(self):
        self.in_cash = []
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button1 = tk.Button(self.master, text="1", command=self._one, height=5, width=10)
        self.button1.grid(row=0, column=0)
        self.button2 = tk.Button(self.master, text="2", command=self._two, height=5, width=10)
        self.button2.grid(row=0, column=1)
        self.button3 = tk.Button(self.master, text="3", command=self._three, height=5, width=10)
        self.button3.grid(row=0, column=2)
        self.button4 = tk.Button(self.master, text="4", command=self._four, height=5, width=10)
        self.button4.grid(row=1, column=0)
        self.button5 = tk.Button(self.master, text="5", command=self._five, height=5, width=10)
        self.button5.grid(row=1, column=1)
        self.button6 = tk.Button(self.master, text="6", command=self._six, height=5, width=10)
        self.button6.grid(row=1, column=2)
        self.button7 = tk.Button(self.master, text="7", command=self._seven, height=5, width=10)
        self.button7.grid(row=2, column=0)
        self.button8 = tk.Button(self.master, text="8", command=self._eight, height=5, width=10)
        self.button8.grid(row=2, column=1)
        self.button9 = tk.Button(self.master, text="9", command=self._nine, height=5, width=10)
        self.button9.grid(row=2, column=2)
        self.button0 = tk.Button(self.master, text="0", command=self._zero, height=5, width=10)
        self.button0.grid(row=3, column=1)

        self.make_change_button = tk.Button(self.master, text="Make Change", command=self._displayChange, height=5, width=10)
        self.make_change_button.grid(row=3, column=2)
        
        self.display_change = tk.Text(self.master, state='disabled', width=10, height=1)
        self.display_change.grid(row=4, column=1)

    # these functions are destined to be used internally by self.makeChange()
    def _one(self):
        self.in_cash.append("1")
        self._update_disp()
    def _two(self):
        self.in_cash.append("2")
        self._update_disp()
    def _three(self):
        self.in_cash.append("3")
        self._update_disp()
    def _four(self):
        self.in_cash.append("4")
        self._update_disp()
    def _five(self):
        self.in_cash.append("5")
        self._update_disp()
    def _six(self):
        self.in_cash.append("6")
        self._update_disp()
    def _seven(self):
        self.in_cash.append("7")
        self._update_disp()
    def _eight(self):
        self.in_cash.append("8")
        self._update_disp()
    def _nine(self):
        self.in_cash.append("9")
        self._update_disp()
    def _zero(self):
        self.in_cash.append("0")
        self._update_disp()
    def _update_disp(self):
        if len(self.in_cash) > 2:
            #more than 1$
            self.string_in_cash = ""
            self.string_in_cash += "".join(self.in_cash[:-2]) # grap pre decimal amount
            self.string_in_cash += "." + "".join(self.in_cash[-2:]) # grab decimal amount
        elif (len(self.in_cash) <= 2) and (len(self.in_cash) != 0):
            #less than 1$
            if len(self.in_cash) == 1:
                self.string_in_cash = ".0" + self.in_cash[0]
            else:
                self.string_in_cash = "." + "".join(self.in_cash)
        else: 
            # len(self.in_cash == 0)
            self.string_in_cash = ".00"
        self.display_change.configure(state='normal')
        self.display_change.delete('1.0', tk.END)
        self.display_change.insert('end', "$" + self.string_in_cash)
        self.display_change.configure(state='disabled')
    def _destroyButtons(self):
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        self.button7.destroy()
        self.button8.destroy()
        self.button9.destroy()
        self.button0.destroy()
        self.make_change_button.destroy()
        return
    def _displayChange(self):
        #if not enough money in self.string_in_cash return from function
        if float(self.string_in_cash) < float(self.cart.maketotal()[2]):
            return
        
        self._destroyButtons()
        #figure out change from self.in_cash
        #self.in_cash is a list of char in numbers
        change = float(self.string_in_cash) - float(self.cart.maketotal()[2])
        
        string_change = "Change: $" + format(change, '.2f') # format returns string so no conversion needed
        
        #set text box to show change
        self.display_change.destroy()
        self.display_change = tk.Text(self.master, state='disabled', width=30, height=1)
        self.display_change.grid(row=0, column=0)
        
        self.exit_button = tk.Button(self.master, text="Return", command=self.kill, height=2, width=10)
        self.exit_button.grid(row=0, column=1)
        
        self.display_change.configure(state='normal')
        self.display_change.delete('1.0', tk.END)
        self.display_change.insert('end', string_change)
        self.display_change.configure(state='disabled')
        # need a destroy button when cashier is done
        
        











