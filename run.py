import gspread
from dateutil import parser
from google.oauth2.service_account import Credentials
import copy
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('costTracker')


def get_data():
    """
    Pull stored data from google sheet
    """
    active_data = SHEET.worksheet('data').get_all_records()
    return active_data


def inputNumber(message):
    """
    Funciton from https://www.101computing.net/number-only/
    """
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("\nNot a number, please enter a number.")
            continue
        else:
            return userInput 
            break 


#Add item - Get working and then add try fail states
def add_data():
    """
    Add data to the google sheet
    """
    new_row = [] #Append to this

    name = input("Enter Item Name: ")
    new_row.append(name)

    cost = inputNumber("Enter the cost (Please don't use symbols): ")
    new_row.append(cost)
    
    tax = inputNumber("Enter tax rate for the item (Please don't use symbols, \
20% > 20)")
    new_row.append(tax)
        
    margin = inputNumber("Enter margin rate for the item (Please don't use \
symbols, 5% > 5)")
    new_row.append(margin)

    new_row.append("FALSE")

    worksheet_to_update = SHEET.worksheet('data')
    worksheet_to_update.append_row(new_row)

    new_row.append(new_row)
    print("\n")

    # Add in question for looping?

    main()



#Print all objects - Get working and then add try fail states
"""
Prints all rows in googlesheets, only print if Hidden set to false. 
Item    Cost    tax     margin
Example from https://www.educba.com/python-print-table/ 
Also from stackoverflow https://stackoverflow.com/questions/42235918/python-tabulate-dictionary-containing-two-values-per-key

"""
def print_table():
    base_data = calc_margin()
    new_data = [{k: v for k, v in dictionary.items() if k != 'hidden'} for dictionary in base_data if dictionary['hidden'] == 'FALSE']
    
    headers = new_data[0].keys()
    values = [list(dictionary.values()) for dictionary in new_data]

    print(tabulate(values, headers=headers))
    print("\n")

    main()




#Delete an object - Get working and then add try fail states
def del_item():
    """
    Prints current items and lets you select an item to hide.
    """
    base_data = get_data()
    
    #prints to delete from items to select
    for item in base_data:
        print(item.get("item").capitalize())

    to_delete = input("Please enter the item name from the list above that\
 you would like to delete: ").lower()


    worksheet_to_update = SHEET.worksheet('data')

    #credit for code snip is https://stackoverflow.com/questions/71029282/update-value-in-google-sheet-with-if-condition-in-another-column-using-python
    records_data = worksheet_to_update.get_all_records()
    test = worksheet_to_update.col_values(1)
    rownum = test.index('pen') + 1
    row = worksheet_to_update.row_values(rownum)

    worksheet_to_update.update_cell(rownum, 7, 'TRUE')
    print("\n")

    main()





#Calculate VAT - Get working and then add try fail states
def calc_gross():
    """
    Gets the data from the google sheet, applies the set VAT and then returns result
    """

    base_data = get_data()
    working_data = copy.deepcopy(base_data)

    for index in range(len(working_data)):
        working_data[index]["gross"] = working_data[index]["cost"] + (working_data[index]["cost"] * (working_data[index]["tax"]/100))
     
    return working_data






#Calculate Margin - Get working and then add try fail states
def calc_margin():
    """
    Gets the data from the google sheet, applies the set VAT, calculates the price with Margin then returns result
    """
    working_data = calc_gross()

    for index in range(len(working_data)):
        working_data[index]["price"] = working_data[index]["gross"] + (working_data[index]["gross"] * (working_data[index]["margin"]/100))

    return working_data


def main():
    """
    The function the governs user interaction, letting them choose what they want to do.
    """
    action = inputNumber("Welcome to my little program. It allows you to keep\
 track of your project's costs and have individual VAT and margin \
percentages.\n\n1. Enter new data\n2. Print data\n3. Delete entered item\
\n\nPlease select what you want to do by entering a number \
from the list above: ")

    #action = int(action)
    
    if action == 1:
        add_data()
    elif action == 2:
        print_table()
    elif action == 3:
        del_item()
    else:
        print("\nPlease enter a valid number")
        main()



main()

"""

Look at adding dates,     

import datetime

input_date = parser.parse(input("Enter a date in DD/MM/YYYY format: "))
date = input_date.date()

date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
"""