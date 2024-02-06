# INVENTORY, a small stock application
#### [Video Demo](https://youtu.be/vMlMlR-eRp4)
#### Description:
INVENTORY is the final project for CS50P curriculum.

A small application that takes a JSON file as a database, where you can operate updates on the quantities or prices, print the total number of items, total value of items, and the whole inventory.

Also, you can add new products to the JSON file, and optionally export a formatted PDF file with all the items.

### LIBRARIES
__fpdf2__ - This module is used to convert the JSON data to a PDF. [(Readmore)](https://py-pdf.github.io/fpdf2/)

__art__ - Used to print text in an ASCII format [(Readmore)](https://github.com/sepandhaghighi/art/)

__tabulate__ - Used to print the items in a table format [(Readmore)](https://github.com/astanin/python-tabulate)

__mypy__ - Used to test the functions. [(Readmore)](https://mypy.readthedocs.io/en/stable/getting_started.html)

### **Installing Libraries**
there is a a requirements.txt file that has all the libraries used.

and simply can be install by this pip command:

```pip install -r requirements.txt```

## USAGE
```python project.py```

The program will ask for a JSON file. If the file doesn't exist or the filename is not a JSON file, the program will ask again.
The JSON must have some data already formatted like this:

```
[
  {
    "id": 1,
    "name": "Product name",
    "price": 100,
    "quantity": 100,
    "description": "Description..."
  },
  ...
]
```

```
 ___  _   _ __     __ _____  _   _  _____   ___   ____  __   __
|_ _|| \ | |\ \   / /| ____|| \ | ||_   _| / _ \ |  _ \ \ \ / /
 | | |  \| | \ \ / / |  _|  |  \| |  | |  | | | || |_| | \ V / 
 | | | |\  |  \ V /  | |___ | |\  |  | |  | |_| ||  _ <   | |  
|___||_| \_|   \_/   |_____||_| \_|  |_|   \___/ |_| \_\  |_|  

Please enter the name of json file: data.json

```

After this, the program will display the options available:

```
Please enter the name of json file: data.json
[1] : PRINT INVENTORY
[2] : PRINT TOTAL VALUE OF ITEMS
[3] : PRINT TOTAL STOCK QUANTITY
[4] : UPDATE ITEM PRICE
[5] : UPDATE ITEM QUANTITY
[6] : CREATE PDF FILE
[7] : EXIT PROGRAM

Please enter your command: 1 - 7
```
Each number corresponds to an action.
After the user has finished working, the user can export a PDF file and exit the application.

The program will print GOOD BYE and exit.

```
  ____   ___    ___   ____     ____  __   __ _____ 
 / ___| / _ \  / _ \ |  _ \   | __ ) \ \ / /| ____|
| |  _ | | | || | | || | | |  |  _ \  \ V / |  _|  
| |_| || |_| || |_| || |_| |  | |_) |  | |  | |___ 
 \____| \___/  \___/ |____/   |____/   |_|  |_____|
```


### APPLICATION STRUCTURE
The application is divided into

main.py: where all the classes and modules are imported
inventory.py: a class that creates a list of product objects from a JSON file with defined methods
product.py: a class that creates individual item objects
decorator.py: a function used to wrap some functionality in main.py

#### Autor: Marian Teodorescu, Feb 2024