# import the Student class from the student.py file
#    to allow us to create our own data type of Student
from student import Student

# create an object of the Student class
# NOTE: an object is an instance of a class (class is a template)
#     and the objects are actual students with actual information - student1, student2
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name, student1.gpa)
print(student2.name, student2.major, student2.gpa, student2.is_on_probation)

