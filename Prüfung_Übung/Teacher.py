from Prüfung_Übung.Human import Human


class Teacher(Human):
    def __init__(self, name, age, sex):
        super(Teacher, self).__init__(name, age, sex)

    def abstractmethod(self):
        pass
