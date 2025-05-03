from person import Person

class Student(Person):
    """Represents a student, inheriting from Person."""
    def __init__(self, name: str, email: str):
        super().__init__(name, email)
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Student: {super().__str__()}"
