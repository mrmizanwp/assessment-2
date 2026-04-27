from enum import Enum

class PrescriptionStatus(Enum):
    preparing_order = 1
    ready_for_collection = 2
    out_of_stock = 3
    collected = 4

class Prescription():
    def __init__(self, pet, medication, dosage):
        self.pet = pet
        self.medication = medication
        self.dosage = dosage
        
        # attach as observer
        self.medication.attach(self)

        self._prepareOrWaitForStock()

    def _prepareOrWaitForStock(self):
        if self.medication.has_enough_stock(self.dosage):
            self.status = PrescriptionStatus.preparing_order
        else:
            self.status = PrescriptionStatus.out_of_stock

    def update(self):
        if self.status not in [PrescriptionStatus.ready_for_collection, PrescriptionStatus.collected]:
            self._prepareOrWaitForStock()

    def prepareForCollection(self):
        if self.status == PrescriptionStatus.preparing_order:
            self.medication.reduce_stock(self.dosage)
            self.status = PrescriptionStatus.ready_for_collection
            
            # stop observing
            self.medication.detach(self)

            return True
        return False

    def collect(self):
        if self.status == PrescriptionStatus.ready_for_collection:
            self.status = PrescriptionStatus.collected
            return True
        return False