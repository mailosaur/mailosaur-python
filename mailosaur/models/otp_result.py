import dateutil.parser


class OtpResult(object):
    """OtpResult.

    :param code: The current one-time password.
    :type code: str
    :param expires: The expiry date/time of the current one-time password.
    :type expires: datetime
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.code = data.get('code', None)
        self.expires = dateutil.parser.parse(data.get('expires', None))
