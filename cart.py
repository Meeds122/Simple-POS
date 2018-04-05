#cart functions

taxrate = 0.0775

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
        return str("\n" + str(self.name) + "    $" + str(self.price) + "\n")

class Cart(object):
    def __init__(self):
        self.cart = list()
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        is_fin = False
        return
    def add(self, item):
        self.cart.append(item)
        return
    def remove(self, item):
        for i in self.cart:
            if i.name == item.name and i.price == item.price and i.taxed == item.taxed:
                self.card.remove(i)
        return
    def maketotal(self):
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        for item in self.cart:
            self.subtotal += item.price
            if item.taxed:
                self.tax += item.price * taxrate
        self.tax = float(format(self.tax, '.2f'))
        self.total = self.subtotal + self.tax

#tests

if __name__=='__main__':
    one = Item('one', 2, 'True')
    two = Item('two', 15, 'False')
    c = Cart()
    c.add(one)
    c.add(two)
    c.maketotal()
    print(c.subtotal, c.tax, c.total)
