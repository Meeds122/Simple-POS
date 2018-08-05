#Simple-POS/printing.py

#functions to print receipt, dayfile, etc.

import records as records # generate dayfile name...
from cart import Cart, Item

import platform # detect platform for printing
import os # windows printing
import subprocess # linux printing

def printReceipt(cart):
    """
    printReceipt(cart)
    usage:
        creates the formatted receipt and prints it
        must be called with a cart object from Simple-POS/cart.py
    """
    return

def printDayFile(day_file_name=None):
    """
    printDayFile(day_file_name(=None))
    usage:
        Parse and print the CSV file summary.
        if day_file_name is unset, today will be used
    """
    if day_file_name == None:
        day_file_name = records.generateFileName()
    csv_lines = records.readCSV(day_file_name)
    
    
    # each is a dict of (cash:0, card:0, check:0)
    day_taxed = {'cash':0.0, 'card':0.0, 'check':0.0}
    day_nontaxed = {'cash':0.0, 'card':0.0, 'check':0.0}
    day_total = {'cash':0.0, 'card':0.0, 'check':0.0}
    day_subtotal = {'cash':0.0, 'card':0.0, 'check':0.0}
    day_tax = {'cash':0.0, 'card':0.0, 'check':0.0}
    number_of_transactions = 0
    
    
    print(csv_lines)
    #format of csv file is [['Trans ID', 'Payment Method', 'Non Taxable', 'Taxable', 'Subtotal', 'Tax', 'Total'], [], ...]
    #ignore first line because it is the title line
    for line in csv_lines[1:]:
        number_of_transactions += 1 # increment transaction counter
        #cash/card/check
        if line[1] == 'cash':
            day_nontaxed['cash'] += float(line[2])
            day_taxed['cash'] += float(line[3])
            day_subtotal['cash'] += float(line[4])
            day_tax['cash'] += float(line[5])
            day_total['cash'] += float(line[6])
        
        elif line[1] == 'card':
            day_nontaxed['card'] += float(line[2])
            day_taxed['card'] += float(line[3])
            day_subtotal['card'] += float(line[4])
            day_tax['card'] += float(line[5])
            day_total['card'] += float(line[6])
        
        elif line[1] == 'check':
            day_nontaxed['check'] += float(line[2])
            day_taxed['check'] += float(line[3])
            day_subtotal['check'] += float(line[4])
            day_tax['check'] += float(line[5])
            day_total['check'] += float(line[6])
    
    #debug
    print("nontaxed: ", day_nontaxed)
    print("taxed: ", day_taxed)
    print("subtotal: ", day_subtotal)
    print("tax", day_tax)
    print("total", day_total)
    print("transactions: ", number_of_transactions)
    
    #write to temporary file
    with open("tmp.txt", 'w') as temp_file:
        temp_file.write("Day Report for " + day_file_name)
        temp_file.write("\n\nSummary:")
        summary = "\n\nNumber of Transactions: " + str(number_of_transactions)
        summary += "\n\nNon-taxable Income: " + str(day_nontaxed['cash'] + day_nontaxed['card'] + day_nontaxed['check'])
        summary +="\n\nTaxable Income: " + str(day_taxed['cash'] + day_taxed['card'] + day_taxed['check'])
        summary += "\n\nTotal Without Tax: " + str(day_subtotal['cash'] + day_subtotal['card'] + day_subtotal['check'])
        summary += "\n\nTax Collected: " + str(day_tax['cash'] + day_tax['card'] + day_tax['check'])
        summary += "\n\nDay Total:\n" + "Cash: " + str(day_total['cash']) + " Card: " + str(day_total["card"]) + " Check: " + str(day_total['check'])
        summary += "\nTogether: " + str(day_total['cash'] + day_total['card'] + day_total['check'])
        summary += "\n\n\n\nCopy of CSV file. This is the central register that keeps track of transactions. Normally you would open this file with"
        summary += " with some spreadsheet software such as Excell or LibreOffice. This is for your records.\n\n"
        temp_file.write(summary)
        for line in csv_lines:
            temp_file.write(str(line) + "\n")
    
    #detect OS and call printer
    current_platform = platform.system()
    if current_platform == "Windows":
        os.startfile("tmp.txt", "print")
        return
    elif current_platform == "Linux":
        #untested. Will need to read in created temp file
        #lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
        #lpr.stdin.write(your_data_here)
        return
    
    return
