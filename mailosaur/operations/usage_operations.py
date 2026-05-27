from ..models import UsageAccountLimits
from ..models import UsageTransactionListResult
from ..models import MailosaurException

class UsageOperations(object):
    """Operations for inspecting your account's usage limits and recent transactional
    usage. These endpoints require authentication with an account-level API key.
    Accessed via ``client.usage``.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def limits(self):
        """Retrieve account usage limits.

        Details the current limits and usage for your account. This endpoint
        requires authentication with an account-level API key.

        :return: The usage limits for your account.
        :rtype: ~mailosaur.models.UsageAccountLimits
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

        This endpoint requires authentication with an account-level API key.

        :return: The transactional usage for the last 31 days.
        :rtype: ~mailosaur.models.UsageTransactionListResult
        """
        url = "%sapi/usage/transactions" % (self.base_url)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return UsageTransactionListResult(data)
