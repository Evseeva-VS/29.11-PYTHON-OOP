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
    
    # Вывод всех студентов группы по полу
    def get_by_gender(self, gender):
        return '\n'.join([f'{student.fio}, {student.age} лет, оценки: {student.grades}' for student in filter(lambda x: x.gender == gender, [student for student in self.students])])
    