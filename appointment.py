"""appointment.py
Implements Appointment and Decorator pattern for extended notes.
"""


class Appointment:
    """Stores appointment details and basic notes."""

    def __init__(self, pet, time):
        self.pet = pet
        pet.add_appointment(self)
        self.time = time
        self.notes = []

    def attend_appointment(self):
        """Collect basic appointment notes."""
        print("Enter pet weight:")
        weight = input()
        self.notes.append(f"weight= {weight}")

        print("Enter health notes:")
        note = input()
        self.notes.append(note)

        return self.notes

    def get_notes(self):
        return self.notes


# ---------------------------
# Decorator Base

class AppointmentDecorator:
    """Base decorator for extending appointment behaviour."""

    def __init__(self, appointment):
        self._appointment = appointment

    def attend_appointment(self):
        return self._appointment.attend_appointment()

    def get_notes(self):
        return self._appointment.get_notes()


# ---------------------------
# Concrete Decorators

class VaccinationDecorator(AppointmentDecorator):
    """Adds vaccination notes to appointment."""

    def attend_appointment(self):
        notes = self._appointment.attend_appointment()
        notes.append("vaccination=input")
        return notes


class SurgeryDecorator(AppointmentDecorator):
    """Adds surgery notes to appointment."""

    def attend_appointment(self):
        notes = self._appointment.attend_appointment()
        notes.append("surgery notes=input")
        return notes