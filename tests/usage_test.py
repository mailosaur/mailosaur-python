import os
from unittest import TestCase
from mailosaur import MailosaurClient

class UsageTest(TestCase):
    @classmethod
    def setUpClass(self):
        base_url = os.getenv('MAILOSAUR_BASE_URL')

        self.client = MailosaurClient(base_url=base_url)

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
