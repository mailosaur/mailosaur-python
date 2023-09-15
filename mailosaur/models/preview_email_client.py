class PreviewEmailClient(object):
    """Describes an email client with which email previews can be generated.

    :param id: The unique identifier of the email client.
    :type id: str

    :param name: The display name of the email client.
    :type name: str

    :param platform_group: Whether the platform is desktop, mobile, or web-based.
    :type platform_group: str

    :param platform_type: The type of platform on which the email client is running.
    :type platform_type: str

    :param platform_version: The platform version number.
    :type platform_version: str

    :param can_disable_images: If true, images can be disabled when generating previews.
    :type can_disable_images: bool

    :param status: The current status of the email client.
    :type status: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.name = data.get('name', None)
        self.platform_group = data.get('platformGroup', None)
        self.platform_type = data.get('platformType', None)
        self.platform_version = data.get('platformVersion', None)
        self.can_disable_images = data.get('canDisableImages', None)
        self.status = data.get('status', None)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'platformGroup': self.platform_group,
            'platformType': self.platform_type,
            'platformVersion': self.platform_version,
            'canDisableImages': self.can_disable_images,
            'status': self.status
        }
