from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teaching_assistant import TeachingAssistant

# Here's Example
# Create people
student1 = Student("Faust", "faust@gmail.com")
instructor1 = Instructor("Dr. Pelin", "pelin@yahoo.com")
teach_assistant1 = TeachingAssistant("Cepin", "cepin@gmail.com")

# Create a course
course1 = Course("Python")

# Enroll student and Teaching assistant
Enrollment(student1, course1)
Enrollment(teach_assistant1, course1)

# Output information
print(student1 )
print(instructor1)
print(teach_assistant1)
print(course1)
print("Students in course:")
for student in course1.students:
    print("-", student.name)
