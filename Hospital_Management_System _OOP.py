# ==========================================================
#                 Hospital Management System
"""
=========================================================
Problem Statement
=========================================================

Develop a Hospital Management System using Python.

Requirements

1. Add Patient
2. View Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Add Doctor
7. View Doctors
8. Book Appointment
9. Cancel Appointment
10. Add Medical Record
11. View Medical Records
12. Hospital Report
13. Exit

This project demonstrates the practical implementation
of Object-Oriented Programming (OOP) concepts.

=========================================================
"""


# ==========================================================
#                    MAIN MENU
# ==========================================================

print("=" * 55)
print("          Hospital Management System")
print("=" * 55)

print("1. Add Patient")
print("2. View Patients")
print("3. Search Patient")
print("4. Update Patient")
print("5. Delete Patient")
print("6. Add Doctor")
print("7. View Doctors")
print("8. Book Appointment")
print("9. Cancel Appointment")
print("10. Add Medical Record")
print("11. View Medical Records")
print("12. Hospital Report")
print("13. Exit")


# ==========================================================
#                  Patient Class
# ==========================================================

class Patient:

    # Constructor
    def __init__(self, patient_id, name, age, gender, phone, disease):

        # Instance Variables
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.disease = disease


    # Display Patient Information
    def display_info(self):

        print("\n========== Patient Details ==========")

        print("Patient ID :", self.patient_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Gender     :", self.gender)
        print("Phone      :", self.phone)
        print("Disease    :", self.disease)


    # Update Patient Information
    def update_info(self, name, age, gender, phone, disease):

        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.disease = disease

        print("Patient information updated successfully.")


# ==========================================================
#                  Doctor Class
# ==========================================================

class Doctor:

    # Constructor
    def __init__(self, doctor_id, name, specialization,
                 experience, fee, age, gender):

        # Instance Variables
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.experience = experience
        self.fee = fee
        self.age = age
        self.gender = gender


    # Display Doctor Information
    def display_info(self):

        print("\n========== Doctor Details ==========")

        print("Doctor ID      :", self.doctor_id)
        print("Name           :", self.name)
        print("Age            :", self.age)
        print("Gender         :", self.gender)
        print("Specialization :", self.specialization)
        print("Experience     :", self.experience, "Years")
        print("Fee            :", self.fee)


    # Update Doctor Information
    def update_info(self, name, specialization,
                    experience, fee, age, gender):

        self.name = name
        self.specialization = specialization
        self.experience = experience
        self.fee = fee
        self.age = age
        self.gender = gender

        print("Doctor information updated successfully.")


# ==========================================================
#               Appointment Class
# ==========================================================

class Appointment:

    # Constructor
    def __init__(self, appointment_id,
                 patient, doctor,
                 date, time):

        self.appointment_id = appointment_id
        self.patient = patient      # Patient Object
        self.doctor = doctor        # Doctor Object
        self.date = date
        self.time = time
        self.status = "Pending"


    # Book Appointment
    def book(self):

        self.status = "Booked"

        print("Appointment booked successfully.")


    # Cancel Appointment
    def cancel(self):

        self.status = "Cancelled"

        print("Appointment cancelled successfully.")


    # Display Appointment Details
    def display_info(self):

        print("\n========== Appointment ==========")

        print("Appointment ID :", self.appointment_id)
        print("Patient        :", self.patient.name)
        print("Doctor         :", self.doctor.name)
        print("Date           :", self.date)
        print("Time           :", self.time)
        print("Status         :", self.status)


# ==========================================================
#               Medical Record Class
# ==========================================================

class MedicalRecord:

    # Constructor
    def __init__(self,
                 record_id,
                 patient,
                 doctor,
                 diagnosis,
                 medicine,
                 notes):

        self.record_id = record_id
        self.patient = patient      # Patient Object
        self.doctor = doctor        # Doctor Object
        self.diagnosis = diagnosis
        self.medicine = medicine
        self.notes = notes


    # Display Medical Record
    def display_record(self):

        print("\n========== Medical Record ==========")

        print("Record ID :", self.record_id)
        print("Patient   :", self.patient.name)
        print("Doctor    :", self.doctor.name)
        print("Diagnosis :", self.diagnosis)
        print("Medicine  :", self.medicine)
        print("Notes     :", self.notes)
# ==========================================================
#                   Hospital Class
# ==========================================================

class Hospital:

    # Constructor
    def __init__(self):

        # Lists to store all objects
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.records = []


# ==========================================================
#                  Patient Methods
# ==========================================================

    # Add Patient
    def add_patient(self, patient):

        # Append patient object into list
        self.patients.append(patient)

        print("Patient added successfully.")


    # View All Patients
    def show_all_patients(self):

        if len(self.patients) == 0:

            print("No patient found.")

        else:

            for patient in self.patients:

                patient.display_info()


    # Search Patient
    def search_patient(self, patient_id):

        for patient in self.patients:

            if patient.patient_id == patient_id:

                return patient

        return None


    # Update Patient
    def update_patient(self, patient_id):

        patient = self.search_patient(patient_id)

        if patient:

            print("\nEnter New Information")

            name = input("Enter Name : ")
            age = int(input("Enter Age : "))
            gender = input("Enter Gender : ")
            phone = input("Enter Phone : ")
            disease = input("Enter Disease : ")

            patient.update_info(name, age, gender, phone, disease)

        else:

            print("Patient not found.")


    # Delete Patient
    def delete_patient(self, patient_id):

        patient = self.search_patient(patient_id)

        if patient:

            self.patients.remove(patient)

            print("Patient deleted successfully.")

        else:

            print("Patient not found.")


# ==========================================================
#                  Doctor Methods
# ==========================================================

    # Add Doctor
    def add_doctor(self, doctor):

        self.doctors.append(doctor)

        print("Doctor added successfully.")


    # View All Doctors
    def show_all_doctors(self):

        if len(self.doctors) == 0:

            print("No doctor found.")

        else:

            for doctor in self.doctors:

                doctor.display_info()


    # Search Doctor
    def search_doctor(self, doctor_id):

        for doctor in self.doctors:

            if doctor.doctor_id == doctor_id:

                return doctor

        return None


    # Update Doctor
    def update_doctor(self, doctor_id):

        doctor = self.search_doctor(doctor_id)

        if doctor:

            print("\nEnter New Doctor Information")

            name = input("Enter Name : ")
            specialization = input("Enter Specialization : ")
            experience = int(input("Enter Experience : "))
            fee = int(input("Enter Fee : "))
            age = int(input("Enter Age : "))
            gender = input("Enter Gender : ")

            doctor.update_info(
                name,
                specialization,
                experience,
                fee,
                age,
                gender
            )

        else:

            print("Doctor not found.")


    # Delete Doctor
    def delete_doctor(self, doctor_id):

        doctor = self.search_doctor(doctor_id)

        if doctor:

            self.doctors.remove(doctor)

            print("Doctor deleted successfully.")

        else:

            print("Doctor not found.")


# ==========================================================
#               Appointment Methods
# ==========================================================

    # Book Appointment
    def book_appointment(self, appointment):

        self.appointments.append(appointment)

        appointment.book()


    # View Appointments
    def show_appointments(self):

        if len(self.appointments) == 0:

            print("No appointments available.")

        else:

            for appointment in self.appointments:

                appointment.display_info()


    # Cancel Appointment
    def cancel_appointment(self, appointment_id):

        for appointment in self.appointments:

            if appointment.appointment_id == appointment_id:

                appointment.cancel()

                return

        print("Appointment not found.")


# ==========================================================
#             Medical Record Methods
# ==========================================================

    # Add Medical Record
    def add_medical_record(self, record):

        self.records.append(record)

        print("Medical record added successfully.")


    # View Medical Records
    def show_medical_records(self):

        if len(self.records) == 0:

            print("No medical record found.")

        else:

            for record in self.records:

                record.display_record()


# ==========================================================
#                Hospital Report
# ==========================================================

    # Display Overall Report
    def hospital_report(self):

        print("\n========== Hospital Report ==========")

        print("Total Patients      :", len(self.patients))
        print("Total Doctors       :", len(self.doctors))
        print("Total Appointments  :", len(self.appointments))
        print("Total Medical Files :", len(self.records))

# ==========================================================
#                Main Program Starts Here
# ==========================================================

# Hospital class ka object create kiya
hospital = Hospital()

# Infinite loop jab tak user Exit select na kare
while True:

    print("\n" + "=" * 50)
    print("       Hospital Management System")
    print("=" * 50)

    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. View Doctors")
    print("8. Book Appointment")
    print("9. Cancel Appointment")
    print("10. Add Medical Record")
    print("11. View Medical Records")
    print("12. Hospital Report")
    print("13. Exit")

    # User se menu choice lena
    choice = input("\nEnter Your Choice : ")


# ==========================================================
#                     OPTION 1
#                    Add Patient
# ==========================================================

    if choice == "1":

        # Patient ki information lena
        patient_id = input("Enter Patient ID : ")
        name = input("Enter Patient Name : ")
        age = int(input("Enter Age : "))
        gender = input("Enter Gender : ")
        phone = input("Enter Phone Number : ")
        disease = input("Enter Disease : ")

        # Patient object create karna
        patient = Patient(
            patient_id,
            name,
            age,
            gender,
            phone,
            disease
        )

        # Hospital list me add karna
        hospital.add_patient(patient)


# ==========================================================
#                     OPTION 2
#                   View Patients
# ==========================================================

    elif choice == "2":

        hospital.show_all_patients()


# ==========================================================
#                     OPTION 3
#                  Search Patient
# ==========================================================

    elif choice == "3":

        patient_id = input("Enter Patient ID : ")

        # Patient search karna
        patient = hospital.search_patient(patient_id)

        if patient:

            patient.display_info()

        else:

            print("Patient Not Found.")


# ==========================================================
#                     OPTION 4
#                  Update Patient
# ==========================================================

    elif choice == "4":

        patient_id = input("Enter Patient ID : ")

        hospital.update_patient(patient_id)


# ==========================================================
#                     OPTION 5
#                  Delete Patient
# ==========================================================

    elif choice == "5":

        patient_id = input("Enter Patient ID : ")

        hospital.delete_patient(patient_id)
# ==========================================================
#                     OPTION 6
#                     Add Doctor
# ==========================================================

    elif choice == "6":

        # Doctor ki information lena
        doctor_id = input("Enter Doctor ID : ")
        name = input("Enter Doctor Name : ")
        specialization = input("Enter Specialization : ")
        experience = int(input("Enter Experience (Years) : "))
        fee = int(input("Enter Doctor Fee : "))
        age = int(input("Enter Age : "))
        gender = input("Enter Gender : ")

        # Doctor object create karna
        doctor = Doctor(
            doctor_id,
            name,
            specialization,
            experience,
            fee,
            age,
            gender
        )

        # Doctor ko hospital list me add karna
        hospital.add_doctor(doctor)


# ==========================================================
#                     OPTION 7
#                    View Doctors
# ==========================================================

    elif choice == "7":

        # Sare doctors show karna
        hospital.show_all_doctors()


# ==========================================================
#                     OPTION 8
#                  Book Appointment
# ==========================================================

    elif choice == "8":

        # Patient aur Doctor ID lena
        patient_id = input("Enter Patient ID : ")
        doctor_id = input("Enter Doctor ID : ")

        # Search methods call karna
        patient = hospital.search_patient(patient_id)
        doctor = hospital.search_doctor(doctor_id)

        # Dono exist karte hain ya nahi check karna
        if patient and doctor:

            appointment_id = input("Enter Appointment ID : ")
            date = input("Enter Appointment Date : ")
            time = input("Enter Appointment Time : ")

            # Appointment object create karna
            appointment = Appointment(
                appointment_id,
                patient,
                doctor,
                date,
                time
            )

            # Appointment book karna
            hospital.book_appointment(appointment)

        else:

            print("Patient or Doctor Not Found.")


# ==========================================================
#                     OPTION 9
#                Cancel Appointment
# ==========================================================

    elif choice == "9":

        appointment_id = input("Enter Appointment ID : ")

        # Appointment cancel method call
        hospital.cancel_appointment(appointment_id)
# ==========================================================
#                     OPTION 10
#                Add Medical Record
# ==========================================================

    elif choice == "10":

        # Patient aur Doctor ID lena
        patient_id = input("Enter Patient ID : ")
        doctor_id = input("Enter Doctor ID : ")

        # Patient aur Doctor search karna
        patient = hospital.search_patient(patient_id)
        doctor = hospital.search_doctor(doctor_id)

        # Agar dono mil jaye to record add karo
        if patient and doctor:

            record_id = input("Enter Record ID : ")
            diagnosis = input("Enter Diagnosis : ")
            medicine = input("Enter Medicine : ")
            notes = input("Enter Notes : ")

            # MedicalRecord object create karna
            record = MedicalRecord(
                record_id,
                patient,
                doctor,
                diagnosis,
                medicine,
                notes
            )

            # Hospital ke records list me add karna
            hospital.add_medical_record(record)

        else:

            print("Patient or Doctor Not Found.")


# ==========================================================
#                     OPTION 11
#              View Medical Records
# ==========================================================

    elif choice == "11":

        # Sare medical records display karna
        hospital.show_medical_records()


# ==========================================================
#                     OPTION 12
#                 Hospital Report
# ==========================================================

    elif choice == "12":

        # Total patients, doctors, appointments aur records show karna
        hospital.hospital_report()


# ==========================================================
#                     OPTION 13
#                        Exit
# ==========================================================

    elif choice == "13":

        print("\nThank you for using Hospital Management System.")
        print("Program Closed Successfully.")

        # While loop se bahar nikalna
        break


# ==========================================================
#                 Invalid Choice
# ==========================================================

    else:

        print("Invalid Choice. Please Try Again.")
























#Hospital managemnet system

print("1. ADD patient")
print("2. view patints")
print("3. seach pateint")
print("4. update patient")
print("5. delete pateint")
print("6. add doctor")
print("7. views doctor")
print("8. book appointement")
print("9. cancel appointement")
print("10. add medical record")
print("11. view medical record")
print("12.hospital report")
print("13.exit")

class Patient:
    def __init__(self, patient_id, name, age, gender, phone, disease):
        self.patient_id = patient_id
        self.name    = name
        self.age     = age
        self.gender  = gender
        self.phone   = phone
        self.disease = disease
    def display_info(self):
       print ("Patient_ID :" , self.patient_id)
       print ("Patient_name" ,self.name)
       print ("patient_age",  self.age)
       print ("Pateint_gender", self.gender)
       print("patient_phone",  self.phone)
       print("patient_disease",  self.disease)
    def update_info(self,patient_id,name,age,gender,phone,disease ):
        self.patient_id = patient_id
        self.name    = name
        self.age     = age
        self.gender  = gender
        self.phone   = phone
        self.disease = disease
        print("patient information updated")

class Doctor:
    def __init__(self,doctor_id,name,specalization,experience,fee,age,gender):
        self.doctor_id     = doctor_id
        self.name          = name
        self.specalization = specalization
        self.experience    =  experience
        self.fee           = fee
        self.age    = age
        self.gender= gender
    
    def display_info(self) :
        print("DoctoR_id"        , self.doctor_id )
        print("doctor_name"      , self.name)
        print("dr_specalization" , self.specalization)
        print("dr_experience"    , self.experience)
        print("dr_fee "          , self.fee)

    def update_info(self,doctor_id,name,specalization,experience,fee):
        self.doctor_id     = doctor_id
        self.name          = name
        self.specalization = specalization
        self.experience    =  experience
        self.fee           = fee
         
class Appointment :
    def __init__(self,appointment_id,patient,doctor,date, time, status):
        self.appointment_id  =  appointment_id
        self.patient  =      patient
        self.doctor   =     doctor
        self.date     =    date
        self.time     =     time 
        self.status   =    status
    def book(self):
      self.status="booked"
      print ("appointment booked ")
         
    def cancel(self):
      self.status="cancelled"
      print("appointement cancel successfully")
    def show_details(self):
        print("appointment_id" , self.appointment_id)
        print("patient" , self.patient)
        print("doctor"   , self.doctor)
        print("date"  , self.date)
        print("Time :", self.time)
        print("status" , self.status)

class MedicalRecord :
    def __init__(self,record_id,patient,doctor,diagnosis,medicine,notes,):
      self.record_id = record_id
      self.patient = patient
      self.doctor  =doctor
      self.diagnosis =diagnosis
      self.medicine=medicine
      self.notes=notes
    def add_record(self):
          print("record added")
    def show_record(self) :
        print("record_id:", self.record_id )
        print("patient"   ,  self.patient)
        print("doctor"    ,self.doctor)
        print("diagnosis" , self.diagnosis)
        print("medicine" , self.medicine)
        print("notes"    , self.notes)

class Hospital:
   def __init__(self):
      self.patients = []
      self.doctors = []
      self.appointments = []
      self.records = []
   def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfull")

   def show_all_patients(self):
        for patient in self.patients:
            patient.display_info()

   def search_patient(self, patient_id):
    for patient in self.patients:
        if patient.patient_id == patient_id:
            return patient
    return None
            
   def remove_patient(self, patient_id):
    patient = self.search_patient(patient_id)
    if patient:
        self.patients.remove(patient)
        print("Patient removed successfully")
    else:
        print("Patient not found")

   def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print("Doctor added successful.")

   def show_all_doctors(self):
      for doctor in self.doctors:
        doctor.display_info()
    
   def search_doctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor 
                
   def book_appointment(self, appointment):
        self.appointments.append(appointment)
        appointment.book()

   def cancel_appointment(self, appointment_id):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.cancel()
        print("Appointment cancel")   

hospital=Hospital()
while True:
 choice = input("Enter Your Choice : ")
 if choice == "1":
        patient_id = input("Enter Patient ID")
        name = input("Enter Name")
        age = int(input("Enter Age"))
        gender = input("Enter Gender")
        phone = input("Enter Phoone ")
        disease = input("Enter Disease ")
        patient = Patient(patient_id,name,age,gender,phone,disease)
        hospital.add_patient(patient)
 elif choice == "2":
    hospital.show_all_patients()
 elif choice == "3":
        patient_id = input("Enter Patient id ")
        patient = hospital.search_patient(patient_id)
        if patient:
            patient.display_info()
        else:
            print("Patient Not Found")
 elif choice == "4":
        patient_id = input("Enter Patient ID ")
        patient = hospital.search_patient(patient_id)
 elif choice == "5":
        patient_id = input("Enter Patient ID")
        hospital.remove_patient(patient_id)
 elif choice == "6":
        doctor_id = input("Enter Doctor ID ")
        name = input("Enter Doctor Name ")
        age = int(input("Enter Age  " ))
        gender = input("Enter Gender ")
        specialization = input("Enter Specialization  ")
        experience = int(input("Enter Experience "))
        fee = int(input("Enter Fee "))
        doctor = Doctor(doctor_id, name, age, gender, specialization, experience, fee,)
        hospital.add_doctor(doctor)
 elif choice=="7":
      hospital.show_all_doctors()
 elif choice=="8":
        doctor_id = input("Enter doctor id ")
        doctor = hospital.search_patient(doctor_id)
        if doctor:
            doctor.display_info()
        else:
            print("doctor Not Found")
 elif choice=="9":
        doctor_id = input("Enter doctor ID ")
        doctor = hospital.search_doctor(doctor_id)
 elif choice =="10" :
        doctor_id = input("Enter docto ID")
        doctor.remove_doctor(doctor_id)
 elif choice =="11" :
        appointment_id = input("Enter Appointment ID : ")
        hospital.cancel_appointment(appointment_id)
 elif choice== "12" :
     patient_id=input("enter the patient id")
     doctor_id=input("enter the doctor id")
     record_id=input("enter the record ID")
     if patient and doctor:

            diagnosis = input("Enter Diagnosis : ")
            medicine = input("Enter Medicine : ")
            notes = input("Enter Notes : ")

            record = MedicalRecord(record_id,patient,doctor,diagnosis,medicine,notes)
            hospital.add_medical_record(record)
     else:
            print("Patient or Doctor Not Found")
 elif choice == "11":
         hospital.show_medical_record()
 elif choice == "12":
        hospital.hospital_report()
 elif choice == "13":
        print("Invalid Choice")