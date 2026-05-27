class ServerCreateOptions(object):
    """Options used to create a new Mailosaur inbox (server).

    :param name: A name used to identify the inbox (server).
    :type name: str
    """

    def __init__(self, name=None):
        self.name = name

    def to_json(self):
        return {
            'name': self.name
        }
