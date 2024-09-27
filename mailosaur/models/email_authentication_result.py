from .spam_filter_results import SpamFilterResults
from .result_enum import ResultEnum

class EmailAuthenticationResult(object):
    """EmailAuthenticationResult.

    :param result:
    :type result: ~mailosaur.models.ResultEnum
    :param description:
    :type description: string
    :param raw_value:
    :type raw_value: string
    :param tags:
    :type tags: dict
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.result = ResultEnum(data.get('result', None))
        self.description = data.get('description', None)
        self.raw_value = data.get('rawValue', None)
        self.tags = data.get('tags', None)
