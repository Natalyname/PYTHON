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
            model.edit_contact()
        elif choice == 4:
            search_contact()
        elif choice == 0:
            return