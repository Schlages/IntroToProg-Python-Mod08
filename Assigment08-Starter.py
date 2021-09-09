# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Brandon Schlagel,9/6/2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #

"""Stores data about a product:

    properties:
        iproduct: (string) with the products  name
        iprice: (float) with the products standard price
        lstTable: list of products to be saved to file
        strStatus: Captures the status of an processing functions
        choice: choice number user selects
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Brandon Schlagel,9/7/2021, Modified code to complete assignment 8
    """
strFileName = 'products.txt'
lstTable = []
strStatus = ""
choice = ""
iprice = ""
iproduct = ""

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, lstTable):

        read_data_from_file(strFileName): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Brandon Schlagel,9/7/2021,Modified code to complete assignment 8
    """

    @staticmethod
    def read_data_from_file(strFileName):
        with open(strFileName, 'r') as file:
            return file.read()

    @staticmethod
    def save_data_to_file(strFileName, lstTable):
        objFile = open(strFileName, "a")
        for row in lstTable:
            objFile.write(row["Product"] + "," + row["Price"] + '\n')
        return lstTable, 'Success'

    @staticmethod
    def add_data_to_list(iproduct, iprice, lstTable):
        list_of_rows = {"Product": iproduct, "Price": iprice}
        lstTable.append(list_of_rows)
        return list_of_rows, 'Success'


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
        create input commands that output different results depending on user choice:
    methods:
        print_menu_Tasks: show menu option (1-3)
        input_menu_choice: select menu option (1-3)
        print_current_Tasks_in_list(lstTable): Show tasks in table list, not text file
        input_new_product_and_price: input product and price
        input_press_to_continue(optional_message='')
        input_yes_no_choice(message):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Brandon Schlagel,9/7/2021,Modified code to complete assignment 8
    """


    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
            Menu of Options
            1) Add a Product
            2) Save Data to File & exit program       
            3) Print current list of data
            ''')
        print()


    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice


    @staticmethod
    def print_current_Tasks_in_list(lstTable):
        """ Shows the current Tasks in the list of dictionaries rows

        :param lstTable: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Products are: *******")
        for row in lstTable:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks


    @staticmethod
    def input_new_product_and_price():
        iproduct = input("Input product: ")
        iprice = input("Input price: ")
        return iproduct, iprice

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()


# Presentation (Input/Output)  -------------------------------------------- #
# Load data from file into a list of product objects when script starts
f = FileProcessor()  # create an object
print(f.read_data_from_file("products.txt"))  # use its method

# Main Body of Script  ---------------------------------------------------- #


# Display a menu of choices to the user
while (True):
    # Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        iproduct, iprice = IO.input_new_product_and_price()
        FileProcessor.add_data_to_list(iproduct, iprice, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Save Data to File

        strChoice = IO.input_yes_no_choice("Save this data to file and exit? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
            break
        elif strChoice.lower() =="n":
            print("Cancelled!")
            continue
        if strChoice.lower() != "y" or strChoice.lower() != "n":
            raise Exception("Please type y or n!")
        continue
       #  else:
       #     IO.input_press_to_continue("Save Cancelled!")
        continue

    elif strChoice == '3':  # Load current list
        strChoice = IO.input_yes_no_choice("Would you like to see what is currently in your list? (y/n) -  ")
        if strChoice.lower() == 'y':
            IO.print_current_Tasks_in_list(lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Cancelled!")
        continue  # to show the menu



