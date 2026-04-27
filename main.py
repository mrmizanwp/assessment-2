""" main.py

Starts the Veterinary Practice application and contains the UserInterface class.
The UI menu is displayed to the user until they choose to exit the application.

"""

from appointment import Appointment, VaccinationDecorator, SurgeryDecorator
from veterinary_practice import veterinary_practice

class UserInterface:
    """
    Displays the menu options to the user and allow the user to interact with the various options.
    """

    def __init__(self, vp):
        self.vp = vp

    def menu(self):

        print("Select one of the following options:")
        print("  1. Register a pet")
        print("  2. Book an appointment")
        print("  3. Attend an appointment")
        print("  4. Stock/re-stock a medication")
        print("  5. Create a prescription")
        print("  6. Prepare a prescription for collection")
        print("  7. Pick-up a prescription")
        print("  8. Exit")

        print("Enter the number of the option you wish to select:")
        option = int(input())
        
        match option:
            case 1:
                self.register_pet()
            case 2:
                self.book_appointment()
            case 3:
                self.attend_appointment()
            case 4:
                self.stock_medication()
            case 5:
                self.create_prescription()
            case 6:
                self.prepare_prescription()
            case 7:
                self.collect_prescription()
            case 8:
                return False
            case _:
                print("Unknown option selected")
        return True
    
    def register_pet(self):
        print("Enter owner's name:")
        owner_name = input()
        print("Enter pet's name:")
        pet_name = input()
        print("Enter pet's species:")
        species = input()

        self.vp.register_pet(pet_name, owner_name, species)

    def book_appointment(self):
        if not self.vp.has_owners():
            print("Register a pet first!")
            return
        
        pet = self._enter_details_to_find_existing_pet()

        print("Enter appointment date and time (any string is accepted):")
        time = input()

        # ✅ Decorator applied here (assignment requirement)
        appointment = Appointment(pet, time)
        appointment = VaccinationDecorator(appointment)
        appointment = VaccinationDecorator(appointment)
        appointment = SurgeryDecorator(appointment)

        id = self.vp.create_appointment(appointment)
        print(f"The appointment ID is {id}")
 
    
    def attend_appointment(self):
        print("Enter appointment ID:")
        appointment_id = int(input())
        notes = self.vp.attend_appointment(appointment_id)
        print(f"Appointment notes: {notes}")
    
    def stock_medication(self):
        print("Enter medication name:")
        medication_name = input()
        print("Enter amount of medication that has been delivered:")
        amount = int(input())
        self.vp.stock_medication(medication_name, amount)

    def create_prescription(self):
        
        if not self.vp.has_owners() or not self.vp.has_medications():
            print("Register a pet and stock medications first!")
            return       
        
        p = self._enter_details_to_find_existing_pet()

        m = None
        while not m:
            print("Enter medication name:")
            medication_name = input()
            m = self.vp.find_medication(medication_name)

        print("Enter dosage (amount to be given):")
        d = int(input())
        
        id = self.vp.create_prescription(p, m, d)
        print(f"The prescription ID is {id}")   

    
    def prepare_prescription(self):
        print("Enter prescription ID:")
        prescription_id = int(input())
        output = self.vp.prepare_prescription_for_collection(prescription_id)
        print(output)

    def collect_prescription(self):   
        print("Enter prescription ID:")
        prescription_id = int(input())
        output = self.vp.collect_prescription(prescription_id)
        print(output)

    def _enter_existing_owner(self):
        owner = None
        while not owner:
            print("Enter owner's name:")
            owner_name = input()
            owner = self.vp.find_owner(owner_name)
        return owner
    
    def _enter_details_to_find_existing_pet(self):
        owner = self._enter_existing_owner()
        
        pet = None
        while not pet:
            print("Enter pet's name:")
            pet_name = input()
            pet = owner.find_pet(pet_name)
        return pet
    

if __name__ == "__main__":
    ui = UserInterface(veterinary_practice())
    keep_going = True
    while keep_going:
        keep_going = ui.menu()