class MessageHeader(object):
    """MessageHeader.

    :param field: Header key.
    :type field: str
    :param value: Header value.
    :type value: str
    """

    def __init__(self, data=dict):
        self.field = data.get('field', None)
        self.value = data.get('value', None)
