#records retention
"""
My idea so far is to read file into memory when recording a transaction, edit file, overwrite with new file
that way if there is an issue an uncorrupted copy of the day file is sitting on the harddrive for as long as possible

Need to include header in CSV
"""
#################################################################
from os import path
import csv
import datetime

"""
def updateCSV(fileName, ID, name, numOfClicks, lastClickTime)
Usage:
    update CSV file
current function is to read file into memory, try to find ID, if ID exists, replace line, rewrite into file, else append new ID and rewrite into file
there is probably a much better way of doing this but this is what I've been able to come up with at 3:22AM on a Thursday
"""
def updateCSV(fileName, ID, name, numOfClicks, lastClickTime, addIfNotFound=True):
    #todo
    inCSV = list()
    with open(str(fileName), 'r', newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            inCSV.append(row)
    for i in range(len(inCSV)):
        if str(inCSV[i][0]) == str(ID):
            del inCSV[i]
            inCSV.insert(i, [str(ID), str(name), str(numOfClicks), str(lastClickTime)])
            #update file with new
            with open(str(fileName), 'w', newline='') as csvFile:
                writer = csv.writer(csvFile)
                for line in inCSV:
                    writer.writerow([line[0], line[1], line[2], line[3]])
            return True #return if ID is found in CSV file after updating
    if addIfNotFound == False:
        return False
    #ID not found in CSV file and flag set true, adding
    inCSV.append([str(ID), str(name), str(numOfClicks), str(lastClickTime)])
    with open(str(fileName), 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for line in inCSV:
            writer.writerow([line[0], line[1], line[2], line[3]])
    return True # success

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
    #write file
    with open(str(file_name), 'w', newline='') as CSV_file:
        writer = csv.writer(CSV_file)
        for line in rows:
            writer.writerow([line[0], line[1], line[2], line[3], line[4], line[5])
    return True # success

"""
def readCSV(fileName)
usage:
    exactly as it looks
    returns list of lines from csv file
"""
def readCSV(fileName):
    csvlist = list()
    with open(str(fileName), 'r', newline='') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            csvlist.append(row)
    return csvlist
