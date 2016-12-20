#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.payment.cancel_approval_payment_response import CancelApprovalPaymentResponse
from ingenico.connect.sdk.domain.payment.cancel_payment_response import CancelPaymentResponse
from ingenico.connect.sdk.domain.payment.create_payment_response import CreatePaymentResponse
from ingenico.connect.sdk.domain.payment.payment_approval_response import PaymentApprovalResponse
from ingenico.connect.sdk.domain.payment.payment_error_response import PaymentErrorResponse
from ingenico.connect.sdk.domain.payment.payment_response import PaymentResponse
from ingenico.connect.sdk.domain.refund.refund_error_response import RefundErrorResponse
from ingenico.connect.sdk.domain.refund.refund_response import RefundResponse
from ingenico.connect.sdk.domain.token.create_token_response import CreateTokenResponse


class PaymentsClient(ApiResource):
    """
    Payments client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(PaymentsClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/payments

        Create payment
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments_post

        :param body:     :class:`CreatePaymentRequest`
        :return: :class:`CreatePaymentResponse`
        :raise: DeclinedPaymentException if the GlobalCollect platform declined / rejected the payment. The payment result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreatePaymentResponse,
                    context)

        except ResponseException as e:
            error_type = {
                400: PaymentErrorResponse,
                402: PaymentErrorResponse,
                403: PaymentErrorResponse,
                502: PaymentErrorResponse,
                503: PaymentErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}

        Get payment
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments__paymentId__get

        :param payment_id:  str
        :return: :class:`PaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments/{paymentId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def approve(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/approve

        Capture payment
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments__paymentId__approve_post

        :param payment_id:  str
        :param body:        :class:`ApprovePaymentRequest`
        :return: :class:`PaymentApprovalResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments/{paymentId}/approve", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    PaymentApprovalResponse,
                    context)

        except ResponseException as e:
            error_type = {
                402: ErrorResponse,
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancel(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/cancel

        Cancel payment
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments__paymentId__cancel_post

        :param payment_id:  str
        :return: :class:`CancelPaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments/{paymentId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    CancelPaymentResponse,
                    context)

        except ResponseException as e:
            error_type = {
                402: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancelapproval(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/cancelapproval

        Undo capture payment request
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments__paymentId__cancelapproval_post

        :param payment_id:  str
        :return: :class:`CancelApprovalPaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments/{paymentId}/cancelapproval", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    CancelApprovalPaymentResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def processchallenged(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/processchallenged

        Approves challenged payment
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments__paymentId__processchallenged_post

        :param payment_id:  str
        :return: :class:`PaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments/{paymentId}/processchallenged", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    PaymentResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
                405: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def refund(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/refund

        Create refund
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments__paymentId__refund_post

        :param payment_id:  str
        :param body:        :class:`RefundRequest`
        :return: :class:`RefundResponse`
        :raise: DeclinedRefundException if the GlobalCollect platform declined / rejected the refund. The refund result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments/{paymentId}/refund", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    RefundResponse,
                    context)

        except ResponseException as e:
            error_type = {
                400: RefundErrorResponse,
                404: RefundErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def tokenize(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/tokenize

        Create a token from payment
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payments__paymentId__tokenize_post

        :param payment_id:  str
        :param body:        :class:`TokenizePaymentRequest`
        :return: :class:`CreateTokenResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payments/{paymentId}/tokenize", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreateTokenResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
