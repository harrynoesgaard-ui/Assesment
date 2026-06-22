# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = "steam_loco's.db"


def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()



"""Code for the menu interface"""
choice =''
while choice != 'z':
    choice = input('Welcome to the steam locomotive database\n\n'
                     'select what you want to chose\n'
                     'A: Age and built date\n' 
                     'B: Whyte and boiler\n'
                     'C: Locomotive, nickname, and current owner\n'
                     'D: Built, Manufacture, and nickname\n' 
                     "E: American locomotive Company Loco's\n" 
                     "F: Baldwin Locomotive Works Loco's\n" 
                     "G: Locomotives with boilers longer than 20 feet\n" 
                     "H: Locomotives built before 1920\n" 
                     "Z: Exit the database \n\n Type here: ")
    #outcomes for each button press
    choice = choice.lower()
    if choice == 'a':
        print_query('age_and_built_date')
    elif choice == 'b':
        print_query('whyte_and_boiler')
    elif choice == 'c':
        print_query('locomotive_owner')
    elif choice == 'd':
        print_query('nickname_manufactuer')
    elif choice == 'e':
        print_query('alco_locos')
    elif choice == 'f':
        print_query('baldwin_locos')
    elif choice == 'g':
        print_query('long_boiler')
    elif choice == 'h':
        print_query('old_locos')
    elif choice == 'z':
        exit