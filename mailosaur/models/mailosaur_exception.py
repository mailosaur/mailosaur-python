class MailosaurException(Exception):
    """MailosaurException.

    :param message:
    type message: str
    :param error_type:
    :type error_type: str
    :param http_status_code:
    :type http_status_code: int
    :param http_response_body:
    :type http_response_body: str
    """

    def __init__(self, message, error_type, http_status_code = None, http_response_body = None):
        super(MailosaurException, self).__init__(message)
        self.message = message
        self.error_type = error_type
        self.http_status_code = http_status_code
        self.http_response_body = http_response_body
 