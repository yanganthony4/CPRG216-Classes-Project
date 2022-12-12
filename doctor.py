class formatDrInfo:
    def __init__ (self, id, name, specialty, schedule, qualification, room_number):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.schedule = schedule
        self.qualification = qualification
        self.room_number = room_number
    
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
                doctor = formatDrInfo(line)
                doctors_list.append(doctor)

readDoctorsFile()