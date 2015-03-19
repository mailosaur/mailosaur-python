class Image:
    def __init__(self, data):
        self.src = data['src']
        self.alt = data['alt'] if 'alt' in data else None
