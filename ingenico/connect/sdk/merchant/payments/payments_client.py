#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.capture.capture_response import CaptureResponse
from ingenico.connect.sdk.domain.capture.captures_response import CapturesResponse
from ingenico.connect.sdk.domain.dispute.dispute_response import DisputeResponse
from ingenico.connect.sdk.domain.dispute.disputes_response import DisputesResponse
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.payment.cancel_approval_payment_response import CancelApprovalPaymentResponse
from ingenico.connect.sdk.domain.payment.cancel_payment_response import CancelPaymentResponse
from ingenico.connect.sdk.domain.payment.complete_payment_response import CompletePaymentResponse
from ingenico.connect.sdk.domain.payment.create_payment_response import CreatePaymentResponse
from ingenico.connect.sdk.domain.payment.find_payments_response import FindPaymentsResponse
from ingenico.connect.sdk.domain.payment.payment_approval_response import PaymentApprovalResponse
from ingenico.connect.sdk.domain.payment.payment_error_response import PaymentErrorResponse
from ingenico.connect.sdk.domain.payment.payment_response import PaymentResponse
from ingenico.connect.sdk.domain.payment.third_party_status_response import ThirdPartyStatusResponse
from ingenico.connect.sdk.domain.refund.refund_error_response import RefundErrorResponse
from ingenico.connect.sdk.domain.refund.refund_response import RefundResponse
from ingenico.connect.sdk.domain.refund.refunds_response import RefundsResponse
from ingenico.connect.sdk.domain.token.create_token_response import CreateTokenResponse


class PaymentsClient(ApiResource):
    """
    Payments client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(PaymentsClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/payments - Create payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/create.html

        :param body:     :class:`ingenico.connect.sdk.domain.payment.create_payment_request.CreatePaymentRequest`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.create_payment_response.CreatePaymentResponse`
        :raise: DeclinedPaymentException if the Ingenico ePayments platform declined / rejected the payment. The payment result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/payments", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreatePaymentResponse,
                    context)

        except ResponseException as e:
            error_type = PaymentErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def find(self, query, context=None):
        """
        Resource /{merchantId}/payments - Find payments
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/find.html

        :param query:    :class:`ingenico.connect.sdk.merchant.payments.find_payments_params.FindPaymentsParams`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.find_payments_response.FindPaymentsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/payments", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    FindPaymentsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId} - Get payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/get.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.payment_response.PaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}", path_context)
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

    def complete(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/complete - Complete payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/complete.html

        :param payment_id:  str
        :param body:        :class:`ingenico.connect.sdk.domain.payment.complete_payment_request.CompletePaymentRequest`
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.complete_payment_response.CompletePaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/complete", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CompletePaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def third_party_status(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/thirdpartystatus - Third party status poll
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/thirdPartyStatus.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.third_party_status_response.ThirdPartyStatusResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/thirdpartystatus", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    ThirdPartyStatusResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def tokenize(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/tokenize - Create a token from payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/tokenize.html

        :param payment_id:  str
        :param body:        :class:`ingenico.connect.sdk.domain.payment.tokenize_payment_request.TokenizePaymentRequest`
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.token.create_token_response.CreateTokenResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/tokenize", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreateTokenResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def processchallenged(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/processchallenged - Approves challenged payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/processchallenged.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.payment_response.PaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/processchallenged", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    PaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def approve(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/approve - Approve payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/approve.html

        :param payment_id:  str
        :param body:        :class:`ingenico.connect.sdk.domain.payment.approve_payment_request.ApprovePaymentRequest`
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.payment_approval_response.PaymentApprovalResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/approve", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    PaymentApprovalResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def capture(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/capture - Capture payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/capture.html

        :param payment_id:  str
        :param body:        :class:`ingenico.connect.sdk.domain.payment.capture_payment_request.CapturePaymentRequest`
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.capture.capture_response.CaptureResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/capture", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CaptureResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancelapproval(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/cancelapproval - Undo capture payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/cancelapproval.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.cancel_approval_payment_response.CancelApprovalPaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/cancelapproval", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    CancelApprovalPaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def captures(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/captures - Get captures of payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/captures.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.capture.captures_response.CapturesResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/captures", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    CapturesResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def refund(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/refund - Create refund
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/refund.html

        :param payment_id:  str
        :param body:        :class:`ingenico.connect.sdk.domain.refund.refund_request.RefundRequest`
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.refund.refund_response.RefundResponse`
        :raise: DeclinedRefundException if the Ingenico ePayments platform declined / rejected the refund. The refund result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/refund", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    RefundResponse,
                    context)

        except ResponseException as e:
            error_type = RefundErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def refunds(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/refunds - Get refunds of payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/refunds.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.refund.refunds_response.RefundsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/refunds", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    RefundsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancel(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/cancel - Cancel payment
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/cancel.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payment.cancel_payment_response.CancelPaymentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    CancelPaymentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def dispute(self, payment_id, body, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/dispute - Create dispute
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/dispute.html

        :param payment_id:  str
        :param body:        :class:`ingenico.connect.sdk.domain.dispute.create_dispute_request.CreateDisputeRequest`
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.dispute.dispute_response.DisputeResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/dispute", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    DisputeResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def disputes(self, payment_id, context=None):
        """
        Resource /{merchantId}/payments/{paymentId}/disputes - Get disputes
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payments/disputes.html

        :param payment_id:  str
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.dispute.disputes_response.DisputesResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "paymentId": payment_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payments/{paymentId}/disputes", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    DisputesResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
