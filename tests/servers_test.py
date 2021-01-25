import os
import numbers
from unittest import TestCase
from mailosaur import MailosaurClient
from mailosaur.models import ServerCreateOptions, MailosaurException

class ServersTest(TestCase):
    @classmethod
    def setUpClass(self):
        api_key = os.getenv('MAILOSAUR_API_KEY')
        base_url = os.getenv('MAILOSAUR_BASE_URL')

        if api_key is None:
            raise Exception("Missing necessary environment variables - refer to README.md")

        self.client = MailosaurClient(api_key, base_url)

    def test_list(self):
        result = self.client.servers.list()
        self.assertTrue(len(result.items) > 1)

    def test_get_not_found(self):
        with self.assertRaises(MailosaurException):
            self.client.servers.get("efe907e9-74ed-4113-a3e0-a3d41d914765")

    def test_crud(self):
        server_name = "My test"

        # Create a new server
        options = ServerCreateOptions(server_name)
        created_server = self.client.servers.create(options)
        self.assertIsNotNone(created_server.id)
        self.assertEqual(server_name, created_server.name)
        self.assertIsNotNone(created_server.password)
        self.assertIsInstance(created_server.users, list)
        self.assertIsInstance(created_server.messages, numbers.Number)

        # Retrieve a server and confirm it has expected content
        retrieved_server = self.client.servers.get(created_server.id)
        self.assertEqual(created_server.id, retrieved_server.id)
        self.assertEqual(created_server.name, retrieved_server.name)
        self.assertIsNotNone(retrieved_server.password)
        self.assertIsInstance(retrieved_server.users, list)
        self.assertIsInstance(retrieved_server.messages, numbers.Number)

        # Update a server and confirm it has changed
        retrieved_server.name += " updated with ellipsis … and emoji 👨🏿‍🚒"
        updated_server = self.client.servers.update(retrieved_server.id, retrieved_server)
        self.assertEqual(retrieved_server.id, updated_server.id)
        self.assertEqual(retrieved_server.name, updated_server.name)
        self.assertEqual(retrieved_server.password, updated_server.password)
        self.assertEqual(retrieved_server.users, updated_server.users)
        self.assertEqual(retrieved_server.messages, updated_server.messages)

        self.client.servers.delete(retrieved_server.id)

        # Attempting to delete again should fail
        with self.assertRaises(MailosaurException):
            self.client.servers.delete(retrieved_server.id)

    def test_failed_create(self):
        with self.assertRaises(MailosaurException) as context:
            options = ServerCreateOptions()
            self.client.servers.create(options)

        ex = context.exception
        self.assertEqual("Request had one or more invalid parameters.", ex.message)
        self.assertEqual("invalid_request", ex.error_type)
        self.assertEqual(400, ex.http_status_code)
        self.assertEqual("{\"type\":\"ValidationError\",\"messages\":{\"name\":\"Please provide a name for your server\"}}", ex.http_response_body)