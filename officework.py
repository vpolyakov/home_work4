"""
Эта программа Делопроизводство предназначена для работы с документами в офисе.
"""
from officefuncs import add_document
from officefuncs import add_shelf
from officefuncs import delete_document
from officefuncs import delete_shelf
from officefuncs import get_docs_shelf
from officefuncs import get_paper_owner
from officefuncs import list_docs_info
from officefuncs import move_document


def main():
    """
    Главная функция, которая запускает программу Делопроизводство
    "Доступные команды: p, s, l, a, d, q"
    p: получить владельца документа по номеру
    s: получить номер полки по номеру документа
    l: вывести список всех документов
    ad: добавить новый документ
    d: удалить документ по номеру
    m: переместить документ на другую полку
    ads: добавить новую полку
    as: добавить новую полку
    ds: удалить полку
    q: выйти из программы
    """
    while True:
        match res := input('Введите команду: ').strip().lower():
            case "q":
                return
            case "p":
                get_paper_owner()
            case "s":
                get_docs_shelf()
            case "l":
                list_docs_info()
            case "ads":
                add_shelf()
            case "as":
                add_shelf()
            case "ds":
                delete_shelf()
            case "ad":
                add_document()
            case "d":
                delete_document()
            case "m":
                move_document()
            case _:
                print("Неизвестная команда. Попробуйте снова.")


if __name__ == '__main__':
    main()
