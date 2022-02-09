from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age=0, sex="Helokopter"):
        self.__name = name
        self.__age = age
        self.__sex = sex

    @abstractmethod
    def abstractmethod(self):
        pass

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_sex(self):
        return self.__sex

    def __str__(self):
        return f"Name: {self.get_name()}, Age: {self.get_age()}"
