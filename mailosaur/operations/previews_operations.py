from ..models import PreviewEmailClientListResult


class PreviewsOperations(object):
    """PreviewsOperations operations.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def list_email_clients(self):
        """List all email clients that can be used to generate email previews.

        Returns a list of available email clients.

        :return: PreviewEmailClientListResult
        :rtype: ~mailosaur.models.PreviewEmailClientListResult
        :raises:
         :class:`MailosaurException<mailosaur.models.MailosaurException>`
        """
        url = "%sapi/previews/clients" % (self.base_url)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return PreviewEmailClientListResult(data)
