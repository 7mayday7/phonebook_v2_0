import view
import model
import text_fields as msg


def start_pb():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.load_file()
                view.print_info(msg.load_success)
            case 2:
                model.save_file()
                view.print_info(msg.save_success)
            case 3:
                pb = model.get_pb()
                view.show_contacts(pb, msg.empty_or_closed)
            case 4:
                contact = view.new_contact()
                model.add_contact(contact)
                view.print_info(msg.new_contact_success)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                if model.exit_pb():
                    if view.confirm(msg.is_changed):
                        model.save_file()
                view.print_info(msg.goodbye)
                exit()
