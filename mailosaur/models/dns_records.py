from .spam_assassin_rule import SpamAssassinRule

class DnsRecords(object):
    """DnsRecords.

    :param a:
    :type a: list[string]
    :param mx:
    :type mx: list[string]
    :param ptr:
    :type ptr: list[string]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.a = [a for a in data.get('a', None)]
        self.mx = [mx for mx in data.get('mx', None)]
        self.ptr = [ptr for ptr in data.get('ptr', None)]