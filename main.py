from person import Person
from student import Student
from group import Group

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

print(group)
group.remove_student(st_7)
print(group)
print(group.search_student('Depp'))
