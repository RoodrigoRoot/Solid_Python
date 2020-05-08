from .menu import Menu
from .user import DeveloperBehavior

ADD = 1
LIST_ALL_DEVS = 3


def list_developers():
    return []


def create_developer():
    name = input("Nombre: ")
    last_name = input("Apellido: ")
    age = input("Edad: ")
    age = int(age)
    languague = input("Lenguaje de programación: ")
    db = input("Base de datos: ")
    developer = DeveloperBehavior(name, last_name, age, languague, db)
    return developer


def list_all_devs(list_dev):
    for dev in list_dev:
        print(dev.show_dev(1))


def add_developer(developer, list_dev):
    list_dev.append(developer)


def selected_option_menu(option, list_dev):
    if option == ADD:
        developer = create_developer()
        add_developer(developer, list_dev)
        return
    elif option == LIST_ALL_DEVS:
        list_all_devs(list_dev)
        return


def execute():
    list_dev = list_developers()
    while True:
        Menu.menu_principal()
        option = Menu.get_option()
        selected_option_menu(option, list_dev)
