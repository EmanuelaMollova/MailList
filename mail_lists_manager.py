from mail_list import MailList

class MailListsManager():
    def __init__(self):
        self.mail_lists = []

    def create(self, list_name):
        if list_name in list(map(lambda mail_list: mail_list.name, self.mail_lists)):
            return False
        else:
            self.mail_lists.append(MailList(list_name))
            return True

    def add(self, list_identifier, name, email):
        if not self.__is_list_identifier_valid(list_identifier):
            return False
        else:
            self.mail_lists[list_identifier - 1].add_subscriber(name, email)
            return True

    def show_lists(self):
        if not self.mail_lists:
            return False
        else:
            result = []
            for index, mail_list in enumerate(self.mail_lists):
                result.append("[{}] {}".format(index + 1, mail_list.name))

            return "\n".join(result)

    def show_list(self, list_identifier):
        if not self.__is_list_identifier_valid(list_identifier):
            return False
        else:
            result = []
            for index, subscriber in enumerate(self.mail_lists[list_identifier - 1].subscribers):
                result.append("[{}] {} - {}".format(index + 1, subscriber.name, subscriber.email))

            return "\n".join(result)

    def __is_email_in_list(self, list_identifier, email):
        if not self.__is_list_identifier_valid(list_identifier):
            return False
        if email in list(map(lambda subscriber: subscriber.email, self.mail_lists[list_identifier - 1])):
            return True
        else:
            return False

    def __is_list_identifier_valid(self, list_identifier):
        if len(self.mail_lists) < list_identifier - 1:
            return False
        else:
            return True
