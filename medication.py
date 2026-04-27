"""medication.py
Represents a medication and implements the Subject in the Observer pattern.
"""


class Medication:
    """Represents a medication with stock management and observer support."""

    def __init__(self, name, amount_in_stock):
        """
        :param name: Name of the medication
        :param amount_in_stock: Initial stock quantity
        """
        self.name = name
        self.amount_in_stock = amount_in_stock

        # List of observers (prescriptions)
        self._observers = []

    # ---------------------------
    # Observer pattern methods

    def attach(self, observer):
        """Attach a prescription as an observer."""
        self._observers.append(observer)

    def detach(self, observer):
        """Detach a prescription observer."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        """Notify all observers when stock changes."""
        for observer in self._observers:
            observer.update()

    # ---------------------------
    # Stock management

    def restock(self, amount):
        """Increase stock and notify observers."""
        self.amount_in_stock += amount
        self.notify()

    def reduce_stock(self, amount):
        """Decrease stock and notify observers."""
        self.amount_in_stock -= amount
        self.notify()

    def has_enough_stock(self, dosage):
        """
        Check if there is enough stock for a given dosage.
        :return: True or False
        """
        return self.amount_in_stock >= dosage