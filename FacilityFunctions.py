#FUNCTIONS/CLASSES

class FacilityInfo:
    def __init__(self,facilityname):
        self.facilityname = facilityname

    def __repr__(self):
        return f"{self.facilityname}"

    def __str__(self):
        return f"{self.facilityname}"

facilityfile = open ("/workspaces/Classes/data/pacilities.txt", "r")

totalFacilities = []

def formatFacilityInfo():
    
    for line in facilityfile:
        items = line.replace("\n","").split(" ")
        facility = FacilityInfo (items[0])
        totalFacilities.append(facility)
    return totalFacilities

def displayFacilityList():
    for i in range (0,len(totalFacilities)):
        print(totalFacilities[i])

def writeFacilityListToFile():
    new_facilityname = input ("Enter Facility name: ")
    edit_facility_file = open ("/workspaces/Classes/data/pacilities.txt", "a+")
    edit_facility_file.write(f"{new_facilityname}")
    edit_facility_file.close()
    return formatFacilityInfo()




#MENU

def facility_menu():
    facility_select = 1

    while facility_select > 0:
        print(f"Facility Menu\n0 - Return to Main Menu\n1 - Display Facilities List\n2 - Add Facility")
        facility_select = int(input("Enter Option: "))
        print("")

        if facility_select == 1:
            formatFacilityInfo()
            displayFacilityList()
            print("")

        if facility_select == 2:
            writeFacilityListToFile()
            print("")
    
facility_menu()
