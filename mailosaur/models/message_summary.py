import dateutil.parser
from .message_address import MessageAddress

class MessageSummary(object):
    """MessageSummary.

    :param id:
    :type id: str
    :param server:
    :type server: str
    :param rcpt:
    :type rcpt: list[~mailosaur.models.MessageAddress]
    :param sender:
    :type sender: list[~mailosaur.models.MessageAddress]
    :param to:
    :type to: list[~mailosaur.models.MessageAddress]
    :param cc:
    :type cc: list[~mailosaur.models.MessageAddress]
    :param bcc:
    :type bcc: list[~mailosaur.models.MessageAddress]
    :param received:
    :type received: datetime
    :param subject:
    :type subject: str
    :param summary:
    :type summary: str
    :param attachments:
    :type attachments: int
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.server = data.get('server', None)
        self.sender = [MessageAddress(i) for i in data.get('from', [])]
        self.to = [MessageAddress(i) for i in data.get('to', [])]
        self.cc = [MessageAddress(i) for i in data.get('cc', [])]
        self.bcc = [MessageAddress(i) for i in data.get('bcc', [])]
        self.received = dateutil.parser.parse(data.get('received', None))
        self.subject = data.get('subject', None)
        self.summary = data.get('summary', None)
        self.attachments = data.get('attachments', 0)
