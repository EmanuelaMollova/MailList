import unittest
import mail_list

class MailListTest(unittest.TestCase):
    def setUp(self):
        self.m = mail_list.MailList("HackBG")
        self.m.add_subscriber("Emi", "emi@emi.emi")

    def test_add_subscriber_returns_false_when_there_is_subscriber_with_same_email(self):
        self.assertTrue(not self.m.add_subscriber("Emanuela", "emi@emi.emi"))

    def test_add_subscriber_adds_subscriber(self):
        self.assertTrue(self.m.add_subscriber("Rado", "rado@rado.rado"))
        self.assertEqual(2, len(self.m.subscribers))
        self.assertEqual("Emi", self.m.subscribers[0].name)
        self.assertEqual("rado@rado.rado", self.m.subscribers[1].email)


if __name__ == '__main__':
    unittest.main()
