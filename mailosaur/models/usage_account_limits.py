from .usage_account_limit import UsageAccountLimit

class UsageAccountLimits(object):
    """UsageAccountLimits.

    :param servers:
    :type servers: ~mailosaur.models.UsageAccountLimit
    :param users:
    :type users: ~mailosaur.models.UsageAccountLimit
    :param email:
    :type email: ~mailosaur.models.UsageAccountLimit
    :param sms:
    :type sms: ~mailosaur.models.UsageAccountLimit
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.servers = UsageAccountLimit(data.get('servers', None))
        self.users = UsageAccountLimit(data.get('users', None))
        self.email = UsageAccountLimit(data.get('email', None))
        self.sms = UsageAccountLimit(data.get('sms', None))
