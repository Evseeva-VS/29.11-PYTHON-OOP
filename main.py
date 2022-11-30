from student import Student 
from group import Group 

# Проверка
student1 = Student('Васильков Николай Александрович', 'Мужской', 17, '','', 1)
student2 = Student('Пешкова Наталия Анатольевна', 'Женский', 18, '', '', 1)
group = Group('СА', 112, [student1, student2])
group2 = Group('ИСП', 139, [student1])
print(group2)
group2.add_student(student2)
group2.remove_student(student1)
print(group2)