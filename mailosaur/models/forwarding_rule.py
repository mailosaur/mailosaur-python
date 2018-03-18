class ForwardingRule(object):
    """ForwardingRule.

    :param field: Possible values include: 'from', 'to', 'subject'
    :type field: str or ~mailosaur.models.enum
    :param operator: Possible values include: 'endsWith', 'startsWith',
     'contains'
    :type operator: str or ~mailosaur.models.enum
    :param value:
    :type value: str
    :param forward_to:
    :type forward_to: str
    """

    def __init__(self, data=None):
        if data is None:
            data = {}
            
        self.field = data.get('field', None)
        self.operator = data.get('operator', None)
        self.value = data.get('value', None)
        self.forward_to = data.get('forward_to', None)
