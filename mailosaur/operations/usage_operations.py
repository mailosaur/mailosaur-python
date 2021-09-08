from ..models import UsageAccountLimits
from ..models import UsageTransactionListResult
from ..models import MailosaurException

class UsageOperations(object):
    """UsageOperations operations.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def limits(self):
        """Retrieve account usage limits.

        Details the current limits and usage for your account.

        :return: UsageAccountLimits
        :rtype: ~mailosaur.models.UsageAccountLimits
        :raises:
        :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/usage/limits" % (self.base_url)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return UsageAccountLimits(data)

    def transactions(self):
        """Retrieves the last 31 days of transactional usage.

        Details the usage transactions processed by Mailosaur in the last 31 days.

        :return: UsageTransactionListResult
        :rtype: ~mailosaur.models.UsageTransactionListResult
        :raises:
        :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/usage/transactions" % (self.base_url)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return UsageTransactionListResult(data)
