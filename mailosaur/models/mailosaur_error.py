import json

class MailosaurError:
    """MailosaurError.

    :param type: Possible values include: 'None', 'ValidationError',
     'AuthenticationError', 'PermissionDeniedError', 'ResourceNotFoundError'
    :type type: str or ~mailosaur.models.enum
    :param messages:
    :type messages: dict[str, str]
    :param model:
    :type model: object
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.type = data.get('type', None)
        self.messages = data.get('messages', None)
        self.model = data.get('model', None)


class MailosaurException(Exception):
    """Server responsed with exception of type: 'MailosaurError'.
    """

    def __init__(self, response):
        message = "Operation returned an invalid status code '%s'" % (response.reason)
        super(MailosaurException, self).__init__(message)
        self.message = message

        if response.status_code in [400]:
            data = json.loads(response._content)
            self.error = MailosaurError(data)
