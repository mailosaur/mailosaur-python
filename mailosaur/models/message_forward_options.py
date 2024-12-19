class MessageForwardOptions(object):
    """MessageForwardOptions.

    :param to: The email address to which the email will be sent. Must be a verified email address.
    :type to: str
    :param cc: The email address to which the email will be CC'd. Must be a verified email address.
    :type cc: str
    :param text: Any additional plain text content to forward the email with. Note that only text or html can be supplied, not both.
    :type text: str
    :param html: Any additional HTML content to forward the email with. Note that only html or text can be supplied, not both.
    :type html: str
    """

    def __init__(self, to, text=None, html=None, cc=None):
        self.to = to
        self.cc = cc
        self.text = text
        self.html = html

    def to_json(self):
        return {
            'to': self.to,
            'cc': self.cc,
            'text': self.text,
            'html': self.html
        }
