#!/usr/bin/python3
#Simple-POS/main.pyw

#gui
from gui import *

#start GUI main loop
def main():
    root = tk.Tk()
    keypad = Keypad(root)
    keypad.pack()
    # Replaces root.mainloop()
    while True:
        root.update_idletasks()
        root.update()
        #should be able to insert keypad.check_special_input() here
        #root.update* are nonblocking unlike tk.mainloop()
        keypad.check_special_input()

if __name__ == '__main__':
    main()
