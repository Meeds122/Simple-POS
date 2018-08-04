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

#NOTES:
#    CSV file is for daily records retention. Actual cart objects to be stored elsewhere prolly xml


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

if __name__ == '__main__':
    main()
