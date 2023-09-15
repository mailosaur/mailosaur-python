from .preview_email_client import PreviewEmailClient


class PreviewEmailClientListResult(object):
    """A list of available email clients with which to generate email previews.

    :param items: A list of available email clients.
    :type items: list[~mailosaur.models.PreviewEmailClient]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = [PreviewEmailClient(i) for i in data.get('items', None)]
