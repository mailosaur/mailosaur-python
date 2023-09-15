import pytest
import os
from unittest import TestCase
import string
import random
from .mailer import Mailer
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria, PreviewRequest, PreviewRequestOptions, MailosaurException


class PreviewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        api_key = os.getenv('MAILOSAUR_API_KEY')
        base_url = os.getenv('MAILOSAUR_BASE_URL')
        cls.server = os.getenv('MAILOSAUR_PREVIEWS_SERVER')

        if api_key is None:
            raise Exception(
                "Missing necessary environment variables - refer to README.md")

        cls.client = MailosaurClient(api_key, base_url)

    def test_list_clients(self):
        result = self.client.previews.list_email_clients()
        self.assertIsNotNone(result.items)
        self.assertTrue(len(result.items) > 1)

    def test_generate_previews(self):
        if self.server is None:
            pytest.skip("Requires server with previews enabled")

        random_string = ''.join(random.choice(
            string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))
        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.net')
        test_email_address = "%s@%s.%s" % (
            random_string, self.server, host)

        Mailer.send_email(self.client, self.server, test_email_address)

        criteria = SearchCriteria()
        criteria.sent_to = test_email_address
        email = self.client.messages.get(self.server, criteria)

        request = PreviewRequest("OL2021")
        options = PreviewRequestOptions([request])

        result = self.client.messages.generate_previews(
            email.id, options)

        self.assertIsNotNone(result.items)
        self.assertTrue(len(result.items) > 0)

        # Ensure we can download one of the generated preview
        file = self.client.files.get_preview(result.items[0].id)
        self.assertIsNotNone(file)


if __name__ == '__main__':
    unittest.main()
