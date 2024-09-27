
class Content(object):
    """Content.

    :param embed:
    :type embed: boolean
    :param iframe:
    :type iframe: boolean
    :param object:
    :type object: boolean
    :param script:
    :type script: boolean
    :param short_urls:
    :type short_urls: boolean
    :param text_size:
    :type text_size: int
    :param total_size:
    :type total_size: int
    :param missing_alt:
    :type missing_alt: boolean
    :param missing_list_unsubscribe:
    :type missing_list_unsubscribe: boolean
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.embed = data.get('embed', None)
        self.iframe = data.get('iframe', None)
        self.object = data.get('object', None)
        self.script = data.get('script', None)
        self.short_urls = data.get('shortUrls', None)
        self.text_size = data.get('textSize', None)
        self.total_size = data.get('totalSize', None)
        self.missing_alt = data.get('missingAlt', None)
        self.missing_list_unsubscribe = data.get('missingListUnsubscribe', None)