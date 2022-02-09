class Building:

    def __init__(self):
        self.__apartments = dict()

    def get_apartments(self):
        return self.__apartments

    def add_apartment(self, ap):
        ap_id = len(self.__apartments)
        ap.set_id(ap_id)
        self.__apartments[ap.get_id()] = ap

    def get_square_meters(self):
        sqm = 0.0
        for aparment in self.__apartments:
            sqm += self.__apartments[aparment].get_square_meters()
        return sqm

    def get_rental_shares(self, total_rent):
        total_sqm = self.get_square_meters()

        print(total_sqm)

        list_of_rents = list()
        for aparment in self.__apartments:
            rent_of_apartment = self.__apartments[aparment].get_square_meters() / total_sqm
            list_of_rents.append(rent_of_apartment)
        list_rent_apart = list()

        for i in list_of_rents:
            print(i)
            print(total_rent)
            var1 = total_rent * i

            list_rent_apart.append(var1)

        return list_rent_apart


class Apartment:
    def __init__(self, rms=0, sqm=0.0):
        self.__rooms = rms
        self.__square_meters = sqm
        self.__id = 0

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id


    def get_square_meters(self):
        return self.__square_meters


if __name__ == '__main__':
    b1 = Building()
    a1 = Apartment(4, 120)
    a2 = Apartment(5, 80)

    b1.add_apartment(a1)
    b1.add_apartment(a2)

    print(b1.get_rental_shares(2000))
