class Mail():
    def __init__(self):
        self.mail_list = {}
        self.register = {}


    def choose_action(self, command):
        if command == 'help':
            self.help()
        if commnad == 'create':
            self.create()


    def say_hello(self):
        print("Hello Stranger! This is a cutting-edge, console-based mail-list!\nType help, to see a list of commands.")


    def help(self):
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

        print("\n".join(messages))


    def create(self, list_name):
        if list_name in self.mail_list:
            return "A mail list with this name already exists!"
        else:
            if len(self.register.keys()) == 0:
                key = 1
            else:
                key = max(self.register.keys()) + 1

            self.register[key] = list_name

        self.mail_list[list_name] = []
        return "New list <{}> was created".format(list_name)


    def add(self,unique_list_identifier):
            input_array = input(">name")
            name = input_array[0]
            input_array = input(">email")
            email = input_array[1]
            print(add_name_email(name, email, unique_list_identifier))


    def add_name_email(self, name, email, unique_list_identifier):
        newlist = [name, email]
        self.mail_list[self.register[unique_list_identifier]].append(newlist)
        return "{} <{}> was added to {}".format(name, email, self.register[unique_list_identifier])


def main():
    mail = Mail()
    mail.say_hello()

    while True:
        input_array = input(">").split()
        command = input_array[0]

        mail.choose_action(command)

if __name__ == '__main__':
    main()
