from .message_header import MessageHeader

class Metadata(object):
    """Advanced use case content related to the message.

    :param headers: Email headers.
    :type headers: list[~mailosaur.models.MessageHeader]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.headers = [MessageHeader(i) for i in data.get('headers', [])]
