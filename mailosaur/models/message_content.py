from .link import Link
from .image import Image

class MessageContent(object):
    """MessageContent.

    :param links:
    :type links: list[~mailosaur.models.Link]
    :param images:
    :type images: list[~mailosaur.models.Image]
    :param body:
    :type body: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.links = [Link(i) for i in data.get('links', [])]

        images = data.get('images', None)
        if isinstance(images, list):
            self.images = [Image(i) for i in images]

        self.body = data.get('body', None)
