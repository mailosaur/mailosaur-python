"""
    mailosaur.com API library. Basic usage:

    >>> from mailosaur import Mailosaur
    >>> mailbox = Mailosaur("BOX_ID", "YOUR_API_KEY")
    >>> emails = mailbox.get_emails()

    More options at https://mailosaur.com/docs/email/
"""

import uuid
import requests

from .operations.servers_operations import ServersOperations
from .operations.messages_operations import MessagesOperations
from .operations.analysis_operations import AnalysisOperations
from .operations.files_operations import FilesOperations
from .operations.usage_operations import UsageOperations
from .operations.devices_operations import DevicesOperations
from .operations.previews_operations import PreviewsOperations
from .models.mailosaur_exception import MailosaurException


class MailosaurClient(object):
    """ Main class to access Mailosaur.com api. """

    def __init__(self, api_key, base_url="https://mailosaur.com/"):
        """ Pass in your mailbox id and api key to authenticate """
        session = requests.Session()
        session.auth = (api_key, '')
        session.headers.update({'User-Agent': 'mailosaur-python/8.0.0'})

        if base_url is None:
            base_url = "https://mailosaur.com/"

        self.servers = ServersOperations(
            session, base_url, self.handle_http_error)
        self.messages = MessagesOperations(
            session, base_url, self.handle_http_error)
        self.analysis = AnalysisOperations(
            session, base_url, self.handle_http_error)
        self.files = FilesOperations(session, base_url, self.handle_http_error)
        self.usage = UsageOperations(session, base_url, self.handle_http_error)
        self.devices = DevicesOperations(
            session, base_url, self.handle_http_error)
        self.previews = PreviewsOperations(
            session, base_url, self.handle_http_error)

    def handle_http_error(self, response):
        message = ""
        if response.status_code == 400:
            try:
                for error in response.json()['errors']:
                    message += "(%s) %s\r\n" % (
                        error['field'], error['detail'][0]['description'])
            except:
                message = "Request had one or more invalid parameters."

            raise MailosaurException(message,
                                     "invalid_request", response.status_code, response.text)
        elif response.status_code == 401:
            raise MailosaurException("Authentication failed, check your API key.",
                                     "authentication_error", response.status_code, response.text)
        elif response.status_code == 403:
            raise MailosaurException("Insufficient permission to perform that task.",
                                     "permission_error", response.status_code, response.text)
        elif response.status_code == 404:
            raise MailosaurException("Not found, check input parameters.",
                                     "invalid_request", response.status_code, response.text)
        elif response.status_code == 410:
            raise MailosaurException("Permanently expired or deleted.",
                                     "gone", response.status_code, response.text)
        else:
            raise MailosaurException("An API error occurred, see httpResponse for further information.",
                                     "api_error", response.status_code, response.text)
