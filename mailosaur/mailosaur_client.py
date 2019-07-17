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

class MailosaurClient(object):
    """ Main class to access Mailosaur.com api. """

    def __init__(self, api_key, base_url="https://mailosaur.com/"):
        """ Pass in your mailbox id and api key to authenticate """
        session = requests.Session()
        session.auth = (api_key, '')
        session.headers.update({'User-Agent': 'mailosaur-python/6.0.0'})

        self.servers = ServersOperations(session, base_url)
        self.messages = MessagesOperations(session, base_url)
        self.analysis = AnalysisOperations(session, base_url)
        self.files = FilesOperations(session, base_url)
