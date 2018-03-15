from ..models import MailosaurException

class FilesOperations(object):
    """FilesOperations operations.
    """

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

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
            raise MailosaurException(response)

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
            raise MailosaurException(response)

        return response