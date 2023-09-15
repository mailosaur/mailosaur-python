from .preview import Preview


class PreviewListResult(object):
    """A list of requested email previews.

    :param items: The summaries for each requested preview.
    :type items: list[~mailosaur.models.Preview]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = [Preview(i) for i in data.get('items', None)]
