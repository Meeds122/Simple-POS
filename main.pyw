#!/usr/bin/python3
#Simple-POS/main.pyw


#TODO:
#    finish admin section
#    close app if Keypad OR Display closes
#    Cart.transID should be implemented and printed on reciept. Cart.transID needs to be set in records.py using current time.  
#    refractor globals and init_config into Keypad somehow
#    Admin.help()? Help menu in admin?
#    
#    Finish records.py transID and file_name generators.
#    Finish printing functions in printing.py.

#NOTES:
#    CSV file is for daily records retention. Actual cart objects to be stored elsewhere prolly xml


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
