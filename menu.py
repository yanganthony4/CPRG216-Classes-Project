# Anthony Yang, Kevin Huang, Kevin Liu, Vinh Huynh
# December 12, 2022

# Program is designed for Alberta Rural Patient Care (ARPC), it is data base that contains information
# on patients, doctors, facilities and labatories. Program contains a main menu which lets the user access
# the patients, doctors, faciities and labatory menus. When the user choses one of the 4 options (patients/doctors/facilities/labatories)
# they can have the option to veiw the list of every patient/doctor/facility/lab. The user can also edit the lists
# either by adding,removing or editing said lists. The program will continue to run until the user enters 0 to exit in the main menu.



# Function for main menu
def mainMenu():
    main_menu_option = 1

    # Filters option until "0" inputted by user which exits program
    while main_menu_option != 0:

        # Print instructions message and gets input from user
        print("Welcome to the Alberta Rural Patient Care Management System\n")
        print("Main Menu \n0 - Close application\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients")
        main_menu_option = int(input("Enter option: "))

        # Opens Doctor menu
        if main_menu_option == 1:
            import doctor

        # Opens Facility menu
        elif main_menu_option == 2:
            import facilities
    
        # Opens Laboratory menu
        elif main_menu_option == 3:
            import laboratory
        
        # Opens Patient menu
        elif main_menu_option == 4:
            import patient

mainMenu()