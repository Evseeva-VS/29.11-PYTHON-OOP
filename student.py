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
