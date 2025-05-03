class Person:
    """Base class representing a person in the university system."""
    def __init__(self, name:str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"
