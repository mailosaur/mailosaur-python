from image import Image
from link import Link
class EmailData:
    def __init__(self, data):
        self.links = [Link(l) for l in data['links']] if 'links' in data else None
        self.body = data['body']
        self.images = [Image(i) for i in data['images']] if 'images' in data else None