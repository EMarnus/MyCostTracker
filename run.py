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



#Add item - Get working and then add try fail states
def add_data():
    """
    Add data to the google sheet
    """
    new_row = [] #Append to this

    name = input("Enter Item Name: ")
    new_row.append(name)

    cost = input("Enter the cost (Don't use symbom): ")
    new_row.append(cost)
    
    try:
        tax = input("Enter tax rate for the item (Don't use %)")
    except:
        print("Please don't enter a symbol")
    new_row.append(tax)

    try:
        margin = input("Enter margin rate for the item (Don't use %)")
    except:
        print("Please don't enter a symbol")
    new_row.append(margin)

    new_row.append("FALSE")

    worksheet_to_update = SHEET.worksheet('data')
    worksheet_to_update.append_row(new_row)

    print(new_row)
    new_row.append(new_row)



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




#Delete an object - Get working and then add try fail states




#Calculate VAT - Get working and then add try fail states
def calc_vat():
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
    working_data = calc_vat()
    print(working_data)

    for index in range(len(working_data)):
        working_data[index]["price"] = working_data[index]["gross"] + (working_data[index]["gross"] * (working_data[index]["margin"]/100))

    return working_data

print_table()
#active_data = print()

#print(active_data)


"""

Look at adding dates,     

import datetime

input_date = parser.parse(input("Enter a date in DD/MM/YYYY format: "))
date = input_date.date()

date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
"""