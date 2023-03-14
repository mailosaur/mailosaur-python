import json


class MessageCreateOptions(object):
    """MessageCreateOptions.

    :param to: The email address to which the email will be sent. Must be a verified email address.
    :type to: str
    :param send: If true, email will be sent upon creation.
    :type send: bool
    :param subject: The email subject line.
    :type subject: str
    :param text: The plain text body of the email. Note that only text or html can be supplied, not both.
    :type text: str
    :param html: The HTML body of the email. Note that only text or html can be supplied, not both.
    :type html: str
    :param attachments: Any message attachments.
    :type attachments: list[~mailosaur.models.Attachment]
    :param sendFrom: Allows for the partial override of the message's 'from' address. This **must** be an
     address ending with `YOUR_SERVER.mailosaur.net`, such as `my-emails@a1bcdef2.mailosaur.net`.
    :type sendFrom: str
    """

    def __init__(self, to, send, subject, text=None, html=None, attachments=None, sendFrom=None):
        self.to = to
        self.send = send
        self.subject = subject
        self.text = text
        self.html = html
        self.attachments = attachments
        self.sendFrom = sendFrom

    def to_json(self):
        attachments = []

        if self.attachments is not None:
            for a in self.attachments:
                attachments.append(a.to_json())

        return {
            'to': self.to,
            'from': self.sendFrom,
            'send': self.send,
            'subject': self.subject,
            'text': self.text,
            'html': self.html,
            'attachments': attachments
        }
