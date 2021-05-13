class UsageTransaction(object):
    """UsageTransaction.

    :param timestamp:
    :type timestamp: datetime
    :param email:
    :type email: int
    :param sms:
    :type sms: int
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.timestamp = data.get('timestamp', None)
        self.email = data.get('email', None)
        self.sms = data.get('sms', None)
