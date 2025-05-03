class Enrollment:
    """Handles student-course enrollment relationships."""
    def __init__(self, student, course):
        self.student = student
        self.course = course
        student.enroll(course)
        course.add_student(student)