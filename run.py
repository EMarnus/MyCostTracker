import gspread
from dateutil import parser
from google.oauth2.service_account import Credentials

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

"""



#Delete an object - Get working and then add try fail states




#Calculate VAT - Get working and then add try fail states
#def calc_vat():




#Calculate Margin - Get working and then add try fail states

active_data = get_data()

print(active_data)


"""

Look at adding dates,     

import datetime

input_date = parser.parse(input("Enter a date in DD/MM/YYYY format: "))
date = input_date.date()

date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
"""