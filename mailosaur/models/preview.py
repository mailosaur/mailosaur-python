class Preview(object):
    """Describes an email preview.

    :param id: Unique identifier for the email preview.
    :type id: str

    :param email_client: The email client the preview was generated with.
    :type email_client: str

    :param disable_images: True if images were disabled in the preview.
    :type disable_images: bool
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.email_client = data.get('emailClient', None)
        self.disable_images = data.get('disableImages', None)

    def to_json(self):
        return {
            'id': self.id,
            'emailClient': self.email_client,
            'disableImages': self.disable_images
        }
