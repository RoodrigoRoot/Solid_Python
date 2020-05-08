import logging

logging.basicConfig(
    level=logging.DEBUG
)


class Menu:

    @staticmethod
    def menu_principal():
        print("**************************+")
        print("1.- Agregar Desarrollador")
        print("2.- Mostrar Desarrollador")
        print("3.- Listar Desarrolladores")
        print("4.- Eliminar Desarrollador")
        print("5.- Modificar Desarrollador")
        print("**************************+")

    @staticmethod
    def get_option():
        try:
            option = input("Ingrese su opción: ")
            option = int(option)
            return option
        except Exception as e:
            logging.debug(e)
