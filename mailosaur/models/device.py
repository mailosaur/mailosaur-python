class Device(object):
    """Device.

    :param id: Unique identifier for the device.
    :type id: str
    :param name: The name of the device.
    :type name: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.name = data.get('name', None)
