from ..models import SpamAnalysisResult
from ..models import MailosaurException
from ..models import DeliverabilityReport

class AnalysisOperations(object):
    """Operations for analyzing the content and deliverability of an email, including
    SpamAssassin scoring and per-provider deliverability reports.
    Accessed via ``client.analysis``.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def spam(self, email):
        """Perform a spam analysis of an email.

        :param email: The identifier of the message to be analyzed.
        :type email: str
        :return: A result containing the spam score and filter results.
        :rtype: ~mailosaur.models.SpamAnalysisResult
        """
        url = "%sapi/analysis/spam/%s" % (self.base_url, email)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return SpamAnalysisResult(data)

    def deliverability(self, email):
        """Perform a deliverability report of an email.

        :param email: The identifier of the message to be analyzed.
        :type email: str
        :return: A deliverability report for the email.
        :rtype: ~mailosaur.models.DeliverabilityReport
        """
        url = "%sapi/analysis/deliverability/%s" % (self.base_url, email)
        response = self.session.get(url)
        
        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return DeliverabilityReport(data)

