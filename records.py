#records retention
#Tests for these functions are bundled with the cart tests in cart.py

from os import path
import csv
import datetime
import time as time


def saveRecord(cart):
    """
    saveRecord(cart)
    usage:
        Needs to be called with a cart object from Simple-POS/cart.py
        Does all required records retention information generation, saves the record
        returns the transID it set for printing on the reciept
    """
    cart.transID = generateTransID()
    appendCSV(generateFileName(), cart)
    return cart.transID



def generateTransID():
    """
    generateTransID():
        the function returns a unique ID for the transaction based on yymmddhhmmss == 1807080450
    """
    tid = time.strftime("%y%m%d%H%M%S")
    # logic to do ID currently I'm thinking that either time since epoc or yymmddhhmmss
    return tid


def generateFileName():
    """
    generateFileName():
        returns the filename for the CSV dayfile
    """
    fname = time.strftime("%B-%d-%y.csv")
    # logic to generate daily file name
    # most important question, mmddyy ddmmyy or yymmdd?
    return fname


def createCSV(file_name):
    """
    createCSV(file_name)
    usage:
        create .csv file and insert the header
    """
    with open(str(file_name), 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(["Trans ID", "Non Taxable", "Taxable", "Subtotal", "Tax", "Total"])
    return


def appendCSV(file_name, cart):
    """
    appendCSV(file_name, cart)
    usage:
        append relevent details of a cart to the daily CSVfile
        CSV format as follows: transactionID | total nontaxable | total taxable | subtotal | tax | total

        needs to be used with the Cart() class from Simple-POS/cart.py
    """
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


def readCSV(fileName):
    """
    def readCSV(fileName)
    usage:
        exactly as it looks
        returns list of lines from csv file
    """
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






