#includes
import tkinter as tk # python 3 import


#gui
from gui import *

"""
TODO:
1. read from config file into vars
2. Figure out Display.clear()
3. Build a Item() class
4. Finish GUI functions

"""

#start GUI main loop
def main():
    root = tk.Tk()
    keypad = Keypad(root)
    keypad.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
