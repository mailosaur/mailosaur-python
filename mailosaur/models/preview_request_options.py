import json


class PreviewRequestOptions(object):
    """PreviewRequestOptions.

    :param previews: The list of email preview requests.
    :type previews: list[~mailosaur.models.PreviewRequest]
    """

    def __init__(self, previews=None):
        self.previews = previews

    def to_json(self):
        previews = []

        if self.previews is not None:
            for a in self.previews:
                previews.append(a.to_json())

        return {
            'previews': previews
        }
