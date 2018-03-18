class Link(object):
    """Link.

    :param href:
    :type href: str
    :param text:
    :type text: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}
            
        self.href = data.get('href', None)
        self.text = data.get('text', None)
