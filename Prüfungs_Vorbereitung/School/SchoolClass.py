class SchoolClass:
    def __init__(self, teacher):
        self.__teacher = teacher
        self.__class_list = list()

    def get_class_list(self):
        return self.__class_list

    def show_name_of_students_in_class(self):
        for i in self.get_class_list():
            print(f"Name of student: {i.get_name()}")

    def get_teacher(self):
        return self.__teacher

    def set_teacher(self, new_teacher):
        self.__teacher = new_teacher

    def add_student_to_class(self, *args):
        for student in args:
            self.__class_list.append(student)
