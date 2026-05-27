from ..models import EmailClientListResult


class PreviewsOperations(object):
    """Operations for discovering the email clients available for generating email
    previews (screenshots of an email rendered in real clients).
    Accessed via ``client.previews``.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def list_email_clients(self):
        """List all email clients that can be used to generate email previews.

        :return: A result containing the available email clients.
        :rtype: ~mailosaur.models.EmailClientListResult
        """
        url = "%sapi/screenshots/clients" % (self.base_url)
        response = self.session.get(url)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        data = response.json()

        return EmailClientListResult(data)
