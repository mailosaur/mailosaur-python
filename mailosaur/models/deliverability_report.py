from .email_authentication_result import EmailAuthenticationResult
from .block_list_result import BlockListResult
from .content import Content
from .dns_records import DnsRecords
from .spam_assassin_result import SpamAssassinResult

class DeliverabilityReport(object):
    """DeliverabilityReport.

    :param spf:
    :type spf: ~mailosaur.models.EmailAuthenticationResult
    :param dkim:
    :type dkim: list[~mailosaur.models.EmailAuthenticationResult]
    :param dmarc:
    :type dmarc: ~mailosaur.models.EmailAuthenticationResult
    :param block_list:
    :type block_lists: list[~mailosaur.models.BlockListResult]
    :param content:
    :type content: ~mailosaur.models.Content
    :param dns_records:
    :type dns_records: ~mailosaur.models.DnsRecords
    :param spam_assassin:
    :type spam_assassin: ~mailosaur.models.SpamAssassinResult
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.spf = EmailAuthenticationResult(data.get('spf', None))
        self.dkim = [EmailAuthenticationResult(i) for i in data.get('dkim', None)]
        self.dmarc = EmailAuthenticationResult(data.get('dmarc', None))
        self.block_lists = [BlockListResult(i) for i in data.get('blockLists', None)]
        self.content = Content(data.get('content', None))
        self.dns_records = DnsRecords(data.get('dnsRecords', None))
        self.spam_assassin = SpamAssassinResult(data.get('spamAssassin', None))
