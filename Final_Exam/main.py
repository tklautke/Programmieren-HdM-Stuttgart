class Bauteil:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name


class Baugruppe(Bauteil):
    def __init__(self, name):
        super().__init__(name)
        self.__elemente = dict()

    def add_bauteil(self, teil, anzahl=1):
        if teil in self.__elemente:
            """Das Bauteil ist zwar schon bekannt, muss aber 
            bzgl. seiner Multiplizität noch "hochgezählt" werden."""
            self.__elemente[teil] += anzahl
        else:
            # Das Bauteil wird mit der Menge 1 neu eingetragen
            self.__elemente[teil] = anzahl

    def __str__(self):
        result = super().__str__()
        for elem, mult in self.__elemente.items():
            result += "\n {:>3} Stück {}".format(mult, str(elem))
        return result


flugzeug = Baugruppe("Airbus A350")
rumpf = Baugruppe("Rumpf A350-800R")
t1 = Bauteil("Rolls-Royce Trent XWB-97")
t2 = Bauteil("Rolls-Royce Trent XWB-97")
f_links = Baugruppe("Tragflügel A35f1 L")
f_rechts = Baugruppe("Tragflügel A35f1 R")
leitwerk = Bauteil("Airbus Sabre xA35LW1")
sitz = Bauteil("Recaro SL3710")

flugzeug.add_bauteil(rumpf)
flugzeug.add_bauteil(f_links)
flugzeug.add_bauteil(f_rechts)
rumpf.add_bauteil(sitz, 280)
rumpf.add_bauteil(leitwerk)

print(flugzeug)
