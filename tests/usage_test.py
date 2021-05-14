import os
from unittest import TestCase
from mailosaur import MailosaurClient

class UsageTest(TestCase):
    @classmethod
    def setUpClass(self):
        api_key = os.getenv('MAILOSAUR_API_KEY')
        base_url = os.getenv('MAILOSAUR_BASE_URL')

        if api_key is None:
            raise Exception("Missing necessary environment variables - refer to README.md")

        self.client = MailosaurClient(api_key, base_url)

    def test_account_limits(self):
        result = self.client.usage.limits()
        self.assertIsNotNone(result.servers)
        self.assertIsNotNone(result.users)
        self.assertIsNotNone(result.email)
        self.assertIsNotNone(result.sms)

        self.assertTrue(result.servers.limit > 0)
        self.assertTrue(result.users.limit > 0)
        self.assertTrue(result.email.limit > 0)
        self.assertTrue(result.sms.limit > 0)

    def test_transactions_list(self):
        result = self.client.usage.transactions()
        self.assertTrue(len(result.items) > 1)
        self.assertIsNotNone(result.items[0].timestamp)
        self.assertIsNotNone(result.items[0].email)
        self.assertIsNotNone(result.items[0].sms)
