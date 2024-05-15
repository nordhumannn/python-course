from person import Person
from student import Student
from group import Group

if __name__ == '__main__':

    st_1 = Student('Andrew', 'Safonov', 18, 'Ukraine')
    st_2 = Student('Johnny', 'Depp', 58, 'USA')
    st_3 = Student('Dan', 'Watson', 21, 'Austria')
    st_4 = Student('Anna', 'Scholz', 19, 'Germany')
    st_5 = Student('John', 'Doe', 12, 'USA')
    st_6 = Student('John', 'Doe', 13, 'Ukraine')
    st_7 = Student('John', 'Doe', 19, 'USA')
    st_8 = Student('John', 'Doe', 29, 'Poland')
    st_9 = Student('John', 'Doe', 32, 'Ukraine')
    st_10 = Student('John', 'Doe', 58, 'Poland')
    st_11 = Student('John', 'Doe', 45, 'USA')

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
        # group.add_student(st_11)
    except Exception as ex:
        print(ex)

    # print(group)

    # group.remove_student(st_7)

    print(group)

    # print(group.search_student('Depp'))
