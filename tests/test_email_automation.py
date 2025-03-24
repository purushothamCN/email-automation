# tests/test_email_automation.py

import unittest
from email_automation.email_automation import EmailAutomation

class TestEmailAutomation(unittest.TestCase):
    def setUp(self):
        # Set up the email automation with your SMTP credentials
        self.email_automation = EmailAutomation(
            smtp_server="smtp.gmail.com",
            smtp_port=587,
            sender_email="purushothamputtu9@gmail.com",  # Use your actual email here
            sender_password="jxrw qqnv oqnc wamt"  # Use your actual email password here
        )

    def test_send_email(self):
        result = self.email_automation.send_email(
            receiver_email="purushothamcn20@gmail.com",
            subject="Test Email",
            body="This is a test email."
        )
        # You can improve the test by asserting successful email delivery.
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
