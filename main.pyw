#!/usr/bin/python3

#includes
import configparser as cp

#gui
from gui import *
#cart functions
from cart import *


#start GUI main loop
def main():
    root = tk.Tk()
    keypad = Keypad(root)
    keypad.pack()
    if not keypad.app:
        return
    root.mainloop()

if __name__ == '__main__':
    main()
