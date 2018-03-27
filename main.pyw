

#includes
import configparser as cp

#gui
from gui import *
#cart functions
from cart import *

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
