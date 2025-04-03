"""
Здесь находятся функции для работы с офисными документами.
"""
import re

from data import documents
from data import directories

def input_doc_number():
    """
    Эта функция обрабатывает ввод пользователем номера документа
    """
    while True:
        doc_number = input("Введите номер документа: ")
        if re.search(r'^\d+[ -]*\d+$', doc_number):
            return doc_number
        print('Введите корректный номер домумента.\nНомер документа может цифр, которые могу разделенны либо пробелом, либо знаком"-"')

def input_shelf_number():
    """
    Эта функция обрабатывает ввод пользователем номера полки
    """
    while True:
        shelf_number = input("Введите номер полки: ")
        if re.search(r'^[1-9][0-9]*$', shelf_number):
            return shelf_number
        print('Введите корректный номер полки. Номер полки может состоять только из цифр.')



def get_paper_owner(doc_num=None):
    """
    Возвращает имя владельца документа, если находит документ по его номеру
    """
    num = doc_num or input_doc_number()
    for doc in documents:
        if doc['number'] == num:
            if not doc_num:
                print(f'Владелец документа: {doc['name']}')
            return doc['name']
    if not doc_num:
        print('Документ не найден в базе.')


def get_docs_shelf(doc_num=None):
    """
    Возвращает номер полки, на которой хранится документ, если находит его по его номеру.
    """
    num = doc_num or input_doc_number()
    for shelf, docs in directories.items():
        if num in docs:
            if not doc_num:
                print(f'Документ хранится на полке: {shelf}')
            return shelf
    print('Документ не найден в базе.')


def list_docs_info():
    """
    Вывести список данных по всем документам
    """
    for doc in documents:
        print(f"№ {doc['number']}, "
              f"тип: {doc['type']}, "
              f"владелец: {doc['name']}, "
              f"полка хранения: {get_docs_shelf(doc['number'])}"
              )


def add_shelf():
    """
    Добавляет новую полку
    """
    shelf_num = input_shelf_number()
    if shelf_num in directories:
        print(f'Такая полка уже существует. ', end='')
    else:
        directories[shelf_num] = []
        print(f'Полка {shelf_num} добавлена. ', end='')

    print(f'Текущий перечень полок: {', '.join(directories.keys())}')


def delete_shelf():
    """
    Удаляет полку
    """
    shelf_num = input_shelf_number()
    if shelf_num in directories:
        if directories[shelf_num]:
            print('На полке есть документы. Удалите их перед удалением полки. ', end='')
        else:
            del directories[shelf_num]
            print(f'Полка удалена {shelf_num}. ', end='')
    else:
        print('Такой полки не существует. ', end='')

    print(f'Текущий перечень полок: {', '.join(directories.keys())}')


def add_document():
    """
    Добавляет новый документ
    """
    doc_number = input_doc_number()
    if get_paper_owner(doc_number):
        print('Уже существует документ с таким номером. Измените номер документа.')
        print('Текущий список документов:')
        list_docs_info()
        return
    doc_type = input("Введите тип документа: ")
    doc_owner = input("Введите владельца документа: ")  # TODO Сделать проверку только на буква и перевод в заглавные
    shelf_num = input_shelf_number()
    if shelf_num not in directories:
        print('Такой полки не существует. Добавьте полку командой "as".')
        print('Текущий список документов:')
        list_docs_info()
        return
    documents.append(
        {
            'type': doc_type,
            'number': doc_number,
            'name': doc_owner,
        }
    )
    directories[shelf_num].append(doc_number)
    print('Документ добавлен. Текущий список документов:')
    list_docs_info()


def delete_document():
    """
    Удаляет документ
    """
    doc_number = input_doc_number()

    if shelf_num := get_docs_shelf(doc_number):
        directories[shelf_num].remove(doc_number)
        for doc in documents:
            if doc_number == doc['number']:
                documents.remove(doc)
        print('Документ удален.')

    print('Текущий список документов:')
    list_docs_info()


def move_document():
    """
    Перемещает документ на другую полку
    """
    doc_number = input_doc_number()

    if shelf_num := get_docs_shelf(doc_number):
        destination_shelf_num = input_shelf_number()
        if destination_shelf_num == shelf_num:
            print('Документ не перемещен!\n'
                  'Полка текущего хранения документа совпадает с полкой, на которую перемещается документ.')
            return
        if not destination_shelf_num in directories:
            print(f'Такой полки не существует. Текущий перечень полок: {', '.join(directories.keys())}')
            return
        directories[shelf_num].remove(doc_number)
        directories[destination_shelf_num].append(doc_number)
        print('Документ перемещен.')
    print('Текущий список документов:')
    list_docs_info()
