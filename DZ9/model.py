filename = 'contacts.txt'
contacts = []

def get_phonebook() -> list:
    return contacts

def open_file():
    with open(filename, 'r') as f:
        for line in f:
            contact = line.strip().split(',')
            contacts.append(contact)
            print(contacts)

def add_contact(contact: list):
    contacts.append(contact)



def save_file(contacts):
    try:
        with open(filename, 'a') as f:
            f.write(','.join(contacts) + '\n')
            print('\nКонтакт успешно добавлен')
    except Exception as e:
        print('Повторите еще раз')