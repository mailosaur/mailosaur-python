class ServerListResult(object):
    """The result of a server listing request.

    :param items: The individual servers forming the result. Servers are
     returned sorted by creation date, with the most recently-created server
     appearing first.
    :type items: list[~mailosaur.models.Server]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = data.get('items', None)
