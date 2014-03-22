from subscriber import Subscriber

class MailList():
    def __init__(self, name):
        self.name        = name
        self.subscribers = []

    def add_subscriber(self, name, email):
        if self.__has_subscriber_with_email(email):
            return False
        else:
            self.subscribers.append(Subscriber(name, email))
            return True

    def __has_subscriber_with_email(self, email):
        if email in list(map(lambda subscriber: subscriber.email, self.subscribers)):
            return True
        else:
            return False
