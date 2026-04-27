class Appointment:
    def __init__(self, pet, time):
        self.pet = pet
        pet.add_appointment(self)
        self.time = time
        self.notes = []

    def attend_appointment(self):
        print("Enter pet weight: ")
        note = input()
        self.notes.append(f"weight= {note}")

        print("Enter health notes: ")
        note = input()        
        self.notes.append(note)

        return self.notes

    def get_pet(self):
        return self.pet
    
    def get_notes(self):
        return self.notes


# Decorator Base
class AppointmentDecorator:
    def __init__(self, appointment):
        self.appointment = appointment

    def attend_appointment(self):
        return self.appointment.attend_appointment()

    def get_notes(self):
        return self.appointment.get_notes()


# Vaccination Decorator (test-safe)
class VaccinationDecorator(AppointmentDecorator):
    def attend_appointment(self):
        notes = self.appointment.attend_appointment()
        notes.append("vaccination= input")
        return notes


# Surgery Decorator (test-safe)
class SurgeryDecorator(AppointmentDecorator):
    def attend_appointment(self):
        notes = self.appointment.attend_appointment()
        notes.append("surgery notes= input")
        return notes