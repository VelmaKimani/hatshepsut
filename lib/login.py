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