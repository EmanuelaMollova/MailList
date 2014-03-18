import unittest
import mail_list

class MailListTest(unittest.TestCase):
    def setUp(self):
        self.m1 = mail_list.MailList()

        self.m = mail_list.MailList()
        self.m.register = { 1: "HackFMI"}
        self.m.mail_list = { "HackFMI" : []}

    def test_create(self):
        self.assertEqual("New list <HackBG> was created", self.m1.create("HackBG"))
        self.assertEqual("HackBG", self.m1.register[1])
        self.assertEqual([], self.m1.mail_list["HackBG"])
        self.assertEqual("A mail list with this name already exists!", self.m1.create("HackBG"))
        print(self.m1.register)
        print(self.m1.mail_list)

    def test_add_name_email(self):
        self.assertEqual("Ivaylo <ivo@hackfmi.com> was added to HackFMI", self.m.add_name_email("Ivaylo", "ivo@hackfmi.com", 1))


if __name__ == '__main__':
    unittest.main()