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
    """

    def __init__(self, to, send, subject, text=None, html=None):
        self.to = to
        self.send = send
        self.subject = subject
        self.text = text
        self.html = html
    
    def to_json(self):
        return {
            'to': self.to,
            'send': self.send,
            'subject': self.subject,
            'text': self.text,
            'html': self.html
        }
