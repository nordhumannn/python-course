STUDENTS_LIMIT_IN_GROUP = 10

class StudentLimitError(Exception):
    
    def __init__(self, value: int | float=None, msg: str=None):
        super().__init__()
        self.value = value
        self.msg = msg

    def __str__(self):
        return f'{self.value}, {self.msg}'

class Person:

    def __init__(self, age: int, country: str):
        self.age = age
        self.country = country

    def __str__(self):
        return f'{self.age}, {self.country}'

class Student(Person):

    def __init__(self, name: str, surname: str, age: int, country: str):
        super().__init__(age, country)
        self.name = name.strip().title()
        self.surname = surname.strip().title()

    def __str__(self):
        return f'{self.name} {self.surname}, {super().__str__()}'

class Group:
    
    def __init__(self, title: str):
        self.title = title
        self.group_list = []

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise TypeError()
        if len(self.group_list) == STUDENTS_LIMIT_IN_GROUP:
            raise StudentLimitError(STUDENTS_LIMIT_IN_GROUP, f'The group is full ({STUDENTS_LIMIT_IN_GROUP})')
        if student in self.group_list:
            raise ValueError('Student already exist')
        
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

st_1 = Student('Andrew', 'Safonov', 18, 'Ukraine')
st_2 = Student('Johnny', 'Depp', 58, 'USA')
st_3 = Student('Dan', 'Watson', 21, 'Austria')
st_4 = Student('Anna', 'Scholz', 19, 'Germany')
st_5 = Student('A', 'B', 12, 'JDSNK')
st_6 = Student('C', 'V', 13, 'SRGG')
st_7 = Student('R', 'F', 19, 'SDGSESB')
st_8 = Student('E', 'Q', 29, 'DSVDSV')
st_9 = Student('E', 'V', 32, 'RSGRVR')
st_10 = Student('G', 'H', 58, 'FDGRG')
st_11 = Student('N', 'N', 45, 'DFDBD')

group = Group('Python Pro')

try:
    group.add_student(st_1)
    group.add_student(st_2)
    group.add_student(st_3)
    group.add_student(st_4)
    group.add_student(st_5)
    group.add_student(st_6)
    group.add_student(st_7)
    group.add_student(st_8)
    group.add_student(st_9)
    group.add_student(st_10)
    group.add_student(st_11)
except Exception as ex:
    print(ex)
