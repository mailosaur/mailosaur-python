# coding=utf-8
import dateutil.parser
from .message_address import MessageAddress
from .message_content import MessageContent
from .attachment import Attachment
from .metadata import Metadata

class Message(object):
    """Message.

    :param id: Unique identifier for the message.
    :type id: str
    :param sender: The sender of the message.
    :type sender: list[~mailosaur.models.MessageAddress]
    :param to: The message’s recipient.
    :type to: list[~mailosaur.models.MessageAddress]
    :param cc: Carbon-copied recipients for email messages.
    :type cc: list[~mailosaur.models.MessageAddress]
    :param bcc: Blind carbon-copied recipients for email messages.
    :type bcc: list[~mailosaur.models.MessageAddress]
    :param received: The datetime that this message was received by Mailosaur.
    :type received: datetime
    :param subject: The message’s subject.
    :type subject: str
    :param html: Message content that was sent in HTML format.
    :type html: ~mailosaur.models.MessageContent
    :param text: Message content that was sent in plain text format.
    :type text: ~mailosaur.models.MessageContent
    :param attachments: An array of attachment metadata for any attached
     files.
    :type attachments: list[~mailosaur.models.Attachment]
    :param metadata:
    :type metadata: ~mailosaur.models.Metadata
    :param server: Identifier for the server in which the message is located.
    :type server: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.sender = [MessageAddress(i) for i in data.get('from', [])]
        self.to = [MessageAddress(i) for i in data.get('to', [])]
        self.cc = [MessageAddress(i) for i in data.get('cc', [])]
        self.bcc = [MessageAddress(i) for i in data.get('bcc', [])]
        self.received = dateutil.parser.parse(data.get('received', None))
        self.subject = data.get('subject', None)
        self.html = MessageContent(data.get('html', None))
        self.text = MessageContent(data.get('text', None))
        self.attachments = [Attachment(i) for i in data.get('attachments', [])]
        self.metadata = Metadata(data.get('metadata', None))
        self.server = data.get('server', None)
