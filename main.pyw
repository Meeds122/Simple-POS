#!/usr/bin/python3
#Simple-POS/main.pyw


#TODO:
#    finish admin section
#    close app if Keypad OR Display closes
#    Need to make Cart.payment_method settable by user
#    refractor globals and init_config into Keypad somehow
#    Admin.help()? Help menu in admin?
#    Finish menu for payment method when calling Keypad.finalize() named ProcessPayment()
#    Keypad.finalize() Should call a new GUI class called Finalize
#    Finish printing functions in printing.py.
#    add Cart.payment_method to CSV file records
#    printing.py needs a parser and format file for reciept formatting
#    printing.py  -> printDayFile() needs to be able to print on linux and OSX boxes. Currently Windows Only!

#NOTES:
#    CSV file is for daily records retention. Actual cart objects to be stored elsewhere prolly xml
#    python-escpos is more than capable of running both the ESC/POS printer and the register through the printer.

#gui
from gui import Keypad, tk

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
        #trying to close if either keypad or display close
        if not keypad.app:
            print("not keypad.app")
            return

if __name__ == '__main__':
    main()
