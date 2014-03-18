import unittest
import mail

class MailTest(unittest.TestCase):
    
    def setUp(self):
        self.m = mail.Mail()
        self.m.register = { 1: "HackFMI"}
        self.m.mail_list = { "HackFMI" : []}


    def test_add_name_email(self):
        self.assertEqual("Ivaylo <ivo@hackfmi.com> was added to HackFMI", self.m.add_name_email("Ivaylo", "ivo@hackfmi.com", 1))


if __name__ == '__main__':
    unittest.main()