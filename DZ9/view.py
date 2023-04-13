import model


def main_menu() -> int:

    print('\nМеню:')
    print('1. Показать все контакты')
    print('2. Добавить новый контакт')
    print('3. Редактировать контакт')
    print('4. Поиск контакта')
    print('0. Выйти')

    choice = input('\nВведите номер команды: ')
    if choice.isdigit() and 0 <= int(choice) <= 4:
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