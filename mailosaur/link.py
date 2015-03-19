class Link:
    def __init__(self, data):
        self.href = data['href'] if 'href' in data else None
        self.text = data['text'] if 'text' in data else None