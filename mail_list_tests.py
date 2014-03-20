import unittest
import mail_list

class MailListTest(unittest.TestCase):
    def setUp(self):
        self.m1 = mail_list.MailList()

        self.m = mail_list.MailList()
        self.m.register = { 1: "HackFMI", 2: "FMI"}
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

    def test_show_list(self):
        self.m.add_name_email("Ivaylo", "ivo@hackfmi.com", 1)
        self.assertEqual("Ivaylo - ivo@hackfmi.com\n", self.m.show_list(1))

    def test_show_lists(self):
        self.assertEqual("[1] HackFMI/n[2] FMI", self.m.show_lists_second())

    def test_merge_list(self):
        mail = mail_list.MailList()
        mail.create("HB1")
        index1 = mail.__find_list_index("HB1")
        mail.add_name_email("Emi", "emi@emi.com")

        mail.crate("HB2")
        index2 = mail.__find_list_index("HB2")
        mail.add_name_email("Rado", "rado@rado.com")

        mail.crate("HB3")
        index3 = mail.__find_list_index("HB3")
        mail.add_name_email("RadoRado", "rado@rado.com")

        mail.__merge_lists(index1, index3, "Merged2")

        self.assertEqual("Merged lists <HB1> and <HB2> into <Merged1>", mail.__merge_lists(index1, index2, "Merged1"))

        self.assertEqual(2, len(mail.mail_list["Merged1"]))
        self.assertEqual(1, len(mail.mail_list["Merged2"]))

if __name__ == '__main__':
    unittest.main()
