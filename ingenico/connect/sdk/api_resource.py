from ingenico.connect.sdk.domain.errors.error_response import \
    ErrorResponse
from ingenico.connect.sdk.domain.payment.payment_error_response import \
    PaymentErrorResponse
from ingenico.connect.sdk.domain.refund.refund_error_response import \
    RefundErrorResponse

from .api_exception import ApiException
from .authorization_exception import AuthorizationException
from .declined_payment_exception import DeclinedPaymentException
from .declined_payout_exception import DeclinedPayoutException
from .declined_refund_exception import DeclinedRefundException
from .global_collect_exception import GlobalCollectException
from .idempotence_exception import IdempotenceException
from ingenico.connect.sdk.domain.payout.payout_error_response import \
    PayoutErrorResponse
from .reference_exception import ReferenceException
from .request_header import RequestHeader
from .validation_exception import ValidationException


class ApiResource(object):
    """
    Base class of all Ingenico ePayments platform API resources.
    """

    def __init__(self, arg, path_context, client_meta_info=None):
        """
        :param arg: communicator or parent
        """
        if arg is None:
            raise ValueError("parent or communicator is required")
        if isinstance(arg, ApiResource):
            self.__parent = arg
            self.__communicator = arg._communicator
            self.__path_context = path_context
            self.__client_meta_info = arg._client_meta_info
        else:
            self.__parent = None
            self.__communicator = arg
            self.__path_context = path_context
            self.__client_meta_info = client_meta_info

    @property
    def _communicator(self):
        return self.__communicator

    @property
    def _client_meta_info(self):
        return self.__client_meta_info

    @property
    def _client_headers(self):
        if self._client_meta_info is not None:
            client_headers = [
                RequestHeader("X-GCS-ClientMetaInfo", self._client_meta_info)]
            return client_headers
        else:
            return None

    def _instantiate_uri(self, uri, path_context):
        uri = self.__replace_all(uri, path_context)
        uri = self.__instantiate_uri(uri)
        return uri

    def __instantiate_uri(self, uri):
        uri = self.__replace_all(uri, self.__path_context)
        if self.__parent is not None:
            uri = self.__parent.__instantiate_uri(uri)
        return uri

    def __replace_all(self, uri, path_context):
        if path_context:
            for key, value in path_context.items():
                uri = uri.replace("{" + key + "}", value)
        return uri

    def _create_exception(self, status_code, body, error_object, context):
        """Return a raisable api-exception based on the error object given"""
        if isinstance(error_object,
                      PaymentErrorResponse) and error_object.payment_result is not None:
            return DeclinedPaymentException(status_code=status_code,
                                            response_body=body,
                                            errors=error_object)
        elif isinstance(error_object,
                        PayoutErrorResponse) and error_object.payout_result is not None:
            return DeclinedPayoutException(status_code=status_code,
                                           response_body=body,
                                           errors=error_object)
        elif isinstance(error_object,
                        RefundErrorResponse) and error_object.refund_result is not None:
            return DeclinedRefundException(status_code=status_code,
                                           response_body=body,
                                           errors=error_object)
        if not isinstance(error_object,
                          (PaymentErrorResponse, PayoutErrorResponse,
                           RefundErrorResponse, ErrorResponse)):
            raise ValueError("Unsupported error object encountered: {}".format(error_object.__class__.__name__)) \
                from error_object  # unsupported error object
        error_id = error_object.error_id
        errors = error_object.errors
        if _is_idempotence_error(status_code, errors, context):
            return IdempotenceException(context.idempotence_key,
                                        context.idempotence_request_timestamp,
                                        status_code, body, error_id, errors)
        # get error based on status code, defaulting to ApiException
        return ERROR_MAP.get(status_code, ApiException)(status_code, body,
                                                        error_id, errors)


def _is_idempotence_error(status_code, errors, context):
    """
    Determines if an idempotence error has occurred based on the status code,
    errors and context
    """
    return status_code == 409 \
        and context is not None \
        and context.idempotence_key is not None \
        and len(errors) == 1 \
        and errors[0].code


ERROR_MAP = {
    400: ValidationException,
    403: AuthorizationException,
    404: ReferenceException,
    409: ReferenceException,  # idempotence has already been tested
    410: ReferenceException,
    500: GlobalCollectException,
    502: GlobalCollectException,
}
