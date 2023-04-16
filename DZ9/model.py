filename = 'contacts.txt'
contacts = []

def get_phonebook() -> list:
    return contacts

def open_file():
    with open(filename, 'r') as f:
        for line in f:
            contact = line.strip().split(',')
            contacts.append(contact)


def add_contact(contact: list):
    if contact is not None:
        contacts.append(contact)



def save_file(contacts):
    try:
        with open(filename, 'a') as f:
            f.write(','.join(contacts) + '\n')
            print('\nКонтакт успешно добавлен')
    except Exception as e:
        print('Повторите еще раз')


def edit_file(contacts, action):
    if contacts is not None:
        with open(filename, 'w') as f:
            for contact in contacts:
                f.write(','.join(contact) + '\n')
        print(f'\nКонтакт успешно {action} ')

# def edit_contact(index):
#     contact = contacts[index]

def search_contact(term, contacts):
    results = []
    for contact in contacts:
        if term.lower() in ' '.join(contact).lower():
            results.append(contact)
    if results:
        print(f'Найдено контактов: {len(results)}')
        for i, contact in enumerate(results):
            print(f'{i+1}. {contact[0]} - {contact[1]}, {contact[2]}')
    else:
        print('Контактов не найдено')


def dell_contact(number, contacts):
    if number <= len(contacts):
        contact = contacts[number]

        print(f'Удаление контакта: {contact[0]} - {contact[1]}, {contact[2]}')
        conf = input('Вы действительно хотите удалить контакт? (y/n): ')
        if conf.lower() == 'y':
            del contacts[number]
            return contacts
        else:
            print('Удаление отменено')
    else:
        print('Контакта с таким номером не существует')
        return None