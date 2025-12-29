import json


class PreviewRequestOptions(object):
    """PreviewRequestOptions.

    :param email_clients: The list email clients to generate previews with.
    :type email_clients: list[str]
    """

    def __init__(self, email_clients=None):
        self.email_clients = email_clients

    def to_json(self):
        return {
            'emailClients': self.email_clients
        }
