import unittest
from mail_lists_manager import MailListsManager

class MailListsManagerTest(unittest.TestCase):
    def setUp(self):
        self.mlm = MailListsManager()
        self.mlm.create("HackBG")
        self.mlm.add(1, "Emi", "emanuela.mollova@gmail.com")

    def test_create_adds_new_mail_lists(self):
        self.assertTrue(self.mlm.create("HackFMI"))
        self.assertEqual(2, len(self.mlm.mail_lists))
        self.assertEqual("HackFMI", self.mlm.mail_lists[1].name)
        self.assertEqual([], self.mlm.mail_lists[1].subscribers)

    def test_create_returns_false_when_mail_list_already_exits(self):
        self.assertTrue(not self.mlm.create("HackBG"))

    def test_add_returns_false_when_list_identifier_is_invalid(self):
        self.assertTrue(not self.mlm.add(5, "Emi", "emi@emi.emi"))

    def test_add_adds_new_subscribers(self):
        self.assertTrue(self.mlm.add(1, "Rado", "radorado@hackbulgaria.com"))
        self.assertEqual("Rado", self.mlm.mail_lists[0].subscribers[1].name)
        self.assertEqual("Emi", self.mlm.mail_lists[0].subscribers[0].name)
        self.assertEqual(2, len(self.mlm.mail_lists[0].subscribers))

    def test_show_lists_returns_false_when_there_are_no_lists(self):
        m = MailListsManager()
        self.assertTrue(not m.show_lists())

    def test_show_lists_shows_lists(self):
        self.assertEqual("[1] HackBG", self.mlm.show_lists())

        self.mlm.create("HackFMI")
        self.assertEqual("[1] HackBG\n[2] HackFMI", self.mlm.show_lists())

    def test_show_list_returns_false_when_list_identifier_is_invalid(self):
        self.assertTrue(not self.mlm.show_list(5))

    def test_show_list_shows_list(self):
        self.assertEqual("[1] Emi - emanuela.mollova@gmail.com", self.mlm.show_list(1))

        self.mlm.add(1, "Rado", "radorado@hackbulgaria.com")
        expected = [
            "[1] Emi - emanuela.mollova@gmail.com",
            "[2] Rado - radorado@hackbulgaria.com"
        ]

        self.assertEqual("\n".join(expected), self.mlm.show_list(1))

if __name__ == '__main__':
    unittest.main()
