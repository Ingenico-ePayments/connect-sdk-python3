from .declined_transaction_exception import DeclinedTransactionException


class DeclinedRefundException(DeclinedTransactionException):
    """
    Represents an error response from a refund call.
    """

    def __init__(self, status_code, response_body, errors):
        if errors is not None:
            super(DeclinedRefundException, self).__init__(status_code,
                                                          response_body,
                                                          errors.error_id,
                                                          errors.errors,
                                                          DeclinedRefundException.__create_message(
                                                              errors))
        else:
            super(DeclinedRefundException, self).__init__(status_code,
                                                          response_body,
                                                          None, None,
                                                          DeclinedRefundException.__create_message(
                                                              errors))
        self.__errors = errors

    @staticmethod
    def __create_message(errors):
        if errors is not None:
            refund = errors.refund_result
        else:
            refund = None
        if refund is not None:
            return "declined refund '" + refund.id + "' with status '" + refund.status + "'"
        else:
            return "the Ingenico ePayments platform returned a declined refund response"

    @property
    def refund_result(self):
        """
        :return: The result of creating a refund if available, otherwise None.
        """
        if self.__errors is None:
            return None
        else:
            return self.__errors.refund_result
