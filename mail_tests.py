import mail
import unittest


class MailTest(unittest.TestCase):

    def setUp(self):
        self.m = mail.Mail()

    def test_create(self):
        self.assertEqual("New list <HackBG> was created", self.m.create("HackBG"))
        self.assertEqual("HackBG", self.m.register[1])
        self.assertEqual([], self.m.mail_list["HackBG"])
        self.assertEqual("A mail list with this name already exists!", self.m.create("HackBG"))
        print(self.m.register)
        print(self.m.mail_list)


if __name__ == '__main__':
    unittest.main()
