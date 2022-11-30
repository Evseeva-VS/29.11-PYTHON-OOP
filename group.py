class Group(object):
    # Аттрибуты
    name=''
    number=0
    students=[]

    # Создание
    def __init__(name, number, students=[]):
        self.name = name
        self.number = number
        self.students = students