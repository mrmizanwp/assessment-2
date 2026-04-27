"""prescription.py
Implements Prescription and Observer behaviour.
"""

from enum import Enum


class PrescriptionStatus(Enum):
    """Tracks the lifecycle of a prescription."""
    preparing_order = 1
    ready_for_collection = 2
    out_of_stock = 3
    collected = 4


class Prescription:
    """Represents a prescription and observes medication stock changes."""

    def __init__(self, pet, medication, dosage):
        """
        :param pet: Pet object
        :param medication: Medication object
        :param dosage: Required dosage
        """
        self.pet = pet
        self.medication = medication
        self.dosage = dosage

        # Register as observer
        self.medication.attach(self)

        self._prepare_or_wait_for_stock()

    def _prepare_or_wait_for_stock(self):
        """Set status based on current stock."""
        if self.medication.has_enough_stock(self.dosage):
            self.status = PrescriptionStatus.preparing_order
        else:
            self.status = PrescriptionStatus.out_of_stock

    # ---------------------------
    # Observer update method

    def update(self):
        """Called automatically when stock changes."""
        if self.status not in (
            PrescriptionStatus.ready_for_collection,
            PrescriptionStatus.collected,
        ):
            self._prepare_or_wait_for_stock()

    # ---------------------------
    # Business logic

    def prepare_for_collection(self):
        """Prepare prescription if stock is available."""
        if self.status == PrescriptionStatus.preparing_order:
            self.medication.reduce_stock(self.dosage)
            self.status = PrescriptionStatus.ready_for_collection

            # Stop observing after preparation
            self.medication.detach(self)
            return True
        return False

    def collect(self):
        """Mark prescription as collected."""
        if self.status == PrescriptionStatus.ready_for_collection:
            self.status = PrescriptionStatus.collected
            return True
        return False