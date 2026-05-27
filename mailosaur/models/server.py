class Server(object):
    """A Mailosaur inbox (server) - a virtual SMTP/SMS endpoint.

    :param id: Unique identifier for the inbox (server). Used as username for
     SMTP/POP3 authentication.
    :type id: str
    :param name: A name used to identify the inbox (server).
    :type name: str
    :param users: Users (excluding administrators) who have access to the
     inbox (server) when access is restricted.
    :type users: list[str]
    :param messages: The number of messages currently in the inbox (server).
    :type messages: int
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.name = data.get('name', None)
        self.users = data.get('users', None)
        self.messages = data.get('messages', None)
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'users': self.users,
            'messages': self.messages
        }
