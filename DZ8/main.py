# Открываем файл со списком контактов
filename = 'contacts.txt'
contacts = []

with open(filename, 'r') as f:
    for line in f:
        contact = line.strip().split(',')
        contacts.append(contact)
print(contacts)
# Функция для показа всех контактов
def show_contacts():
    print('\nКонтакты:')
    for i, contact in enumerate(contacts):
        print(f"{i+1}. {contact[0]} - {contact[1]}, {contact[2]}")

# Функция для добавления нового контакта
def add_contact():
    print('\nДобавление нового контакта')
    phone = input('Введите номер телефона: ')
    name = input('Введите фамилию и имя: ')
    comment = input('Введите комментарий: ')
    contact = [phone, name, comment]
    contacts.append(contact)
    with open(filename, 'a') as f:
        f.write(','.join(contact) + '\n')
    print('Контакт успешно добавлен')

# Функция для редактирования контакта
def edit_contact():
    show_contacts()
    index = int(input('Введите номер контакта, который хотите отредактировать: ')) - 1
    contact = contacts[index]
    print(f'Редактирование контакта: {contact[0]} - {contact[1]}, {contact[2]}')
    phone = input('Введите новый номер телефона (оставьте пустым для сохранения прежнего значения): ')
    name = input('Введите новую фамилию и имя (оставьте пустым для сохранения прежнего значения): ')
    comment = input('Введите новый комментарий (оставьте пустым для сохранения прежнего значения): ')
    if phone:
        contact[0] = phone
    if name:
        contact[1] = name
    if comment:
        contact[2] = comment
    contacts[index] = contact
    with open(filename, 'w') as f:
        for contact in contacts:
            f.write(','.join(contact) + '\n')
    print('Контакт успешно отредактирован')

# Функция для поиска контакта
def search_contact():
    search_term = input('Введите строку для поиска: ')
    results = []
    for contact in contacts:
        if search_term.lower() in ' '.join(contact).lower():
            results.append(contact)
    if results:
        print(f'Найдено контактов: {len(results)}')
        for i, contact in enumerate(results):
            print(f"{i+1}. {contact[0]} - {contact[1]}, {contact[2]}")
    else:
        print('Контактов не найдено')

# Интерактивное меню
while True:
    print('\nМеню:')
    print('1. Показать все контакты')
    print('2. Добавить новый контакт')
    print('3. Редактировать контакт')
    print('4. Поиск контакта')
    print('0. Выйти')

    choice = input('\nВведите номер команды: ')

    if choice == '1':
        show_contacts()
    elif choice == '2':
        add_contact()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        search_contact()
    elif choice == '0':
        break
    else:
        print('Неверный выбор')
