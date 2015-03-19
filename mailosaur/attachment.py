class Attachment:
    def __init__(self, data):
        self.content_type = data['contentType']
        self.file_name = data['fileName'] if 'fileName' in data else None
        self.length = data['length']
        self.id = data['id']