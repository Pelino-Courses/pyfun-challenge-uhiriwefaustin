class Product:
    """
    A simple Product class for inventory management.

    Attributes:
        name (str): The name of the product.
        price (float): The price of one unit (must be non-negative).
        quantity (int): How many units are in stock (must be non-negative).
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a new product with name, price, and quantity.

        Raises:
            ValueError: If price or quantity is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        
        self.__name = name              
        self.__price = price           
        self.__quantity = quantity      

    def add_inventory(self, amount):
        """
        Adds units to inventory.

        Args:
            amount (int): Units to add (must be non-negative).
        """
        if amount < 0:
            raise ValueError("Amount to add cannot be negative.")
        self.__quantity += amount

    def remove_inventory(self, amount):
        """
        Removes units from inventory.

        Args:
            amount (int): Units to remove (must be available and non-negative).
        """
        if amount < 0:
            raise ValueError("Amount to remove cannot be negative.")
        if amount > self.__quantity:
            raise ValueError("Not enough stock to remove.")
        self.__quantity -= amount

    def total_value(self):
        """Returns total value of stock (price * quantity)."""
        return self.__price * self.__quantity

    def display_info(self):
        """Prints product details."""
        print(f"Product: {self.__name}")
        print(f"Price: ${self.__price}")
        print(f"Quantity: {self.__quantity}")
        print(f"Total Value: ${self.total_value()}")

    # Get (optional, show encapsulation)
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity
