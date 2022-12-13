class formatDrInfo:
    # Initialize the class.
    def __init__ (self, id, name, speciality, schedule, qualification, room_number):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.schedule = schedule
        self.qualification = qualification
        self.room_number = room_number
        
    # Formatting string representation for printing of results.
    def __str__(self):
        return f'{self.id:<4s}  {self.name:<14s}  {self.speciality:<20s}  {self.schedule:<10s}  {self.qualification:<15s}  {self.room_number:<15s}'
    
    # Formatting representation in later list.
    def __repr__(self):
        return f'{self.id} {self.name} {self.speciality} {self.schedule} {self.qualification} {self.room_number}'

def doctorsMenu():
    # Reads doctor list from external save file.
    option = 1
    doctors_list = readDoctorsFile()

    # Displays menu continuously until requested stop.
    while option != 0:

        # Displays options and retrieve option input.
        print("\nDoctor's Menu")
        print("0 - Return to Main Menu\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info")
        option = int(input("Enter option: "))
        print("\n")

        # Displays doctor list.
        if option == 1:
            displayDoctorsList(doctors_list)

        # Search Doctor by ID.
        elif option == 2:

            # Initial configurations and conducting search doctor function.
            doctor = [0, 0]
            doctor[0], doctor[1] = searchDoctorById(doctors_list)
            neg_one = -1

            # 'Not found' message if search function returns '-1', Otherwise just prints found patient.
            if doctor[0] == neg_one:
                print("Doctor with ID " + doctor[1] + " not in doctor file")
            else:
                print(doctor[0])
        
        # Search Doctor by Name.
        elif option == 3:

            # Initial configurations and conducting search doctor function.
            doctor = [0, 0]
            doctor[0], doctor[1] = searchDoctorByName(doctors_list)
            neg_one = -1

            # 'Not found' message if search function returns '-1', Otherwise just prints found patient.
            if doctor[0] == neg_one:
                print("Doctor with name " + doctor[1] + " not in doctor file")
            else:
                print(doctor[0])
        
        # Adds doctor to doctor list.
        elif option == 4:

            # Retrieves doctor object.
            doctor = enterDrInfo()

            # Adds doctor object to doctor list.
            addDrToList(doctor,doctors_list)

        # Edit doctor in doctor list.
        elif option == 5:
            # Edit doctor info function.
            editDoctorInfo(doctors_list)

            # Displays doctor list
            displayDoctorsList(doctors_list)
    writeDoctorsListToFile(doctors_list)

# Enter doctor info function.
def enterDrInfo():

    # Retrieve user inputs for doctor info.
    id = input("Enter Dr ID: ")
    name = input("Enter Dr name: ")
    spec = input("Enter Dr speciality: ")
    sched = input("Enter Dr schedule: ")
    qual = input("Enter Dr qualifications: ")
    room = input("Enter Dr room number: ")\

    # Creates new doctor object and returns it.
    doctor = formatDrInfo(id, name, spec, sched, qual, room)
    return doctor

# Read doctor info from external save function.
def readDoctorsFile():
    # Opens external save file.
    with open('data\doctors.txt', 'r') as file:
        doctors_list = []

        # Iterates through every line and filters out empty lines.
        for line in file:
            if not line.isspace():
                
                # Restructures each line and puts it into a list before creating a new object that gets put into another list.
                line = line.replace("\n","").split("_")
                doctor = formatDrInfo(line[0], line[1], line[2], line[3], line[4], line[5])
                doctors_list.append(doctor)

    return doctors_list

# Search doctor by ID function.
def searchDoctorById(doctors_list):

    # Retrieves requested search ID.
    search_id = input("Enter the doctor ID: ")

    # Searches for doctor in the list and returns the doctor.
    for doctor in doctors_list:
        if doctor.id == search_id:
            return doctor, search_id
    
    # If doctor is not found, then returns '-1' value.
    return -1, search_id

# Search doctor by name function.
def searchDoctorByName(doctors_list):

    # Retrieves request search name.
    search_name = input("Enter the doctor name: ")

    # Searches for doctor in the list and returns the doctor.
    for doctor in doctors_list:
        if doctor.name == search_name:
            return doctor, search_name

    # If doctor is not found, then returns '-1' value.
    return -1, search_name

# Edit doctor function.
def editDoctorInfo(doctors_list):

    # Initial configurations and conducting search doctor function.
    doctor = [0, 0]
    doctor[0], doctor[1] = searchDoctorById(doctors_list)
    neg_one = -1

     # 'Not found' message if search function returns '-1', Otherwise just prints found patient and proceeds to edit.
    if doctor[0] == neg_one:
        print("Patient with name " + doctor[1] + " not in patient file")
    else:
        print(doctor[0])

        # Prints patient and makes edits to the patient object before returning the object.
        doctor_edit = doctor[0]
        doctor_edit.name = input("Enter new name: ")
        doctor_edit.speciality = input("Enter new speciality in: ")
        doctor_edit.schedule = input("Enter new schedule: ")
        doctor_edit.qualification = input("Enter new qualifications: ")
        doctor_edit.room_number = input("Enter new room number: ")
        return doctor_edit

# Display doctors list.
def displayDoctorsList(doctors_list):

    # Prints each line.
    for doctor in doctors_list:
        print(doctor)
    
# Writes 
def writeDoctorsListToFile(doctors_list):
    f = open("data\doctors.txt")
    f.truncate(0)

    for doctor in doctors_list:
        doctors_write_list = []
        doctors_write_list.append(doctor.id)
        doctors_write_list.append(doctor.name)
        doctors_write_list.append(doctor.speciality)
        doctors_write_list.append(doctor.schedule)
        doctors_write_list.append(doctor.qualifications)
        doctors_write_list.append(doctor.room_number)
        f.write("_".join(doctors_write_list))

def addDrToList(doctor, doctors_list):
    doctors_list.append(doctor)
    return(doctors_list)

doctorsMenu()