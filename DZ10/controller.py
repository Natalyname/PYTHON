
from classes import PhoneBook


def start():
    phone_book = PhoneBook()
    while True:
        print('\nМеню:')
        print('1. Показать все контакты')
        print('2. Добавить новый контакт')
        print('3. Редактировать контакт')
        print('4. Поиск контакта')
        print('5. Удалить контакт')
        print('0. Выйти')

        choice = input('\nВведите номер команды: ')
        if choice.isdigit() and 0 <= int(choice) <= 5:
            if choice == "1":
                phone_book.display_all_contact()
            elif choice == "2":
                phone = input("Введите номер телефона: ")
                name = input("Введите фамилию и имя: ")
                comment = input("Введите комментарий: ")
                if phone and name:
                    phone_book.add_contact(phone, name, comment)
                else:
                    print('\nОшибка: номер телефона и фамилия/имя не могут быть пустыми')



            elif choice == "3":
                phone_book.display_all_contact()
                index = int(input('\nВведите номер контакта, который хотите отредактировать: ')) - 1

                phone_book.edit_contact(index)


            elif choice == "4":
                search_team = input('Введите строку для поиска: ')
                if not search_team:
                    print("Вы не ввели текст для поиска!")
                    return
                phone_book.search_contact(search_team)

            elif choice == "5":
                phone_book.display_all_contact()
                number_dell = int(input('Введите номер контакта, который хотите удалить: '))
                phone_book.dell_contact(number_dell)

            elif choice == "0":
                print('До скорой встречи!')
                return

