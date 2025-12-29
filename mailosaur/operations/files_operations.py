from ..models import MailosaurException
import time
from datetime import datetime


class FilesOperations(object):
    """FilesOperations operations.
    """

    def __init__(self, session, base_url, handle_http_error):
        self.session = session
        self.base_url = base_url
        self.handle_http_error = handle_http_error

    def get_attachment(self, id):
        """Download an attachment.

        Downloads a single attachment. Simply supply the unique identifier for
        the required attachment.

        :param id: The identifier of the attachment to be downloaded.
        :type id: str
        :return: object
        :rtype: Generator
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        url = "%sapi/files/attachments/%s" % (self.base_url, id)
        response = self.session.get(url, stream=True)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        return response

    def get_email(self, id):
        """Download EML.

        Downloads an EML file representing the specified email. Simply supply
        the unique identifier for the required email.

        :param id: The identifier of the email to be downloaded.
        :type id: str
        :return: object
        :rtype: Generator
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        url = "%sapi/files/email/%s" % (self.base_url, id)
        response = self.session.get(url, stream=True)

        if response.status_code not in [200]:
            self.handle_http_error(response)
            return

        return response

    def get_preview(self, id):
        """Download an email preview.

        Downloads a screenshot of your email rendered in a real email client. Simply supply
        the unique identifier for the required preview.

        :param id: The identifier of the email preview to be downloaded.
        :type id: str
        :return: object
        :rtype: Generator
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        timeout = 120000
        poll_count = 0
        start_time = datetime.today()

        while True:
            url = "%sapi/files/screenshots/%s" % (self.base_url, id)
            response = self.session.get(url, stream=True)

            if response.status_code == 200:
                return response

            if response.status_code not in [202]:
                self.handle_http_error(response)
                return

            # List conversion necessary for Python 3 compatibility
            # https://stackoverflow.com/questions/36982858/object-of-type-map-has-no-len-in-python-3
            delay_pattern = list(
                map(int, (response.headers.get('x-ms-delay') or '1000').split(',')))

            delay = delay_pattern[len(
                delay_pattern) - 1] if poll_count >= len(delay_pattern) else delay_pattern[poll_count]

            poll_count += 1

            # Stop if timeout will be exceeded
            if ((1000 * (datetime.today() - start_time).total_seconds()) + delay) > timeout:
                raise MailosaurException(
                    "An email preview was not generated in time. The email client may not be available, or the preview ID [%s] may be incorrect." % id, "preview_timeout")

            time.sleep(delay / 1000)
