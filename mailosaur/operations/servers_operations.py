import os
import random
import string
from ..models import ServerListResult
from ..models import Server
from ..models import MailosaurException

class ServersOperations(object):
    """Operations for creating and managing your Mailosaur inboxes (servers) - they
    group your tests together, each with its own domain and
    SMTP/POP3/IMAP credentials. Accessed via ``client.servers``.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def generate_email_address(self, server):
        """Generates a random email address by appending a random string in front of
        the domain name of the inbox (server).

        :param server: The identifier of the inbox (server).
        :type server: str
        :return: A random email address ending in the domain of the inbox (server).
        :rtype: str
        """
        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.net')
        randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        return "%s@%s.%s" % (randomString, server, host)

    def list(self):
        """Returns a list of your inboxes (servers).

        Inboxes (servers) are returned sorted in alphabetical order.

        :return: A result containing your inboxes (servers).
        :rtype: ~mailosaur.models.ServerListResult
        """
        url = "%sapi/servers" % (self.base_url)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return ServerListResult(data)

    def create(self, server_create_options):
        """Creates a new inbox (server).

        :param server_create_options: Options used to create a new Mailosaur inbox (server).
        :type server_create_options: ~mailosaur.models.ServerCreateOptions
        :return: The newly-created inbox (server).
        :rtype: ~mailosaur.models.Server
        """
        url = "%sapi/servers" % (self.base_url)
        response = self.session.post(url, json=server_create_options.to_json())
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return
        
        data = response.json()

        return Server(data)

    def get(self, id):
        """Retrieves the detail for a single inbox (server).

        :param id: The unique identifier of the inbox (server).
        :type id: str
        :return: The inbox (server).
        :rtype: ~mailosaur.models.Server
        """
        url = "%sapi/servers/%s" % (self.base_url, id)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Server(data)

    def get_password(self, id):
        """Retrieves the password for an inbox (server).

        This password can be used for SMTP, POP3, and IMAP connectivity.

        :param id: The unique identifier of the inbox (server).
        :type id: str
        :return: The password for the inbox (server).
        :rtype: str
        """
        url = "%sapi/servers/%s/password" % (self.base_url, id)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return data.get('value', None)

    def update(
            self, id, server):
        """Updates the attributes of an inbox (server).

        :param id: The unique identifier of the inbox (server).
        :type id: str
        :param server: The updated inbox (server).
        :type server: ~mailosaur.models.Server
        :return: The updated inbox (server).
        :rtype: ~mailosaur.models.Server
        """
        url = "%sapi/servers/%s" % (self.base_url, id)
        response = self.session.put(url, json=server.to_json())
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Server(data)

    def delete(
            self, id):
        """Permanently delete an inbox (server).

        This will also delete all messages, associated attachments, etc. within
        the inbox (server). This operation cannot be undone.

        :param id: The unique identifier of the inbox (server).
        :type id: str
        :return: None
        :rtype: None
        """
        url = "%sapi/servers/%s" % (self.base_url, id)
        response = self.session.delete(url)
        
        if response.status_code not in [204]:
            self.handle_http_error(response)
            return
