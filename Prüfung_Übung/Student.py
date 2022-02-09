from Prüfung_Übung.Human import Human


class Student(Human):
    def __init__(self, name, age, sex, matrikel, semester):
        super(Student, self).__init__(name, age, sex)
        self.__matrikel = matrikel
        self.__semester = semester

    def abstractmethod(self):
        pass

    def set_matrikel(self, new_matrikel):
        self.__matrikel = new_matrikel

    def get_matrikel(self):
        return self.__matrikel

    def set_semester(self, new_semester):
        self.__semester = new_semester

    def get_semester(self):
        return self.__semester
