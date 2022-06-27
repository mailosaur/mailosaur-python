import os
from unittest import TestCase
from mailosaur import MailosaurClient
from mailosaur.models import ServerCreateOptions, MailosaurException


class ErrorsTest(TestCase):
    def test_unauthorized(self):
        client = MailosaurClient('invalid_key')

        with self.assertRaises(MailosaurException) as context:
            client.servers.list()

        self.assertEqual(
            'Authentication failed, check your API key.', context.exception.message)

    def test_not_found(self):
        client = MailosaurClient(os.getenv('MAILOSAUR_API_KEY'))

        with self.assertRaises(MailosaurException) as context:
            client.servers.get('not_found')

        self.assertEqual(
            'Not found, check input parameters.', context.exception.message)

    def test_bad_request(self):
        client = MailosaurClient(os.getenv('MAILOSAUR_API_KEY'))

        with self.assertRaises(MailosaurException) as context:
            options = ServerCreateOptions()
            client.servers.create(options)

        self.assertEqual(
            '(name) Servers need a name\r\n', context.exception.message)
