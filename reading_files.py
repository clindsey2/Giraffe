
# file open options: r |  w | a | r+
employee_file = open("employees.txt", "r")

# is the file readable
print(employee_file.readable())

print(employee_file.read())
print("=======================")

employee_file.seek(0, 0)
print(employee_file.readline())

print("-------------------------")
employee_file.seek(0, 0)
# put each line into an array
print(employee_file.readlines())

print("++++++++++++++++++++++++++")
employee_file.seek(0, 0)
for employee in employee_file.readlines():
    print(employee)

employee_file.close()


