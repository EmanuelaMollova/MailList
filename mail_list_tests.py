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

    def test_merge_list(self):
        mail = mail_list.MailList()
        mail.create("HB1")
        index1 = mail.find_list_index("HB1")
        mail.add_name_email("Emi", "emi@emi.com", index1)

        mail.create("HB2")
        index2 = mail.find_list_index("HB2")
        mail.add_name_email("Rado", "rado@rado.com", index2)

        mail.create("HB3")
        index3 = mail.find_list_index("HB3")
        mail.add_name_email("RadoRado", "rado@rado.com", index3)

        mail.merge_lists_helper(index2, index3, "Merged2")

        self.assertEqual("Merged lists <HB1> and <HB2> into <Merged1>", mail.merge_lists_helper(index1, index2, "Merged1"))

        self.assertEqual(2, len(mail.mail_list["Merged1"]))
        self.assertEqual(1, len(mail.mail_list["Merged2"]))

    def test_delete(self):
        self.assertEqual("<FMI> was deleted.", self.m.delete(2))

    def test_delete_not_there(self):
        self.assertEqual("List with unique identifier <2> was not found.", self.m.delete(2))

    def test_update_subscriber(self):
        self.m1.create("HB")
        index = self.m1.find_list_index("HB")

        self.assertTrue(not self.m1.update_subscriber(index, 1))

        self.m1.add_name_email("Emi", "emi@emi.com", index)
        self.m1.update_name_email("", "emanuela@emi.com", index, 1)

        self.assertEqual("emanuela@emi.com", self.m1["HB"][1][1])
        self.assertEqual("Emi", self.m1["HB"][1][0])


if __name__ == '__main__':
    unittest.main()
