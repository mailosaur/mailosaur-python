class EmailClient(object):
    """Describes an email client with which email previews can be generated.

    :param label: The unique email client label. Used when generating email preview requests.
    :type label: str

    :param name: The display name of the email client.
    :type name: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.label = data.get('label', None)
        self.name = data.get('name', None)

    def to_json(self):
        return {
            'label': self.label,
            'name': self.name
        }
