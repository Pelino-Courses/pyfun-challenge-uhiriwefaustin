from person import Person

class Instructor(Person):
    """Represents an instructor, inheriting from Person."""
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def __str__(self):
        return f"Instructor: {super().__str__()}"
