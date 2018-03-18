from .spam_filter_results import SpamFilterResults

class SpamAnalysisResult(object):
    """SpamAnalysisResult.

    :param spam_filter_results:
    :type spam_filter_results: ~mailosaur.models.SpamFilterResults
    :param score:
    :type score: float
    """

    def __init__(self, data=None):
        if data is None:
            data = {}

        self.spam_filter_results = SpamFilterResults(data.get('spamFilterResults', None))
        self.score = data.get('score', 0.0)
