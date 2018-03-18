from .message_summary import MessageSummary

class MessageListResult(object):
    """The result of a message listing request.

    :param items: The individual summaries of each message forming the result.
     Summaries are returned sorted by received date, with the most
     recently-received messages appearing first.
    :type items: list[~mailosaur.models.MessageSummary]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = [MessageSummary(i) for i in data.get('items', None)]
