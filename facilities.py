#FUNCTIONS/CLASSES

#Creating a facility Class
class FacilityInfo:
    def __init__(self,facilityname):
        self.facilityname = facilityname

    def __repr__(self):
        return f"{self.facilityname}"
#Formats facility information (attributes)- for display
    def __str__(self):
        return f"{self.facilityname}"

facilityfile = open ("data/pacilities.txt", "r")
totalFacilities = []

#Takes information from facility text and puts them into a list
def formatFacilityInfo():
    
    for line in facilityfile:
        items = line.split("\n")
        facility = FacilityInfo (items[0])
        totalFacilities.append(facility)
    return totalFacilities

#Display all facilities on the terminal 
def displayFacilityList():
    for i in range (0,len(totalFacilities)):
        print(totalFacilities[i])

#Formats all the list of facilities back into facilities.txt file
def writeFacilityListToFile():
    new_facilityname = input ("Enter Facility name: ")
    edit_facility_file = open ("data/pacilities.txt", "a+")
    edit_facility_file.write(f"{new_facilityname}")
    edit_facility_file.close()
    return formatFacilityInfo()




#MENU

def facility_menu():
    facility_select = 1

    while facility_select > 0:
        print(f"\nFacility Menu\n0 - Return to Main Menu\n1 - Display Facilities List\n2 - Add Facility")
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
