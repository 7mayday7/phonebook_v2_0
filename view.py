import text_fields as msg


def main_menu():
    print('''Главное меню:
                 1. Открыть файл
                 2. Сохранить файл
                 3. Показать все контакты 
                 4. Создать новый контакт
                 5. Найти контакт
                 6. Удалить контакт
                 7. Изменить контакт
                 8. Выход ''')
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print('Ведите число от 1 до 8: ')


def print_info(message: str):
    line = '\n' + '-' * len(message)
    print(line)
    print(message)
    print(line)


def show_contacts(book: list[dict], message: str):
    line = '\n' + '-' * 63
    if book:
        print(line)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print(line)
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(msg.new_name)
    phone = input(msg.new_phone)
    comment = input(msg.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def confirm(message: str) -> bool:
    print()
    answer = input(message)
    if answer.lower() == 'y':
        return True
    else:
        return False
