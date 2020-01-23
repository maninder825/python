students = ["john", "jennie", "jim", "jack", "joe"]
print(students, hex(id(students)))

newStudents = students + ["fionna", "george"]
# print(students + ["Fionna", "George"])

print(newStudents, hex(id(newStudents)))

students = students + ["fionna", "george"]
# Operation -> Concatenation in the same List
print("students", hex(id(students)))

