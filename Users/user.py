class BaseUser:
    def __init__(self, name, last_name, age):
        self.__name = name
        self.__last_name = last_name
        self.__age = age

    def __str__(self):
        return "Name: {}, Laste Name: {}, Age: {}".format(self.__name, self.__last_name, self.__age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name
        return self.__last_name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        return self.__age

    name = property(get_name, set_name)
    age = property(get_age, set_age)
    last_name = property(get_last_name, set_last_name)


class Developer(BaseUser):

    def __init__(self, name, last_name, age, language, data_base):
        super().__init__(name, last_name, age)
        self.__language = language
        self.__data_base = data_base

    @property
    def languague(self):
        return self.__language

    @property
    def data_base(self):
        return self.__data_base


class DeveloperBehavior:

    def __init__(self, name, last_name, age, language, data_base):
        self.developer = Developer(name, last_name, age, language, data_base)

    def __str__(self):
        return "Clase secreta, we"

    def coding(self):
        print("Nombre: {}, Tecnología: {}, Base de Datos: {}".format(self.developer.name, self.developer.languague, self.developer.data_base))

    def show_dev(self, index):
        print("{}.- {}, {}, {}, {}, {}".format(
                                               index,
                                               self.developer.name,
                                               self.developer.last_name,
                                               self.developer.age,
                                               self.developer.languague,
                                               self.developer.data_base,
                                             ))
        index += 1
        return None
