#cart functions

class Item(object):
    def __init__(self, name, price, taxed):
        self.name = str(name)
        self.price = float(format(float(price), '.2f'))
        if taxed.lower() == "true":
            self.taxed = True
        else:
            self.taxed = False
        return
    def print(self):
        "usage: returns a formatted price string for printing"
        price = str(self.price)
        #determine if trailing zero is needed
        if len(price) - (price.find('.') + 1) == 1:
            price = price + '0'
        fmtprice = "$" + price
        #equalize spaceing
        fmtprice = fmtprice + ' '*(20 - len(fmtprice))
        #add in name
        fmtprice = fmtprice + self.name + '\n'
        return fmtprice

class Cart(object):
    def __init__(self, taxRate):
        self.taxRate = taxRate
        self.cart = list()
        self.subtotal = 0.0
        self.tax = 0.0
        self.total = 0.0
        self.transID = None # transaction ID
        return
    def add(self, item):
        "usage: adds an item to the 'cart'"
        self.cart.append(item)
        return
    def remove(self, item):
        "usage: removes an item from the cart given another item object with the same fields"
        for i in self.cart:
            if i.name == item.name and i.price == item.price and i.taxed == item.taxed:
                self.card.remove(i)
                break
        return
    def clear(self):
        "usage: resets cart object to default"
        self.__init__(self.taxRate)
        return
    def getNontaxable(self):
        "usage: returns the total of the non taxed items in the cart"
        nontax = 0
        for item in self.cart:
            if not item.taxed:
                nontax += item.price
        return nontax
    def getTaxable(self):
        "usage: returns the total of the taxed items in the cart"
        taxable = 0
        for item in self.cart:
            if item.taxed:
                taxable += item.price
        return taxable
    def maketotal(self):
        "usage: returns a tuple of the (subtotal, tax, total) of the items in the cart"
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        for item in self.cart:
            self.subtotal += item.price
            if item.taxed:
                self.tax += item.price * self.taxRate
        self.total = self.subtotal + self.tax
        
        # cosmetic changes for str return
        self.total = float(format(self.total, '.2f'))
        total = str(self.total)
        if len(total) - (total.find('.') + 1) == 1:
            total = total + '0'
        
        self.tax = float(format(self.tax, '.2f'))
        tax = str(self.tax)
        if len(tax) - (tax.find('.') + 1) == 1:
            tax = tax + '0'
        
        self.subtotal = float(format(self.subtotal, '.2f'))
        subtotal = str(self.subtotal)
        if len(subtotal) - (subtotal.find('.') + 1) == 1:
            subtotal = subtotal + '0'
        
        # return is in format (subtotal, tax, total)
        return (subtotal, tax, total)

#tests

if __name__=='__main__':
    import records as records
    #testing CSV functions as well
    taxrate = 0.0775
    one = Item('one', 2, 'True')
    two = Item('two', 15, 'False')
    three = Item('three', 3, 'true')
    four = Item('four', 5, 'false')
    c = Cart(taxrate)
    c.add(one)
    c.add(two)
    c.add(three)
    c.add(four)
    ret = c.maketotal()
    print(ret[0], ret[1], ret[2])
    #testing CSV function
    records.saveRecord(c)

