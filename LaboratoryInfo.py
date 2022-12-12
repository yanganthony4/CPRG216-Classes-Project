class formatLabInfo:

    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def __str__(self):
        return f'{self.lab_name:<20s} {self.cost:>10s}'

    def __repr__(self):
        return f'{self.lab_name}{self.cost}'

def readLaboratoriesFile(formatLabInfo):
    with open('data\laboratories.txt', 'r') as file:
        labs_list = []

        for line in file:
            if not line.isspace():

                lab_info = line.replace('\n', '').split('_')
                lab = formatLabInfo(lab_info[0], lab_info[1])
                labs_list.append(lab)

    return labs_list

def displayLabsList(labs_list):
    print("\n")

    for i in labs_list:
        print(i)

def enterLaboratoryInfo():
    lab_name = input("\nEnter Lab Name: ")
    cost = input("Enter Lab Cost: ")

    lab = formatLabInfo(lab_name, cost)
    return lab

def writeLabsListToFile(labs_list):
    f = open('data\laboratories.txt', 'a')
    f.truncate(0)

    for i in labs_list:
        write_labs_list = []
        write_labs_list.append(i.lab_name)
        write_labs_list.append(i.cost)
        write_labs_list.append('\n')
        f.write('_'.join(write_labs_list))

def addLabtoList(lab, labs_list):
    labs_list.append(lab)
    return labs_list

def laboratoriesMenu():
    print('\nLaboratory Menu')
    print('0 - Return to Main Menu \n1 - Display laboratories list \n2 - Add laboratory')

    labs_option = int(input('Enter option: '))
    return labs_option

labs_option = 1
labs_list = readLaboratoriesFile(formatLabInfo)

while labs_option != 0:
    labs_option = laboratoriesMenu()

    if labs_option == 1:
        displayLabsList(labs_list)
    
    elif labs_option == 2:
        new_lab = enterLaboratoryInfo()
        addLabtoList(new_lab, labs_list)

writeLabsListToFile(labs_list)