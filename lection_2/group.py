from student import Student
from config import STUDENTS_LIMIT_IN_GROUP

class Group:
    
    def __init__(self, title: str):
        self.title = title
        self.group_list = []

    def add_student(self, student: Student):
        if student not in self.group_list and len(self.group_list) < STUDENTS_LIMIT_IN_GROUP:
            self.group_list.append(student)

    def remove_student(self, student: Student):
        if student in self.group_list:
            self.group_list.remove(student)

    def search_student(self, value: str):
        res = [student for student in self.group_list if student.surname == value]

        return res if res else None

    def __str__(self):
        res = f'\n--- Group: {self.title} ---\n\nStudents in group:\n'
        res += '\n'.join(map(str, self.group_list))

        return res
