class Campingplatz():
    def __init__(self):
        self.__zelte = []
        self.__counter = 0

    def get_zelte(self):
        return self.__zelte

    def add_zelt(self, zt):
        if type(zt) is Zelt:
            zt_id = len(self.__zelte)
            zt.set_id(zt_id)
            zt_dict = {zt.get_id(): zt}
            self.__zelte.append(zt_dict)
            self.__counter += 1

    def get_counter(self):
        return self.__counter

    def get_square_meters(self):
        sqm = 0.0
        for zt_dict in self.get_zelte():
            for key in zt_dict:
                sqm += zt_dict[key].get_square_meters()
        return sqm

    def remove_zelt(self, zelt):
        if type(zelt) is Zelt:
            self.__zelte.pop(zelt.get_id())


class Zelt():
    def __init__(self, sqm=10, person=5):
        self.__get_square_meters = sqm
        self.__person = person
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_person(self):
        return self.__person

    def get_square_meters(self):
        return self.__get_square_meters


if __name__ == '__main__':
    z1 = Zelt(4, 3)  # Aufgabe 1
    z2 = Zelt(4, 3)  # Aufgabe 1
    c1 = Campingplatz()  # 2
    c1.add_zelt(z1)  # 2
    print(c1.get_counter())
    c1.add_zelt(z2)
    print(c1.get_counter())

    print(c1.get_zelte())

    c1.remove_zelt(z2)

    print(c1.get_zelte())
