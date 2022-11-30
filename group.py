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
    
    # Сравнение групп по количеству студентов
    def students_comparison(self, instance):
        if (len(self.students) > len(instance.students)):
            return f'В группе {self.name}-{self.number} больше студентов чем в группе {instance.name}-{instance.number} на {len(self.students) - len(instance.students)}'
        elif (self.curs < instance.curs):
            return f'В группе {instance.name}-{instance.number} больше студентов чем в группе {self.name}-{self.number} на {len(instance.students) - len(self.students)}'
        else:
            return f'В группах одинаковое количество студентов'

    # Добавление студента в группу
    def add_student(self, student):
        self.students.append(student)