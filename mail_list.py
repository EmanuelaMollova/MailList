#TODO Class for contacts, not array
#TODO No strings here, everything with IO should go in mail.py
#TODO Private methods and attributes

class MailList():
    def __init__(self):
        self.mail_list = {}
        self.register  = {}

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

    def show_list(self, unique_list_identifier):
        list_name = self.register[unique_list_identifier]
        contacts = ''
        for contact in self.mail_list[list_name]:
            contacts += contact[0] + " - " + contact[1] + "\n"

        return contacts

    def show_lists(self):
        print(self.show_lists_second())

    def show_lists_second(self):
        formatted_strings = []
        for key in self.register:
            formatted_strings.append("[{}] {}".format(key, self.register[key]))
        return "/n".join(formatted_strings)

    def is_email_in_mail_list(self, email, unique_list_identifier):
        for name_email in self.mail_list[self.register[unique_list_identifier]]:
            if name_email[1] == email:
                return True
        return False

    def search_email(self, searched_email):
        where_is_email = []
        where_is_email.append("<{}> was found in:".format(searched_email))
        is_anywhere = False
        for key in self.register:
            if self.is_email_in_mail_list(searched_email, key):
                where_is_email.append("[{}] {}".format(key, self.register[key]))
                is_anywhere = True
        if not is_anywhere:
            return "<{}> was not found in the current mailing lists.".format(searched_email)
        else:
            return "/n".join(where_is_email)

    def find_list_index(self, list_name):
        for key in self.register:
            if self.register[key] == list_name:
                return key

        return False

    def merge_lists_helper(self, list_identifier_1, list_identifier_2, new_list_name):
        self.create(new_list_name)
        new_identifier = self.find_list_index(new_list_name)

        list_name_1 = self.register[list_identifier_1]
        list_name_2 = self.register[list_identifier_2]

        for contact in self.mail_list[list_name_1]:
            self.add_name_email(contact[0], contact[1], new_identifier)

        for contact in self.mail_list[list_name_2]:
            if self.is_email_in_mail_list(contact[1], list_identifier_1):
                continue
            else:
                self.add_name_email(contact[0], contact[1], new_identifier)

        return "Merged lists <{}> and <{}> into <{}>".format(list_name_1, list_name_2, new_list_name)

    def merge_lists(self, list_identifier_1, list_identifier_2, new_list_name):
        print(self.merge_lists_helper(list_identifier_1, list_identifier_2, new_list_name))

