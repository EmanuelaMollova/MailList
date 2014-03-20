import unittest
import mail_list

class MailListTest(unittest.TestCase):
    def setUp(self):
        self.m1 = mail_list.MailList()

        self.m = mail_list.MailList()
        self.m.register = { 1: "HackFMI", 2: "FMI"}
        self.m.mail_list = {"HackFMI" : [["Rado", "radorado@fmi.com"], ], "FMI": [ ["Rado", "radorado@fmi.com"], ["Ico", "icoico@fmi.com"]]}

    def test_create(self):
        self.assertEqual("New list <HackBG> was created", self.m1.create("HackBG"))
        self.assertEqual("HackBG", self.m1.register[1])
        self.assertEqual([], self.m1.mail_list["HackBG"])
        self.assertEqual("A mail list with this name already exists!", self.m1.create("HackBG"))
        print(self.m1.register)
        print(self.m1.mail_list)

    def test_add_name_email(self):
        self.assertEqual("Ivaylo <ivo@hackfmi.com> was added to HackFMI", self.m.add_name_email("Ivaylo", "ivo@hackfmi.com", 1))

    def test_show_list(self):
        self.m.add_name_email("Ivaylo", "ivo@hackfmi.com", 1)
        self.assertEqual("Rado - radorado@fmi.com\nIvaylo - ivo@hackfmi.com\n", self.m.show_list(1))

    def test_show_lists(self):
        self.assertEqual("[1] HackFMI/n[2] FMI", self.m.show_lists_second())

    def test_search_unregistered_email(self):
        self.assertEqual("<anton@antonov.com> was not found in the current mailing lists.", self.m.search_email("anton@antonov.com"))

    def test_serch_email(self):
        self.assertEqual("<radorado@fmi.com> was found in:/n[1] HackFMI/n[2] FMI", self.m.search_email("radorado@fmi.com"))

    def test_is_email_in_mail_list(self):
        self.assertTrue(self.m.is_email_in_mail_list("radorado@fmi.com", 1))

    def test_is_not_email_in_mail_list(self):
        self.assertTrue(not self.m.is_email_in_mail_list("emoemo@fmi.com", 1))




if __name__ == '__main__':
    unittest.main()
