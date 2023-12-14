from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from getpass import getpass
from main import Appointment, Doctor, Patient, User
from tabulate import tabulate
from datetime import datetime
from datetime import time

# Connect to the database
engine = create_engine('sqlite:///linda_mama_care.db')
Session = sessionmaker(bind=engine)
session = Session()

#user interface when the program runs
def login_menu():
    print("Welcome to Linda Mama Care!")
    print("1. Login as Doctor")
    print("2. Login as Patient")
    print("3. Exit")
#selection to either login as a doctor or patient
    choice = input("Please enter your choice:")

    if choice == "1":
        login_as_doctor()
    elif choice == "2":
        login_as_patient()
#option 3 is to exit the program        
    elif choice == "3":
        print("Goodbye!")
    else:
               print("Invalid choice. Please try again")

#enter details to log in as doctor
def login_as_doctor():
    username = input("Enter your username:")
    password = getpass("Enter your password:")
#validates the inputs from user and compares with the one stored in database
    doctor = session.query(User).filter(User.username == username, User.password == password, User.role == "doctor").first()
    if doctor:
        print(f"Logged in as Doctor: {doctor.username}")
        doctor_menu(doctor)
    else:
        print("Invalid username or password")
        

#after logging in as a doctor
def doctor_menu(doctor):
    print(f"Welcome, Dr. {doctor.username}!")
    print("1. View Patients")
    print("2. View Appointments")
    print("3. Add a Patient")
    print("4. Delete a Patient")
    print("5. Get Report")
    print("6. Update Appointment Status")
    print("7. Logout")
#after logging as doctor there are several options made avaibale to them
    choice = input("Please enter your choice:")

    if choice == "1":
        read_patients()
    elif choice == "2":
        read_appointments()
    elif choice == "3":
        add_patient()
    elif choice == "4":
        delete_patient()
    elif choice == "5":
        get_report()
    elif choice == "6":
        update_appointment_status()
    elif choice == "7":
        print("Logging out. Goodbye!")
    else:
        print("Invalid choice. Please try again")
        doctor_menu(doctor)


#doctor will be able to view the list of patients with the help of tabulate
def read_patients():
    patients = session.query(Patient).all()
    if patients:
        patient_data = []
        for patient in patients:
            patient_data.append([patient.id, patient.name, patient.age, patient.contact_info, patient.address])

        headers = ["Patient ID", "Name", "Age", "Contact Info", "Address"]
        print(tabulate(patient_data, headers=headers, tablefmt="grid"))
    else:
        print("No patients found.")



# Doctor can view the list of appointments with the help of tabulate
def read_appointments():
    appointments = session.query(Appointment).all()
    if appointments:
        appointment_data = [] #initialized an empty list to append details from the db
        for appointment in appointments:
            appointment_data.append([appointment.id, appointment.appointment_date, appointment.appointment_time, appointment.status])
#initialized headers and use tabulate to present the output nicely
        headers = ["Appointment ID", "Date", "Time", "Status"]
        print(tabulate(appointment_data, headers=headers, tablefmt="grid"))
    else:
        print("No appointments found.")



#function to add doctors via the command line.
def add_patient():
    #request for user inputs
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    contact_info = input("Enter patient's contact information: ")
    address = input("Enter patient's address: ")
#create an instance from user inputs and store them in database
    patient = Patient(name=name, age=age, contact_info=contact_info, address=address, appointments=None)
    session.add(patient)
    session.commit()
    print("Patient added successfully.")
    
#function to delete patient record by id
def delete_patient():
    patient_id = input("Enter the patient ID to delete: ")
#first() finds the id and stops from there
    patient = session.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        session.delete(patient)
        session.commit()
        print("Patient deleted successfully.")
    else:
         print("Patient not found.")
