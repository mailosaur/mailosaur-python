class SearchCriteria(object):
    """SearchCriteria.

    :param sent_to: The full email address to which the target email was sent.
    :type sent_to: str
    :param subject: The value to seek within the target email's subject line.
    :type subject: str
    :param body: The value to seek within the target email's HTML or text
     body.
    :type body: str
    :param match: If set to "ALL" (default), then only results that match 
     all specified criteria will be returned. If set to "ANY", results that 
     match any of the specified criteria will be returned.
    :type match: str
    """

    def __init__(self):
        self.sent_to = None
        self.subject = None
        self.body = None
        self.match = None

    def toJSON(self):
        return {
            'sentTo': self.sent_to,
            'subject': self.subject,
            'body': self.body
            'match': self.match
        }
