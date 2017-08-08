""" Email module """

import dateutil.parser
from .email_address import EmailAddress
from .email_data import EmailData
from .attachment import Attachment


class Email:
    """ Mailosaur email class parsed from api response. """
    def __init__(self, data):
        self.id = data['id']
        self.creation_date = dateutil.parser.parse(data['creationdate'])
        self.sender_host = data.get('senderHost', data.get('senderhost', None))
        self.from_address = [EmailAddress(k) for k in data['from']]
        self.to_address = [EmailAddress(k) for k in data['to']]
        self.mailbox = data['mailbox']
        self.raw_id = data.get('rawId', data.get('rawid', None))
        self.html = EmailData(data['html']) if ('html' in data and data['html'] is not None) else None
        self.text = EmailData(data['text']) if ('text' in data and data['text'] is not None) else None
        self.headers = data['headers']
        self.subject = data['subject']
        self.priority = data['priority']

        if 'attachments' in data:
            self.attachments = [Attachment(a) for a in data['attachments']]
        else: 
            self.attachements = None
