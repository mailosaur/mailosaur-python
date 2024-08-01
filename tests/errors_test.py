import os
from unittest import TestCase
from mailosaur import MailosaurClient
from mailosaur.models import ServerCreateOptions, MailosaurException


class ErrorsTest(TestCase):
    @classmethod
    def setUpClass(self):
        self.api_key = os.getenv('MAILOSAUR_API_KEY')
        self.base_url = os.getenv('MAILOSAUR_BASE_URL')

        if self.api_key is None:
            raise Exception(
                "Missing necessary environment variables - refer to README.md")

    def test_unauthorized(self):
        client = MailosaurClient('invalid_key', self.base_url)

        with self.assertRaises(MailosaurException) as context:
            client.servers.list()

        self.assertEqual(
            'Authentication failed, check your API key.', context.exception.message)

    def test_not_found(self):
        client = MailosaurClient(self.api_key, self.base_url)

        with self.assertRaises(MailosaurException) as context:
            client.servers.get('not_found')

        self.assertEqual(
            'Not found, check input parameters.', context.exception.message)

    def test_bad_request(self):
        client = MailosaurClient(self.api_key, self.base_url)

        with self.assertRaises(MailosaurException) as context:
            options = ServerCreateOptions()
            client.servers.create(options)

        self.assertEqual(
            '(name) Servers need a name\r\n', context.exception.message)
