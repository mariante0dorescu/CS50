import json
from product import Product
from tabulate import tabulate
from decorator import decorator

class Inventory:
    '''
    class that creates a list of products objects from a json file
    with the followinf methods:
    - load file: loads a json and creates Product objectby assigning ke/value entries with Product class attributes
    - get item to update: get ID from user and checks if is an integer and the ID is one of the products in the list
    - total value of inventory: sum the number of items/pcs multiplied by price and return the total value
    - total quantity of items: sum the number of pcs / items and returns the value
    - update item price
    - update item quantity
    - edit items data function: transforms the keys to uppercase, adds ".pcs" and "$ " to each item from the inventory (used in printing)
    - prints inventory using tabulate moduleand edit items data function
    - prints one line of the inventory using tabulate module and edit items data function
    '''
    def __init__(self):
        self.inventory = []

    def load_file(self, filename: str):
        self.file_name = filename
        with open(filename) as file:
            data = json.load(file)
            for line in data:
                self.inventory.append(
                    Product(
                        id=line["id"],
                        name=line["name"],
                        price=line["price"],
                        quantity=line["quantity"],
                        description=line["description"],
                    )
                )

    def get_items(self):
        data = []
        for item in self.inventory:
            data.append(item.info)
        return data

    def total_value_of_items(self):
        return f"\n===================\nTotal value: ${sum(item.price * item.quantity for item in self.inventory):,.2f}\n==================="

    def total_quantity_of_items(self):
        return f"\n===================\nTotal stock: {sum(item.quantity for item in self.inventory)} pcs.\n==================="

    def update_item_price(self):
        print(f"\nUpdate price\n===================")
        self.update_price(self.get_id_to_update())

    def update_item_stock(self):
        print(f"\nUpdate stock\n===================")
        self.update_stock(self.get_id_to_update())

    @decorator
    def get_id_to_update(self) -> int:
        try:
            id = int(input("\nPlease enter the ID of item: ").strip())
            if 1 <= int(id) <= len(self.inventory):
                return id
            else:
                raise ValueError
        except ValueError:
            raise ValueError("\nWrong input / no product with this ID")

    @decorator
    def update_price(self, id: int):
        self.print_line(self.inventory[id - 1].info)
        try:
            new_price = int(input("\nPlease enter the new price: ").strip())
            if new_price > 0:
                self.inventory[id - 1].price = new_price
                print(
                    f"\nPrice updated successfully.\nNew price: $ {self.inventory[id-1].price}"
                )
                self.print_line(self.inventory[id - 1].info)
            else:
                raise ValueError
        except ValueError:
            raise ValueError("\nPrice cannot be smaller than zero")

    @decorator
    def update_stock(self, id: int):
        self.print_line(self.inventory[id - 1].info)
        try:
            new_quantity = int(input("\nPlease enter the new quantity: ").strip())
            if new_quantity > 0:
                self.inventory[id - 1].quantity = new_quantity
                print(
                    f"\nStock updated successfully.\nNew quantity: {self.inventory[id-1].quantity}"
                )
                self.print_line(self.inventory[id - 1].info)
            else:
                raise ValueError
        except ValueError:
            raise ValueError("\nStock cannot be smaller than zero")

    def print_inventory(self):
        print(
            tabulate(
                self.edit_items_data(self.get_items()),
                headers="keys",
                tablefmt="outline",
                numalign="left",
            )
        )

    def print_line(self, data: list):
        print(
            tabulate(
                self.edit_items_data([data]),
                headers="keys",
                tablefmt="outline",
                numalign="left",
            )
        )

    @staticmethod
    def edit_items_data(data: list) -> list:
        new_data = []
        for entry in data:
            new_data.append(
                {
                    "ID": entry["id"],
                    "NAME": entry["name"],
                    "DESCRIPTION": entry["description"],
                    "QUANTITY": f"{entry['quantity']} pcs.",
                    "PRICE": f"$ {entry['price']}",
                }
            )
        return new_data
