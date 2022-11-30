class Group(object):
    # Аттрибуты
    name=''
    number=0
    students=[]

    # Создание
    def __init__(self, name, number, students=[]):
        self.name = name
        self.number = number
        self.students = students

    # Вывод всех студентов группы
    def __str__(self):
        return '\n'.join([f'{student.fio}, {student.age} лет, оценки: {student.grades}' for student in self.students])
    