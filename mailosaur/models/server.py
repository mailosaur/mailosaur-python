from .forwarding_rule import ForwardingRule

class Server(object):
    """Server.

    :param id: Unique identifier for the server. Used as username for
     SMTP/POP3 authentication.
    :type id: str
    :param password: SMTP/POP3 password.
    :type password: str
    :param name: A name used to identify the server.
    :type name: str
    :param users: Users (excluding administrators) who have access to the
     server.
    :type users: list[str]
    :param messages: The number of messages currently in the server.
    :type messages: int
    :param forwarding_rules: The rules used to manage email forwarding for
     this server.
    :type forwarding_rules: list[~mailosaur.models.ForwardingRule]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.password = data.get('password', None)
        self.name = data.get('name', None)
        self.users = data.get('users', None)
        self.messages = data.get('messages', None)
        self.forwarding_rules = [ForwardingRule(i) for i in data.get('forwardingRules', [])]
