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
    while True:
        root.update_idletasks()
        root.update()
        #should be able to insert keypad.check_special_input() here
        keypad.check_special_input()

if __name__ == '__main__':
    main()
