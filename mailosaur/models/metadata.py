from .message_header import MessageHeader
from .message_address import MessageAddress


class Metadata(object):
    """Advanced use case content related to the message.

    :param headers: Email headers.
    :type headers: list[~mailosaur.models.MessageHeader]
    :param mail_from:
    :type mail_from: str
    :param rcpt_to:
    :type rcpt_to: list[~mailosaur.models.MessageAddress]
    :param ehlo:
    :type ehlo: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.headers = [MessageHeader(i) for i in data.get('headers', [])]
        self.ehlo = data.get('ehlo', None)
        self.mail_from = data.get('mailFrom', None)
        self.rcpt_to = [MessageAddress(i) for i in data.get('rcptTo', [])]
