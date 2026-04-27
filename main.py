from appointment import (
    Appointment,
    VaccinationDecorator,
    SurgeryDecorator,
)
from veterinary_practice import veterinary_practice


class UserInterface:
    def __init__(self, vp):
        self.vp = vp

    def book_appointment(self):
        if not self.vp.has_owners():
            print("Register a pet first!")
            return

        pet = self._enter_details_to_find_existing_pet()

        print("Enter appointment date and time:")
        time = input()

        # Apply decorators (2 vaccinations + 1 surgery)
        appointment = Appointment(pet, time)
        appointment = VaccinationDecorator(appointment)
        appointment = VaccinationDecorator(appointment)
        appointment = SurgeryDecorator(appointment)

        appointment_id = self.vp.create_appointment(appointment)
        print(f"The appointment ID is {appointment_id}")