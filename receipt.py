#Simple-POS/receipt.py

#receipt formatting and parsing functions

import configparser as cp

from cart.py import Cart, Item



def getReceiptConfig(config_file):
    """
    usage: getReceiptConfig(config_file)
        returns a tuple of data from the receipt config file
        data looks like
        (
   1-   [('name', 'Customcrypto.com'),
        ('address', '1 Code Ave. Los Angeles, CA'),
        ('phone', '7606736121'),
        ('fax', 'none'),
        ('email', 'tristan@customcrypto.com')],
   2-   [('greeting', 'Have a great day!')],
   3-   [('image', 'none')],
   4-   [('printer', 'none')]
        )
    """
    parser = cp.ConfigParser()
    parser.read(config_file)
    for section in parser.sections():
        if "Basic" in section:
            basic_info = parser.items(section)
        elif "Greetings" in section:
            greetings = parser.items(section)
        elif "Image" in section:
            image_location = parser.items(section)
        elif "Printer" in section:
            printer_location = parser.items(section)
    return (basic_info, greetings, image_location, printer_location)

def formattedReceipt(receipt_config, cart_obj):
    return