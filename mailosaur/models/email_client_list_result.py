from .email_client import EmailClient


class EmailClientListResult(object):
    """A list of available email clients with which to generate email previews.

    :param items: A list of available email clients.
    :type items: list[~mailosaur.models.EmailClient]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = [EmailClient(i) for i in data.get('items', None)]
