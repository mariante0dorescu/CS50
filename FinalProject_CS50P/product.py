from decorator import decorator

class Product:
    """class with id, name, quantity, price, description
    and a single method that returns a dictionary to be used
    with tabulate for printing"""

    def __init__(
        self, id: int, name: str, quantity: str, price: int | float, description: str
    ):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.description = description

    @property
    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "description": self.description,
        }

    def __str__(self):
        return f"{self.name} {self.quantity} ${self.price}"
