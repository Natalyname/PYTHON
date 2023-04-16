import model
import view

def start():
    model.open_file()
    con = model.get_phonebook()
    while True:
        choice = view.main_menu()
        if choice == 1:
            pb = model.get_phonebook()

            view.show_contacts(pb)
        elif choice == 2:
            contact = view.add_contact()

            model.add_contact(contact)
            model.save_file(contact)
        elif choice == 3:
            pb = model.get_phonebook()
            view.show_contacts(pb)
            model.edit_file(view.show_number_contact(pb), 'отредактирован')
        elif choice == 4:
            pb = model.get_phonebook()
            term = view.search_term()
            model.search_contact(term, pb)
        elif choice == 5:
            pb = model.get_phonebook()
            view.show_contacts(pb)
            number_dell = view.number_dell()
        #    model.dell_contact(number_dell, pb)
            model.edit_file(model.dell_contact(number_dell, pb), 'удален')
        elif choice == 0:
            print('До скорой встречи!')
            return




