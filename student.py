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

student = Student('','',0,'','',5)
print(student.curs)
student.go_to_next_curs()
print(student.curs)