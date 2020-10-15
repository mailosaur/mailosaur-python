import os
import random
import string
from ..models import ServerListResult
from ..models import Server
from ..models import MailosaurException

class ServersOperations(object):
    """ServersOperations operations.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def generate_email_address(self, server):
        host = os.getenv('MAILOSAUR_SMTP_HOST', 'mailosaur.io')
        randomString = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        return "%s.%s@%s" % (randomString, server, host)

    def list(self):
        """List all servers.

        Returns a list of your virtual SMTP servers. Servers are returned
        sorted in alphabetical order.

        :return: ServerListResult
        :rtype: ~mailosaur.models.ServerListResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/servers" % (self.base_url)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return ServerListResult(data)

    def create(self, server_create_options):
        """Create a server.

        Creates a new virtual SMTP server and returns it.

        :param server_create_options:
        :type server_create_options: ~mailosaur.models.ServerCreateOptions
        :return: Server
        :rtype: ~mailosaur.models.Server
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/servers" % (self.base_url)
        response = self.session.post(url, json=server_create_options.__dict__)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return
        
        data = response.json()

        return Server(data)

    def get(self, id):
        """Retrieve a server.

        Retrieves the detail for a single server. Simply supply the unique
        identifier for the required server.

        :param id: The identifier of the server to be retrieved.
        :type id: str        
        :return: Server
        :rtype: ~mailosaur.models.Server
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/servers/%s" % (self.base_url, id)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Server(data)

    def update(
            self, id, server):
        """Update a server.

        Updats a single server and returns it.

        :param id: The identifier of the server to be updated.
        :type id: str
        :param server:
        :type server: ~mailosaur.models.Server
        :param dict custom_headers: headers that will be added to the request
        :return: Server
        :rtype: ~mailosaur.models.Server
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/servers/%s" % (self.base_url, id)
        response = self.session.put(url, json=server.__dict__)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return Server(data)

    def delete(
            self, id):
        """Delete a server.

        Permanently deletes a server. This operation cannot be undone. Also
        deletes all messages and associated attachments within the server.

        :param id: The identifier of the server to be deleted.
        :type id: str        
        :return: None
        :rtype: None
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/servers/%s" % (self.base_url, id)
        response = self.session.delete(url)
        
        if response.status_code not in [204]:
            self.handle_http_error(response)
            return
