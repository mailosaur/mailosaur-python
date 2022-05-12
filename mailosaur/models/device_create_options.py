class DeviceCreateOptions(object):
    """DeviceCreateOptions.

    :param name: A name used to identify the device.
    :type name: str
    :param shared_secret: The base32-encoded shared secret for this device.
    :type shared_secret: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.name = data.get('name', None)
        self.shared_secret = data.get('shared_secret', None)

    def to_json(self):
        return {
            'name': self.name,
            'sharedSecret': self.shared_secret
        }
