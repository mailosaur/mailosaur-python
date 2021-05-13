from .usage_transaction import UsageTransaction

class UsageTransactionListResult(object):
    """UsageTransactionListResult.

    :param items: The individual transactions forming the result.
    :type items: list[~mailosaur.models.UsageTransaction]
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.items = [UsageTransaction(i) for i in data.get('items', None)]
