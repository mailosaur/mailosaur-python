class PreviewRequest(object):
    """Describes an email preview request.

    :param email_client: The email client you wish to generate a preview for.
    :type email_client: str

    :param disable_images: If true, images will be disabled (only if supported by the client).
    :type disable_images: bool
    """

    def __init__(self, email_client, disable_images=False):
        self.email_client = email_client
        self.disable_images = disable_images

    def to_json(self):
        return {
            'emailClient': self.email_client,
            'disableImages': self.disable_images
        }
