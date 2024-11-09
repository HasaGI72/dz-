grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
if len(students_list) != len(grades):
    print()
else:
    student_grades_dict = {}
    for i in range(len(students_list)):
        name = students_list[i]
        student_grades_dict[name] = grades[i]
    sorted_students = sorted(student_grades_dict.keys())
    print()
    for name in sorted_students:
        grades = student_grades_dict[name]
        average = sum(grades) / len(grades)
        print(f"{name}: {average:.2f}")