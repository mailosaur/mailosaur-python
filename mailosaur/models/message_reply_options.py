import json


class MessageReplyOptions(object):
    """MessageReplyOptions.

    :param cc: The email address to which the email will be CC'd. Must be a verified email address.
    :type cc: str
    :param text: Any additional plain text content to include in the reply. Note that only text or html can be supplied, not both.
    :type text: str
    :param html: Any additional HTML content to include in the reply. Note that only html or text can be supplied, not both.
    :type html: str
    :param attachments: Any message attachments.
    :type attachments: list[~mailosaur.models.Attachment]
    """

    def __init__(self, text=None, html=None, attachments=None, cc=None):
        self.cc = cc
        self.text = text
        self.html = html
        self.attachments = attachments

    def to_json(self):
        attachments = []

        if self.attachments is not None:
            for a in self.attachments:
                attachments.append(a.to_json())

        return {
            'cc': self.cc,
            'text': self.text,
            'html': self.html,
            'attachments': attachments
        }
