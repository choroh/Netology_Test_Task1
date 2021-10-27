"""
Программа для отработки тестирования. Функции добавления, поиска, удаления документов
"""

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }


def find_people(number):
    """
    Поиск имени по номеру документа'
    :param number:
    :return:
    """
    for i in documents:
        if i['number'] == number:
            return i['name']
    else:
        return f'{number}. Номер документа не верен'


def add_doc(type, number, name, shelf_number):
    """
    Добавление документов
    :param type:
    :param number:
    :param name:
    :param shelf_number:
    :return:
    """
    documents.append({'type': type, 'number': number, 'name': name})
    if shelf_number in directories:
        directories[shelf_number].append(number)
        return f'{type} с номером {number} с именем {name} добавлен в каталог и перечень полок'
    else:
        return f'{shelf_number}. Полки с таким номером нет'


#  Удалить из обоих списков
def delete_doc(number):
    """
    Удаление документов из списка документов и из списка полок
    :param number:
    :return:
    """
    for i in documents:
        find = False
        if i['number'] == number:
            documents.remove(i)
            for key, value in directories.items():
                if number in value:
                    shel = key
                    value.remove(number)
                    find = True
    if find == True:
        return f'Документ с номером {number} удален с полки {shel}'
    else:
        return 'Документа с таким номером в каталоге нет'


def main():
    print('Поиск имени по номеру документа')
    for number in ['10006', '11-2', '2207 876234', '111']:
        print(find_people(number))
    print()

    print('Добавление документов')
    print(add_doc('паспорт', '123456789', 'Александр Пушкин', '2'))
    print(add_doc('паспорт', '9876543219', 'Михаил Лермонтов', '4'))
    print()

    print('Удаление документа')
    print(delete_doc('123456789'))


if __name__ == '__main__':
    main()

