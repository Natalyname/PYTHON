class Contact:

    def __init__(self, phone, name, comment):
        self.phone = phone
        self.name = name
        self.comment = comment

    def __str__(self):
        return f'{self.phone}, {self.name}, {self.comment}'

class PhoneBook:

    def __init__(self):
        self.contacts = []


    def add_contact(self, phone, name, comment):
        contact = Contact(phone, name, comment)
        self.contacts.append(contact)


    def display_all_contact(self):
        if not self.contacts:
            print('\nКонтакты не найдены')
        else:
            print('\nКонтакты:')
            for i, contact in enumerate(self.contacts):
                print(f'{i+1}. {contact}')


    def search_contact(self, search_team):
        results = []
        for contact in self.contacts:
            if (search_team.lower() in contact.phone.lower()
                    or search_team.lower() in contact.name.lower()
                    or search_team.lower() in contact.comment.lower()):
                results.append(contact)
        if not results:
            print('\nКонтакты не найдены')
        else:
            print(f'\nНайдено контактов - {len(results)}')
            for i, contact in enumerate(results):
                print(f'{i+1}. {contact}')


    def dell_contact(self, index):
        if len(self.contacts) >= index > 0:
            print(f'\nУдаление контакта: {self.contacts[index - 1]}')
            del self.contacts[index - 1]
            # print(f'Удаление контакта: {self.contacts[index - 1]}')

        else:
            print('\nНекорректный индекс контакта')

    def edit_contact(self, index, phone=None, name=None, comment=None):
        if len(self.contacts) > index >= 0:
            print(f'\nРедактирование контакта: {self.contacts[index]}')
            phone = input('\nВведите новый номер телефона (оставьие пустым для сохранения прежнего значения): ')
            name = input('\nВведите новую фамилию и имя (оставьие пустым для сохранения прежнего значения): ')
            comment = input('\nВведите новый комментарий (оставьие пустым для сохранения прежнего значения): ')
            contact = self.contacts[index]
            if phone:
                contact.phone = phone
            if name:
                contact.name = name
            if comment:
                contact.comment = comment
            print("\nКонтакт сохранен")
        else:
            print("Ошибка: некорректный индекс контакта")