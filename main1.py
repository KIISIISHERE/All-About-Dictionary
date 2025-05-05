students = [
    {"id": 1, "name": "Alice", "Class": "Grade 9", "Subject": "Mathematics"},
    {"id": 2, "name": "Bob", "Class": "Grade 10", "Subject": "Science"},
    {"id": 3, "name": "Charlie", "Class": "Grade 9", "Subject": "Mathematics"},    
    {"id": 1, "name": "Alice", "Class": "Grade 9", "Subject": "Mathematics"},
    {"id": 4, "name": "David", "Class": "Grade 11", "Subject": "English"},
    {"id": 1, "name": "Bob", "Class": "Grade 10", "Subject": "Science"},
]
unique_set = set()
unique_students = []
for student in students:
    student_tuple = tuple(student.items())
    if student_tuple not in unique_set:
        unique_set.add(student_tuple)
        unique_students.append(student)
print("Unique student entries:")
for student in unique_students:
    print(student)
    