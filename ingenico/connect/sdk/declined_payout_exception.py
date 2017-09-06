from .declined_transaction_exception import DeclinedTransactionException


class DeclinedPayoutException(DeclinedTransactionException):
    """
    Represents an error response from a payout call.
    """

    def __init__(self, status_code, response_body, errors):
        if errors is not None:
            super(DeclinedPayoutException, self).__init__(status_code,
                                                          response_body,
                                                          errors.error_id,
                                                          errors.errors,
                                                          DeclinedPayoutException.__create_message(
                                                              errors))
        else:
            super(DeclinedPayoutException, self).__init__(status_code,
                                                          response_body,
                                                          None, None,
                                                          DeclinedPayoutException.__create_message(
                                                              errors))
        self.__errors = errors

    @staticmethod
    def __create_message(errors):
        if errors is not None:
            payout = errors.payout_result
        else:
            payout = None
        if payout is not None:
            return "declined payout '" + payout.id + "' with status '" + payout.status + "'"
        else:
            return "the Ingenico ePayments platform returned a declined payout response"

    @property
    def payout_result(self):
        """
        :return: The result of creating a payout if available, otherwise None.
        """
        if self.__errors is None:
            return None
        else:
            return self.__errors.payout_result
