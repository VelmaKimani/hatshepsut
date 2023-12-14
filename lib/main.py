import datetime
import sqlalchemy
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String,VARCHAR, Date, ForeignKey,Time
from faker import Faker
import random


Base = declarative_base()

#class patient and its attribute
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age= Column(String)
    contact_info = Column(VARCHAR)
    address= Column(String)
    appointments = relationship("Appointment", back_populates="patient")

    def __init__(self, name, age, contact_info, address, appointments):
        self.name=name
        self.age=age
        self.contact_info=contact_info
        self.address=address
       

    def __rep__(self):
        return f"{self.name}"

#class appointment and its attribute
class Appointment(Base):
    #appointment table and some of its attribute
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    status = Column(String)
    appointment_type = Column(String)  # Add the appointment_type attribute
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")