from .result_enum import ResultEnum

class BlockListResult(object):
    """BlockListResult.

    :param id:
    :type id: string
    :param name:
    :type name: string
    :param result:
    :type result: ~mailosaur.models.ResultEnum
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.id = data.get('id', None)
        self.name = data.get('name', None)
        self.result = ResultEnum(data.get('result', None))
