# Creation of Patient class
class PatientInfo:

    # Initialization with patient's characterization
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age

    # Formatting string representation for printing of results
    def __str__(self):
        return f'{self.id:<4s}  {self.name:<14s}  {self.diagnosis:<14s}  {self.gender:<10s}  {self.age:<10s}'
    
    # Formatting representation in later list.
    def __repr__(self):
        return f'{self.id} {self.name} {self.diagnosis} {self.gender} {self.age}'

# Function for main patient menu for selecting options
def patientsMenu():

    # Printing out 
    print("\nPatient Menu")
    print("0 - Return to Main Menu \n1 - Display patient's list \n2 - Search for patient by ID \n3 - Add patient \n4 - Edit patient info")
    
    # Input for option choice and returns it
    option = int(input(("Enter option: ")))
    return option

# Function for entering in a new patient
def enterPatientInfo():

    # Inputs for patients characteristics
    id = input("\nEnter Patient ID: ")
    name = input("Enter Patient name: ")
    diagnosis = input("Enter Patient diagnosis: ")
    gender = input("Enter Patient gender: ")
    age = input("Enter Patient age: ")

    # Creates new object and returns object
    patient = PatientInfo(id, name, diagnosis, gender, age)
    return patient

# Function for reading save file in data folder
def readPatientsFile(PatientInfo):

    # Opens and reads file, sets up empty list of patients
    with open('data\patients.txt', 'r') as file:
        patients_list = []

        # Takes each line in the file and filters out empty lines
        for line in file:
            if not line.isspace():

                # For each line delete the newlines and create a list splitting using the underscores
                line = line.replace("\n", "").split("_")

                # Creates new object and then adds to end of a list, returning it 
                patient = PatientInfo(line[0], line[1], line[2], line[3], line[4])
                patients_list.append(patient)
        return patients_list

# Function for searching a patient by ID
def searchPatientById(patients_list):

    # Gets ID input and then filter through the ID attribute of the object list before returning it
    search_id = input("\nEnter the Patient ID: ")
    for patient in patients_list:
        if patient.id == search_id:
            return patient
    
    # Returns "not found" message if no ID is matched
    return "Patient with ID " + search_id + " not in patient file"

# Function for editing existing patients
def editPatientInfo(patients_list):

    # Use earlier created search function to find the desired patient info to edit, prints result
    patient = searchPatientById(patients_list)
    print(patient)

    # Gathers inputs for new data and updates objects attributes
    patient.name = input("Enter new Name: ")
    patient.diagnosis = input("Enter new diagnosis: ")
    patient.gender = input("Enter new gender: ")
    patient.age = input("Enter new age: ")
    return patient

# Function for displaying patient list
def displayPatientsList(patients_list):
    print("\n")

    # Each object in the list will get printed
    for i in patients_list:
        print(i)

# Function for saving the current patient list to an external .txt file in data folder
def writePatientsListToFile(patients_list):

    # Opens folder and clears content before writing
    f = open("data\patients.txt","a")
    f.truncate(0)

    # For each object, gather the attributes into a list and then write into the .txt file
    for i in patients_list:
        patients_write_list = []
        patients_write_list.append(i.id)
        patients_write_list.append(i.name)
        patients_write_list.append(i.diagnosis)
        patients_write_list.append(i.gender)
        patients_write_list.append(i.age)
        patients_write_list.append("\n")

        # Joins together list separating each object with an underscore, before writing into the .txt file
        f.write("_".join(patients_write_list))

# Function for adding patient into the list
def addPatientToList(patient, patients_list):
    patients_list.append(patient)
    return patients_list

# Setting initial options value and retrieves patient list from a save file in the data folder
option = 1
patients_list = readPatientsFile(PatientInfo)

# Filtering of options until "0" inputted by user
while option != 0:
    option = patientsMenu()
    
    # Displays patient list
    if option == 1:
        displayPatientsList(patients_list)

    # Searches for patient by ID
    elif option == 2:
        print(searchPatientById(patients_list))

    # Enter in new patient data
    elif option == 3:
        new_patient = enterPatientInfo()
        addPatientToList(new_patient, patients_list)

    # Edit existing patient data
    elif option == 4:
        editPatientInfo(patients_list)
        displayPatientsList(patients_list)

# Updates save file after data entry finished
writePatientsListToFile(patients_list)




