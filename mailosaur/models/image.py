class Image(object):
    """Image.

    :param src:
    :type src: str
    :param alt:
    :type alt: str
    """

    def __init__(self, data):
        self.src = data.get('src', None)
        self.alt = data.get('alt', None)
