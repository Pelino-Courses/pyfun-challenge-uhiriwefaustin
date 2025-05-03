class Course:
    """Represents a university course."""
    def __init__(self, title: str):
        self.title = title
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course: {self.title}"