class ServerListResult(object):
    """The result of an inbox (server) listing request.

    :param items: The individual inboxes (servers) forming the result. Inboxes
     (servers) are returned sorted by creation date, with the most
     recently-created inbox (server) appearing first.
    :type items: list[~mailosaur.models.Server]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = data.get('items', None)
