import gspread
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

data_worksheet = SHEET.worksheet('data')

data = data_worksheet.get_all_values()

data_worksheet.append_row()

print(data)


#Add item - Get working and then add try fail states




#Print all objects - Get working and then add try fail states




#Delete an object - Get working and then add try fail states




#Calculate VAT - Get working and then add try fail states




#Calculate Margin - Get working and then add try fail states





print("What would you like to do?")
print()
print("Options")