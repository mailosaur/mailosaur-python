class Code(object):
    """Code.

    :param value:
    :type value: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.value = data.get('value', None)
