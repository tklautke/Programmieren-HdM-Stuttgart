class Person:
    def __init__(self, fname, lname):
        self.__first_name = fname
        self.__last_name = lname
        self.__birthday = None

    def get_birthday(self):
        return self.__birthday

    def set_birthday(self, bday):
        self.__birthday = bday

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name


class Student(Person):
    __ergebnisse = []

    def __init__(self, firstname, lastname, matrikelnummer):
        super(Student, self).__init__(firstname, lastname)
        self.matrikelnummer = matrikelnummer
        self.__ergebnisse = []

    def add_ergebnis(self, neues_ergebnis):
        self.__ergebnisse.append(neues_ergebnis)


class Pruefungsergebnis():
    def __init__(self, modulname, note):
        self.modulname = modulname,
        self.note = note


# Funktionalität zu den folgenden 2 Zeilen wurden bereits
# bzgl. Aufgabe 1 umgesetzt!
lisa = Student("Lisa", "Müller", 385123)
tim = Student("Tim", "Eisele", 372194)

# Neuerung bzgl. Aufgabe 2 (1.-3.):
e1 = Pruefungsergebnis("Programmieren", 1.0)
e2 = Pruefungsergebnis("Programmieren", 4.0)
lisa.add_ergebnis(e1)
tim.add_ergebnis(e2)
