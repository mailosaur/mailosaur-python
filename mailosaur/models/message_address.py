class MessageAddress(object):
    """MessageAddress.

    :param name: Display name, if one is specified.
    :type name: str
    :param email: Email address (applicable to email messages).
    :type email: str
    :param phone: Phone number (applicable to SMS messages).
    :type phone: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.name = data.get('name', None)
        self.email = data.get('email', None)
        self.phone = data.get('phone', None)
