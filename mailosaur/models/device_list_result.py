class DeviceListResult(object):
    """The result of a device listing request.

    :param items: The individual devices forming the result.
    :type items: list[~mailosaur.models.Device]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = data.get('items', None)
