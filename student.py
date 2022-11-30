class Student(object):
    # Атрибуты
    fio = ''
    gender = ''
    age = 0
    phone = ''
    email = ''
    curs = 0
    grades = {}

    # Создание
    def __init__(self, fio, gender, age, phone, email, curs, grades = {}):
        self.fio = fio
        self.gender = gender
        self.age = age
        self.phone = phone
        self.email = email
        self.curs = curs
        self.grades = grades

    # Перевести на курс выше
    def go_to_next_curs(self):
        # Если студент 5 курса - не переводим
        if (self.curs == 5): return
        self.curs += 1

    # Добавление оценок
    def add_grade(self, grade):
        # Разбираем словарь на предмет и оценку
        subject, _grade = list(grade.items())[0]
        # Если предмет уже существует - добавляем оценку в список
        try:
            self.grades[subject].append(_grade)
        # Иначе создаём ключ в словаре и добавляем оценку
        except:
            self.grades[subject] = [_grade]

# Проверка
student = Student('','',0,'','',2)
student.add_grade({'math': 5})
student.add_grade({'math': 3})
print(student.grades)