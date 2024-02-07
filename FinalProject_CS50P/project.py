import sys
import json
from inventory import Inventory
from fpdf import FPDF
from art import *
from decorator import decorator

def main():
    
    # just prints inventory formated with art module
    print(text2art("INVENTORY"))

    # assign variables for stock object and file name as string
    stock, opened_file_name = start_program()

    while True:
        """takes user command and returns the corresponding function loops each time after user action"""    
        opt = ask_command()

        match opt:
            case 1:
                stock.print_inventory()
            case 2:
                print(stock.total_value_of_items())
            case 3:
                print(stock.total_quantity_of_items())
            case 4:
                stock.update_item_price()
                export_file(stock, opened_file_name)
            case 5:
                stock.update_item_stock()
                export_file(stock, opened_file_name)
            case 6:
                export_to_pdf(stock, opened_file_name)
            case 7:
                sys.exit(text2art("GOOD  BYE"))
            case _:
                print("Invalid command")


# @decorator
def start_program() -> object:
    '''try to get the user input of the json file
        if the user inputs a file that doesnt exist or wrong format
        the program keeps asking for the correct filename
        if user closes the program, program prints GOOD BY and sys.exit()
    '''
    try:
        while True:
            file_name = input("Please enter the name of json file: ").strip()

            if file_name.split(".")[-1] == "json":
                try:
                    inventory = Inventory()
                    inventory.load_file(file_name)
                    return inventory, file_name
                except FileNotFoundError:
                    print(
                        "\nFile not found. Please provide the right name for the JSON file"
                    )
            else:
                print("\nInvalid file extension. Please provide a JSON file.")
    except KeyboardInterrupt:
        print("\n")
        sys.exit(text2art("GOOD  BYE"))

@decorator
def ask_command() -> int:
    '''
    this function ask for a number from user, corresponding an action
    if the value from user is not in list, the program ask again or prints 
    invalid command for invalid input
    '''
    options = [x for x in range(1, 8)]
    commands = {"[1]": "PRINT INVENTORY",
                "[2]": "PRINT TOTAL VALUE OF ITEMS",
                "[3]": "PRINT TOTAL STOCK QUANTITY",
                "[4]": "UPDATE ITEM PRICE",
                "[5]": "UPDATE ITEM QUANTITY",
                "[6]": "CREATE PDF FILE",
                "[7]": "EXIT PROGRAM"
    }

    while True:
        try:
            for key, value in commands.items():
                print(f"{key} : {value}")
            command = input("\nPlease enter your command: ").strip()

            if int(command) in options:
                return int(command)
            else:
                print("\nNot available.\n")
        except:
            print("\nInvalid command.\n")



def export_file(inventory, file_name: str):
    '''this checks each entry from the json file and updates if an item
    has stock or price updates, after replace the local json file
    is called each time the user finish to update stock or price values
    '''
    with open(file_name) as f:
        data = json.load(f)
    for product in inventory.get_items():
        for entry in data:
            if entry["id"] == product["id"]:
                if (
                    entry["price"] != product["price"]
                    or entry["quantity"] != product["quantity"]
                ):
                    entry["quantity"] = product["quantity"]
                    entry["price"] = product["price"]

    with open(file_name, "w") as out:
        json.dump(data, out, indent=2)


def export_to_pdf(inventory, file_name):
    '''function used to export the json file to a formated pdf using FPDF2 module
    takes the name of the json file loaded into the program from start program function
    outputs a pdf with the same name, formated as a table
    '''
    print(f"\nCreating PDF file\n===================")

    file_name = file_name.split(".")[0]
    data = inventory.get_items()
    headers_upper = list(key.upper() for key in data[0].keys())
    headers = list(data[0].keys())
    pdf = FPDF()
    pdf.set_font("helvetica", size=10)
    pdf.add_page()

    with pdf.table(col_widths=(7, 40, 10, 20, 60), text_align=("CENTER", "LEFT", "CENTER", "CENTER", "LEFT")) as table:
        header_row = table.row()
        for header in headers_upper:
            header_row.cell(header)

        for data_row in data:
            row = table.row()

            for header in headers:
                if header in data_row:
                    row.cell(str(data_row[header]))
                else:
                    row.cell('N/A')  # Handle missing keys

    pdf.output(f"{file_name}.pdf")

if __name__ == "__main__":
    main()
