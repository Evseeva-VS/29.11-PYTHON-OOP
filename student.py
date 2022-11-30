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

    # Сравнение студентов по курсу
    def curs_comparison(self, instance):
        if (self.curs > instance.curs):
            return f'Студент {self.fio} старше {instance.fio} по курсу на {self.curs - instance.curs} год/лет'
        elif (self.curs < instance.curs):
            return f'Студент {instance.fio} старше {self.fio} по курсу на {instance.curs - self.curs} год/лет'
        else:
            return f'Студенты {self.fio} и {instance.fio} на одном курсе'
