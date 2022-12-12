class formatDrInfo:
    def __init__ (self, id, name, speciality, schedule, qualification, room_number):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.schedule = schedule
        self.qualification = qualification
        self.room_number = room_number
        
    # Formatting string representation for printing of results
    def __str__(self):
        return f'{self.id:<4s}  {self.name:<14s}  {self.speciality:<20s}  {self.schedule:<10s}  {self.qualification:<15s}  {self.room_number:<15s}'
    
    # Formatting representation in later list.
    def __repr__(self):
        return f'{self.id} {self.name} {self.speciality} {self.schedule} {self.qualification} {self.room_number}'

def doctorsMenu():
    option = 1
    doctors_list = readDoctorsFile()
    while option != 0:
        print("\nDoctor's Menu")
        print("0 - Return to Main Menu\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info")
        option = int(input("Enter option: "))
        print("\n")
        if option == 1:
            displayDoctorsList(doctors_list)
        elif option == 2:
            doctor = [0, 0]
            doctor[0], doctor[1] = searchDoctorById(doctors_list)
            neg_one = -1
            if doctor[0] == neg_one:
                print("Patient with ID " + doctor[1] + " not in patient file")
            else:
                print(doctor[0])
        elif option == 3:
            doctor = [0, 0]
            doctor[0], doctor[1] = searchDoctorByName(doctors_list)
            neg_one = -1
            if doctor[0] == neg_one:
                print("Patient with name " + doctor[1] + " not in patient file")
            else:
                print(doctor[0])
        elif option == 4:
            doctor = enterDrInfo()
            addDrToList(doctor,doctors_list)
        elif option == 5:
            editDoctorInfo(doctors_list)
            displayDoctorsList(doctors_list)

def enterDrInfo():
    id = input("Enter Dr ID: ")
    name = input("Enter Dr name: ")
    spec = input("Enter Dr speciality: ")
    sched = input("Enter Dr schedule: ")
    qual = input("Enter Dr qualifications: ")
    room = input("Enter Dr room number: ")
    doctor = formatDrInfo(id, name, spec, sched, qual, room)
    return doctor

def readDoctorsFile():
    with open('data\doctors.txt', 'r') as file:
        doctors_list = []
        for line in file:
            if not line.isspace():
                line = line.replace("\n","").split("_")
                doctor = formatDrInfo(line[0], line[1], line[2], line[3], line[4], line[5])
                doctors_list.append(doctor)
    return doctors_list

def searchDoctorById(doctors_list):
    search_id = input("Enter the doctor ID: ")
    for doctor in doctors_list:
        if doctor.id == search_id:
            return doctor, search_id
    return -1, search_id

def searchDoctorByName(doctors_list):
    search_name = input("Enter the doctor name: ")
    for doctor in doctors_list:
        if doctor.name == search_name:
            return doctor, search_name
    return -1, search_name

def editDoctorInfo(doctors_list):
    doctor = [0, 0]
    doctor[0], doctor[1] = searchDoctorById(doctors_list)
    neg_one = -1
    if doctor[0] == neg_one:
        print("Patient with name " + doctor[1] + " not in patient file")
    else:
        print(doctor[0])
        doctor_edit = doctor[0]
        doctor_edit.name = input("Enter new name: ")
        doctor_edit.speciality = input("Enter new speciality in: ")
        doctor_edit.schedule = input("Enter new schedule: ")
        doctor_edit.qualification = input("Enter new qualifications: ")
        doctor_edit.room_number = input("Enter new room number: ")
        return doctor_edit

def displayDoctorsList(doctors_list):
    for doctor in doctors_list:
        print(doctor)
    
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