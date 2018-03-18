class SpamAssassinRule(object):
    """SpamAssassinRule.

    :param score:
    :type score: float
    :param rule:
    :type rule: str
    :param description:
    :type description: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.score = data.get('score', 0.0)
        self.rule = data.get('rule', None)
        self.description = data.get('description', None)
