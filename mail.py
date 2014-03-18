import mail_list

def say_hello():
    return "Hello Stranger! This is a cutting-edge, console-based mail-list!\nType help, to see a list of commands."


def help():
    messages = [
        "Here is a full list of commands:",
        "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
        "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
        "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
        "* create <list_name> - Creates a new empty list, with the given name.",
        "* search_email <email> - Performs a search into all lists to see if theunique_list_identifier given email is present. Shows all lists, where the email was found.",
        "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
        "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
        "* exit - this will quit the program"
    ]

    return "\n".join(messages)


def choose_action(mail, command):
    if command == 'help':
        print(help())
    if command == 'create':
        mail.create()
    if command == 'add':
        mail.add()


def main():
    print(say_hello())

    mail = mail_list.MailList()

    while True:
        input_array = input(">").split()
        command = input_array[0]

        choose_action(mail, command)

if __name__ == '__main__':
    main()
