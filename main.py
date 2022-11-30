from student import Student 
from group import Group 

# Проверка
student1 = Student('Васильков Николай Александрович', 'Мужской', 17, '','', 1)
student2 = Student('Пешкова Наталия Анатольевна', 'Женский', 18, '', '', 1)
group = Group('СА', 112, [student1, student2])
print(group)