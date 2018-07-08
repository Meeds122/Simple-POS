#records retention
"""
My idea so far is to read file into memory when recording a transaction, edit file, overwrite with new file
that way if there is an issue an uncorrupted copy of the day file is sitting on the harddrive for as long as possible

Tests for these functions are bundled with the cart tests in cart.py
"""

from os import path
import csv
import datetime


def generateTransID():
    tid = 1807080451443
    # logic to do ID currently I'm thinking that either time since epoc or yymmddhhmmss[ms] == 1807080450443
    return tid

def generateFileName():
    fname = "july-8-2018.csv"
    # logic to generate daily file name
    # most important question, mmddyy ddmmyy or yymmdd?
    return fname

def saveRecord(cart):
    cart.transID = generateTransID()
    appendCSV(generateFileName(), cart)
    return



"""
createCSV(file_name)
usage:
    create .csv file and insert the header
"""
def createCSV(file_name):
    with open(str(file_name), 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Trans ID", "NonTaxable", "Taxable", "Subtotal", "Tax", "Total"])
    return

"""
appendCSV(file_name, cart)
usage:
    append relevent details of a cart to the daily CSVfile
    CSV format as follows: transactionID | total nontaxable | total taxable | subtotal | tax | total

    needs to be used with the Cart() class from Simple-POS/cart.py
"""
def appendCSV(file_name, cart):
    rows = readCSV(file_name)
    transID = cart.transID
    subtotal, tax, total = cart.maketotal()
    taxable = cart.getTaxable()
    nontaxable = cart.getNontaxable()
    rows.append([str(transID), str(nontaxable), str(taxable), str(subtotal), str(tax), str(total)])
    #write file and handle file not existing
    with open(str(file_name), 'w', newline='') as CSV_file:
        writer = csv.writer(CSV_file)
        for line in rows:
            writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5]])
    return True

"""
def readCSV(fileName)
usage:
    exactly as it looks
    returns list of lines from csv file
"""
def readCSV(fileName):
    csvlist = list()
    try:
        with open(str(fileName), 'r', newline='') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                csvlist.append(row)
    except: # create file + header if none exists
        createCSV(fileName)
        csvlist = readCSV(fileName) # try to read again
    return csvlist






