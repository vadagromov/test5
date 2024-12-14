'''Group'''

from student import Student

class Group:
    def __init__(self):
        self.students = {}  # Инициализация атрибута для студентов

    def add_student(self, last_name, first_name, second_name):
        student = Student(last_name, first_name, second_name)
        self.students[str(student)] = student  # Храним объект студента в словаре

    def del_student(self, last_name, first_name, second_name):
        student_key = f"{last_name} {second_name}"
        if student_key in self.students:
            del self.students[student_key]
        else:
            print("Студента с таким ФИО не существует.")

    def list_students(self):
        for student in self.students.values():
            print(student)