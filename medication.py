""" medication.py """

class Medication():
    def __init__(self, name, amount_in_stock):
        self.name = name
        self.amountInStock = amount_in_stock
        
        # observer list
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for obs in self._observers:
            obs.update()

    def restock(self, amount):
        self.amountInStock += amount
        self.notify()

    def reduce_stock(self, amount):
        self.amountInStock -= amount
        self.notify()

    def has_enough_stock(self, dosage):
        return self.amountInStock >= dosage