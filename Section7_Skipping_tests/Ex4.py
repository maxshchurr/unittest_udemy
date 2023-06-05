import unittest


class EmailSender:
    def send_email(self, to, subject, body):
        # Code to send email
        return True


def is_network_available():
    # Code to check if network is available
    return True


# Enter your solution here
class TestEmailSender(unittest.TestCase):
    @unittest.skipIf(not is_network_available(), "Network unavailable")
    def test_send_email(self):
        sender = EmailSender()
        result = sender.send_email("test@gmail.com", "subject", "body")
        self.assertTrue(result)
