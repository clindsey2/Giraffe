
# import the Student class from the student_wfxn.py file
#    to allow us to create our own data type of Student
from student_wfxn import Student

# class function can be used inside a class
#    can modify the objects of the class or give us specific information
#    about those objects

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.6)

print(student2.on_honor_role())

