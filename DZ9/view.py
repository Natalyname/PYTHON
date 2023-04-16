import model


def main_menu() -> int:

    print('\nМеню:')
    print('1. Показать все контакты')
    print('2. Добавить новый контакт')
    print('3. Редактировать контакт')
    print('4. Поиск контакта')
    print('5. Удалить контакт')
    print('0. Выйти')

    choice = input('\nВведите номер команды: ')
    if choice.isdigit() and 0 <= int(choice) <= 5:
        return int(choice)

    else:
        print('Неверный выбор')

def add_contact() -> list:
    print('\nДобавление нового контакта')
    phone = input('Введите номер телефона: ')
    name = input('Введите фамилию и имя: ')
    comment = input('Введите комментарий: ')
    if not phone or not name:
        print('\nОшибка: номер телефона и фамилия/имя не могут быть пустыми')
        return None

    return [phone, name, comment]
    # return contact

def show_contacts(contacts):
    print('\nКонтакты:')

    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact[0]} - {contact[1]}, {contact[2]}")

def show_number_contact(contacts) -> list:
    index = int(input('\nВведите номер контакта, который хотите отредактировать: ')) - 1
    contact = contacts[index]
    print(f'Редактирование контакта: {contact[0]} - {contact[1]}, {contact[2]}')
    phone = input('Введите новый номер телефона (оставьие пустым для сохранения прежнего значения): ')
    name = input('Введите новую фамилию и имя (оставьие пустым для сохранения прежнего значения): ')
    comment = input('Введите новый комментарий (оставьие пустым для сохранения прежнего значения): ')
    if phone:
        contact[0] = phone
    if name:
        contact[1] = name
    if comment:
        contact[2] = comment
    contacts[index] = contact

    return contacts

def search_term():
    search_term = input('Введите строку для поиска: ')
    return search_term



def number_dell():
    number_dell = int(input('Введите номер контакта, который хотите удалить: ')) - 1
    return number_dell