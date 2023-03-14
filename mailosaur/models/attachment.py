class Attachment(object):
    """Describes a message attachment.

    :param id: Unique identifier for the attachment.
    :type id: str

    :param content_type: The MIME type of the attachment.
    :type content_type: str

    :param file_name: The filename of the attachment.
    :type file_name: str

    :param content: The base64-encoded content of the attachment. Note: This is only populated when sending attachments.
    :type content: str

    :param content_id: The content identifier (for attachments that are embedded within the body of the message).
    :type content_id: str
    :param length: The file size, in bytes.
    :type length: int
    :param url: The URL from which the attachment can be downloaded.
    :type url: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.content_type = data.get('contentType', None)
        self.file_name = data.get('fileName', None)
        self.content_id = data.get('contentId', None)
        self.content = data.get('content', None)
        self.length = data.get('length', None)
        self.url = data.get('url', None)

    def to_json(self):
        return {
            'contentType': self.content_type,
            'fileName': self.file_name,
            'contentId': self.content_id,
            'content': self.content
        }
