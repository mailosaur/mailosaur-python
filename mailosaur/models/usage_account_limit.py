class UsageAccountLimit(object):
    """UsageAccountLimit.

    :param limit:
    :type limit: int
    :param current:
    :type current: int
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.limit = data.get('limit', None)
        self.current = data.get('current', None)
