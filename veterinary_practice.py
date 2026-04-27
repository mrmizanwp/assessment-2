"""veterinary_practice.py
Contains the veterinary_practice class.
Handles pets, appointments, medications, and prescriptions.
"""

from medication import Medication
from owner import Owner
import utils


class veterinary_practice:
    """
    Stores and manages all veterinary practice data.

    Responsibilities:
    - Register pets
    - Manage appointments
    - Manage medications
    - Manage prescriptions
    """

    def __init__(self):
        """Initialize empty data collections."""
        self.owners = []
        self.medications = []
        self.prescriptions = []
        self.appointments = []

    # ---------------------------
    # Pet management

    def register_pet(self, pet_name, owner_name, species):
        """
        Register a pet. Creates owner if not exists.
        """
        owner = self.find_owner(owner_name)

        if not owner:
            owner = Owner(owner_name)
            self.owners.append(owner)

        owner.add_pet(pet_name, species)

    # ---------------------------
    # Appointment management

    def create_appointment(self, appointment):
        """
        Store appointment and return its ID.
        """
        self.appointments.append(appointment)
        return len(self.appointments) - 1

    def attend_appointment(self, appointment_id):
        """
        Attend an appointment and return notes.
        """
        appointment = self.find_appointment(appointment_id)

        if appointment:
            appointment.attend_appointment()
            return appointment.get_notes()

        return "Unrecognized appointment ID"

    # ---------------------------
    # Medication management

    def stock_medication(self, medication_name, amount):
        """
        Add or restock medication.
        """
        medication = self.find_medication(medication_name)

        if medication:
            medication.restock(amount)
        else:
            medication = Medication(medication_name, amount)
            self.medications.append(medication)

    # ---------------------------
    # Prescription management

    def create_prescription(self, pet, medication, dosage):
        """
        Create prescription and return its ID.
        """
        prescription = pet.create_prescription(medication, dosage)
        self.prescriptions.append(prescription)

        return len(self.prescriptions) - 1

    def prepare_prescription_for_collection(self, prescription_id):
        """
        Prepare prescription if possible.
        """
        prescription = self.find_prescription(prescription_id)

        if prescription:
            # ⚠ IMPORTANT: method name unchanged (test-safe)
            if prescription.prepareForCollection():
                return "Prescription prepared"

            return "Prescription is not ready for preparation"

        return "Unrecognized prescription ID"

    def collect_prescription(self, prescription_id):
        """
        Mark prescription as collected.
        """
        prescription = self.find_prescription(prescription_id)

        if prescription:
            if prescription.collect():
                return "Prescription collected"

            return "Prescription is not ready for collection"

        return "Unrecognized prescription ID"

    # ---------------------------
    # Helper methods

    def has_owners(self):
        return len(self.owners) > 0

    def has_medications(self):
        return len(self.medications) > 0

    def has_prescriptions(self):
        return len(self.prescriptions) > 0

    def find_owner(self, name):
        return utils.find_by_name(name, self.owners)

    def find_medication(self, name):
        return utils.find_by_name(name, self.medications)

    def find_prescription(self, prescription_id):
        if prescription_id < len(self.prescriptions):
            return self.prescriptions[prescription_id]
        return None

    def find_appointment(self, appointment_id):
        if appointment_id < len(self.appointments):
            return self.appointments[appointment_id]
        return None