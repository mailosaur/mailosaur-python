from .spam_assassin_rule import SpamAssassinRule
from .result_enum import ResultEnum

class SpamAssassinResult(object):
    """SpamAssassinResult.

    :param score:
    :type score: float
    :param result:
    :type result: ~mailosaur.models.ResultEnum
    :param rules:
    :type rules: list[~mailosaur.models.SpamAssassinRule]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.score = data.get('score', 0.0)
        self.result = ResultEnum(data.get('result', None))
        self.rules = [SpamAssassinRule(i) for i in data.get('rules', None)]
