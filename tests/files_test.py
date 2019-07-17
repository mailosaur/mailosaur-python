import os
from unittest import TestCase
from .mailer import Mailer
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria, MailosaurException

class EmailsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        api_key = os.getenv('MAILOSAUR_API_KEY')
        base_url = os.getenv('MAILOSAUR_BASE_URL')
        cls.server = os.getenv('MAILOSAUR_SERVER')

        if (api_key or cls.server) is None:
            raise Exception("Missing necessary environment variables - refer to README.md")

        cls.client = MailosaurClient(api_key, base_url)

        cls.client.messages.delete_all(cls.server)

        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.io')
        test_email_address = "files_test.%s@%s" % (cls.server, host)

        Mailer.send_email(cls.client, cls.server, test_email_address)

        criteria = SearchCriteria()
        criteria.sent_to = test_email_address
        cls.email = cls.client.messages.get(cls.server, criteria)

    def test_get_email(self):
        result = self.client.files.get_email(self.email.id)
        content = b''.join(result).decode('utf-8')
        self.assertIsNotNone(content)
        self.assertTrue(len(content) > 1)
        self.assertTrue(self.email.subject in content)
    
    def test_get_attachment(self):
        attachment = self.email.attachments[0]
        result = self.client.files.get_attachment(attachment.id)
        self.assertIsNotNone(result)

        file_length = 0
        for i in result:
            file_length += len(i)
        self.assertEqual(attachment.length, file_length)

if __name__ == '__main__':
    unittest.main()
