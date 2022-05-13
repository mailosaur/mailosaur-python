import os
import numbers
from unittest import TestCase
from mailosaur import MailosaurClient
from mailosaur.models import DeviceCreateOptions, MailosaurException


class DevicesTest(TestCase):
    @classmethod
    def setUpClass(self):
        api_key = os.getenv('MAILOSAUR_API_KEY')
        base_url = os.getenv('MAILOSAUR_BASE_URL')

        if api_key is None:
            raise Exception(
                "Missing necessary environment variables - refer to README.md")

        self.client = MailosaurClient(api_key, base_url)

    def test_crud(self):
        device_name = "My test"
        shared_secret = "ONSWG4TFOQYTEMY="

        # Create a new device
        options = DeviceCreateOptions()
        options.name = device_name
        options.shared_secret = shared_secret

        created_device = self.client.devices.create(options)
        self.assertIsNotNone(created_device.id)
        self.assertEqual(device_name, created_device.name)

        # Retrieve an otp via device ID
        otp_result = self.client.devices.otp(created_device.id)
        self.assertEqual(6, len(otp_result.code))

        before = self.client.devices.list()
        self.assertTrue(
            any(x['id'] == created_device.id for x in before.items))

        self.client.devices.delete(created_device.id)

        after = self.client.devices.list()
        self.assertFalse(
            any(x['id'] == created_device.id for x in after.items))

    def test_otp_via_shared_secret(self):
        shared_secret = "ONSWG4TFOQYTEMY="

        otp_result = self.client.devices.otp(shared_secret)
        self.assertEqual(6, len(otp_result.code))
