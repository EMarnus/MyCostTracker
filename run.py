import gspread
from google.oauth2.service_account import Credentials
import copy
from tabulate import tabulate
import datetime

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
    Function from https://www.101computing.net/number-only/
    """
    while True:
        try:
            userInput = float(input(message))
            if userInput < 0:
                print("\n Number must be a positive")
                continue
        except ValueError:
            print("\nNot a number, please enter a positive number.")
            continue
        else:
            return userInput


def inputText(message):
    """
    Function from https://www.101computing.net/number-only/ and adapted
    """
    while True:
        userInput = input(message)

        if userInput.strip() != "":
            return userInput
        else:
            print("\nPlease enter a meaningful name for the item.")


def add_data():
    """
    Add data to the google sheet
    """
    new_row = []  # Append to this

    name = inputText("Enter Item Name: \n")
    new_row.append(name)

    cost = inputNumber(
        "Enter the cost "
        "(Please don't use symbols): \n"
    )
    new_row.append(cost)

    tax = inputNumber(
        "Enter tax rate for the item "
        "(Please don't use symbols 20% > 20): \n"
        )
    new_row.append(tax)

    margin = inputNumber(
        "Enter margin rate for the item "
        "(Please don't use symbols, 5% > 5): \n"
        )
    new_row.append(margin)

    new_row.append("FALSE")

    date = datetime.datetime.now()
    new_row.append(str(date.strftime("%d/%m/%y")))

    print("Updating Database\n")
    worksheet_to_update = SHEET.worksheet('data')
    worksheet_to_update.append_row(new_row)

    new_row.append(new_row)
    print("Item saved\n")


def print_table():
    """
    Prints all rows from googlesheets, only print if Hidden set to false.
    Example from https://www.educba.com/python-print-table/
    Also from stackoverflow https://stackoverflow.com/questions/42235918
    /python-tabulate-dictionary-containing-two-values-per-key
    """
    try:
        base_data = calc_margin()
        new_data = ([{k: v for k, v in dictionary.items() if k != 'hidden'}
                    for dictionary in base_data
                    if dictionary['hidden'] == 'FALSE'])

        headers = new_data[0].keys()
        values = [list(dictionary.values()) for dictionary in new_data]

        print("\n")
        print(tabulate(values, headers=headers, floatfmt=".2f"))
        print("\n")
    except TypeError:
        print("No data to display")
    except IndexError:
        print("No data to display")


def del_item():
    """
    Prints current items and lets you select an item to hide.
    """
    base_data = get_data()

    for item in base_data:
        try:
            if item.get("hidden") == "FALSE":
                print(item.get("item"))
        except Exception:
            continue

    to_delete = input(
        "Please enter the item name from "
        "the list above that you would like to delete: \n"
        )
    worksheet_to_update = SHEET.worksheet('data')

    try:
        # credit for code snip is
        # https://stackoverflow.com/questions/71029282/update-
        # value-in-google-sheet-with-if-condition-in-another-column-using-python
        records_data = worksheet_to_update.get_all_records()
        test = worksheet_to_update.col_values(1)
        rownum = test.index(to_delete) + 1
        row = worksheet_to_update.row_values(rownum)

        worksheet_to_update.update_cell(rownum, 5, 'TRUE')
        print("\n"f"{to_delete} has been removed.""\n")

    except ValueError:
        print("\n"f"{to_delete} is not in the list.""\n")


def calc_gross():
    """
    Gets the data from the google sheet, applies the set VAT and then
    returns result.
    """

    base_data = get_data()
    working_data = copy.deepcopy(base_data)

    for index, item in enumerate(working_data):
        cost = item["cost"]
        tax_rate = item["tax"]/100
        gross = cost + (cost * tax_rate)
        working_data[index]["gross"] = gross

    return working_data


def calc_margin():
    """
    Gets the data from the google sheet, applies the set VAT, calculates the
    price with Margin then returns result
    """
    working_data = calc_gross()

    for index, item in enumerate(working_data):
        cost = item["gross"]
        rate = item["margin"]/100
        price = cost + (cost * rate)
        working_data[index]["price"] = price

    return working_data


def main():
    """
    The function the governs user interaction, letting them choose what they
    want to do.
    """

    while True:
        action = inputNumber(
            "Welcome to my little program. It allows "
            "you to keep track of your project's costs and have "
            "individual VAT and margin percentages.\n\n1. "
            "Enter new item\n2. Print items\n3. Delete entered item "
            "\n\nPlease select what you want to do by entering a number"
            " from the list above: \n"
            )

        database = get_data()

        if action == 1:
            add_data()
        elif action == 2:
            if len(database) != 0:
                print_table()
            else:
                print(
                    "These is noththing to print,"
                    " please select sommething else.\n"
                    )

        elif action == 3:
            if len(database) != 0:
                del_item()
            else:
                print(
                    "These is noththing to delete, "
                    "please select sommething else.\n"
                    )
        else:
            print("\nPlease enter a valid number")


main()
