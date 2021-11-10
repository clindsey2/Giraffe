
from student import Student

# create an object of the Student class
# NOTE: an object is an instance of a class (class is a template)
#     and an object is an actual student with actual information - student1
student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name, student1.gpa)
print(student2.name, student2.major, student2.gpa, student2.is_on_probation)
