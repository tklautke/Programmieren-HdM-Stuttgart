class Notizbuch:
    def __init__(self):
        self.__notizen = []

    def get_notizen(self):
        return self.__notizen

    def add_notizen(self, nt):
        nt_id = len(self.__notizen)
        nt.set_id(nt_id)
        nt_dict = {nt.get_id(): nt}
        self.__notizen.append(nt_dict)


class Notiz:
    def __init__(self, autor, name, seitenzahl):
        self.__autor = autor
        self.__name = name
        self.__seitenzahl = seitenzahl
        self.__id = id

    def get_autor(self):
        return self.__autor

    def get_name(self):
        return self.__name

    def get_seitenzahl(self):
        return self.__seitenzahl

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id


if __name__ == '__main__':
    n1 = Notiz("test", "test", 4)
    n2 = Notiz("test", "test", 3)

    nb1 = Notizbuch()

    nb1.add_notizen(n1)
    nb1.add_notizen(n2)
