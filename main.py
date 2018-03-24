#includes
import tkinter as tk # python 3 inport

#gui
"""

"""
class Keypad(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        #start text display
        self.newWindow = tk.Toplevel(self.master)
        self.app = Display(self.newWindow)
        
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
        self.app.update("1")
        return
    def button2(self):
        self.app.update("2")
        return
    def button3(self):
        self.app.update("3")
        return
    def button4(self):
        self.app.update("4")
        return
    def button5(self):
        self.app.update("5")
        return
    def button6(self):
        self.app.update("6")
        return
    def button7(self):
        return
    def button8(self):
        return
    def button9(self):
        return
    def special(self):
        return
    def admin(self):
        return
    def finalize(self):
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

#
def main():
    root = tk.Tk()
    keypad = Keypad(root)
    keypad.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
