from .api_exception import ApiException


class DeclinedTransactionException(ApiException):
    """
    Represents an error response from a create payment, payout or refund call.
    """

    def __init__(self, status_code, response_body, error_id, errors,
                 message=False):
        if message is False:
            super(DeclinedTransactionException, self).__init__(status_code,
                                                               response_body,
                                                               error_id, errors)
        else:
            super(DeclinedTransactionException, self).__init__(status_code,
                                                               response_body,
                                                               error_id, errors,
                                                               message)
