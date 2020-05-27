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
    """Tipo de usuario Developer. Hereda de Baseuser"""
    def __init__(self, name, last_name, age, language, data_base):
        super().__init__(name, last_name, age)
        self.__language = language
        self.__data_base = data_base

    def __str__(self):
        return "Override del método padre en BaseUser"
    
    @property
    def languague(self):
        return self.__language

    @property
    def data_base(self):
        return self.__data_base


class Documentary(BaseUser):
    """Tipo de usuario Documentador. Hereda de Baseuser"""
    def __init__(self, name, last_name, age,):
        super().__init__(name, last_name, age)
        

class UserBhavior:
    """Clase base para el comportamiento de nuestros usuarios """
    def __init__(self, user):
        self.user = user

    def __str__(self):
        return "Clase secreta, we"


    def Working(self):
        print("Nombre: {}".format(self.user.name))


    def show_user(self, index):
        print("{}.- {}, {}, {}".format(
                                               index,
                                               self.user.name,
                                               self.user.last_name,
                                               self.user.age,
                                             ))
        index += 1
        return None

#Comportamiento de los usuarios del Sistema
class DevBehavior(UserBhavior):
    """Clase que hereda de UserBehavior, de manera generica"""
    def __init__(self, type_user):
         super().__init__(type_user)
         self.type_user = "Developer"
    
    def show_user(self, index):
        print("{}.- {}, {}, {}, {}".format(
                                               index,
                                               self.user.name,
                                               self.user.last_name,
                                               self.user.age,
                                               self.type_user
                                             ))
        index += 1
        return None

    


class DocumentaryBehavior(UserBhavior):
    """Clase que hereda de UserBehavior, de manera generica"""
    def __init__(self, type_user):
         super().__init__(type_user)
         self.type_user = "Documentary"
    


if __name__ == "__main__":
    print("------------------Developer----------------")
    developer = Developer("rodrigo", "Urcino", 24, "Python", "DB")
    dev =  DevBehavior(developer)
    dev.Working()
    dev.show_user(1)
    print("------------------Documentador----------------")
    documentary = Documentary("Francisco", "Urcino", 25)
    doc = DocumentaryBehavior(documentary)
    doc.Working()
    doc.show_user(1)