class formatDrInfo:
    def __init__ (self, id, name, speciality, schedule, qualification, room_number):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.schedule = schedule
        self.qualification = qualification
        self.room_number = room_number

def doctorsMenu():
    print("Doctor's Menu")
    print("0 - Return to Main Menu\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info")
    option = 1
    doctors_list = readDoctorsFile()
    while option != 0:
        option = int(input("Enter option: "))
        if option == 1:
            displayDoctorsList(doctors_list)
        elif option == 2:
            searchDoctorById(doctors_list)
        elif option == 3:
            searchDoctorByName(doctors_list)
            
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
    search_id = int(input("Enter the doctor ID: "))
    for doctor in doctors_list:
        if doctor.id == search_id:
            return doctor
    return "Doctor with ID " + search_id + " not in doctor file"

def searchDoctorByName(doctors_list):
    search_name = input("Enter the doctor name: ")
    for doctor in doctors_list:
        if doctor.name == search_name:
            return doctor
    return "Doctor with name " + search_name + " not in doctor file"

def editDoctorInfo(doctors_list):
    doctor = searchDoctorById(doctors_list)
    print(doctor)

    doctor.name = input("Enter new name: ")
    doctor.speciality = input("Enter new speciality in: ")
    doctor.schedule = input("Enter new schedule: ")
    doctor.qualification = input("Enter new qualifications: ")
    doctor.room_number = input("Enter new room number: ")
    return doctor

def displayDoctorsList(doctors_list):
    print("\n")
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

option = 1
doctors_list = readDoctorsFile()

while option != 0:
    option = doctorsMenu