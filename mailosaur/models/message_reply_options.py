class MessageReplyOptions(object):
    """MessageReplyOptions.

    :param text: Any additional plain text content to include in the reply. Note that only text or html can be supplied, not both.
    :type text: str
    :param html: Any additional HTML content to include in the reply. Note that only html or text can be supplied, not both.
    :type html: str
    """

    def __init__(self, text=None, html=None):
        self.text = text
        self.html = html

    def to_json(self):
        return {
            'text': self.text,
            'html': self.html
        }
