#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.refund.find_refunds_response import FindRefundsResponse
from ingenico.connect.sdk.domain.refund.refund_response import RefundResponse


class RefundsClient(ApiResource):
    """
    Refunds client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(RefundsClient, self).__init__(parent, path_context)

    def find(self, query, context=None):
        """
        Resource /{merchantId}/refunds - Find refunds
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/refunds/find.html

        :param query:    :class:`ingenico.connect.sdk.merchant.refunds.find_refunds_params.FindRefundsParams`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.refund.find_refunds_response.FindRefundsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/refunds", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    FindRefundsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, refund_id, context=None):
        """
        Resource /{merchantId}/refunds/{refundId} - Get refund
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/refunds/get.html

        :param refund_id:  str
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.refund.refund_response.RefundResponse`
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/refunds/{refundId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    RefundResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def approve(self, refund_id, body, context=None):
        """
        Resource /{merchantId}/refunds/{refundId}/approve - Approve refund
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/refunds/approve.html

        :param refund_id:  str
        :param body:       :class:`ingenico.connect.sdk.domain.refund.approve_refund_request.ApproveRefundRequest`
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: None
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/refunds/{refundId}/approve", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    None,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancel(self, refund_id, context=None):
        """
        Resource /{merchantId}/refunds/{refundId}/cancel - Cancel refund
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/refunds/cancel.html

        :param refund_id:  str
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: None
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/refunds/{refundId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    None,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancelapproval(self, refund_id, context=None):
        """
        Resource /{merchantId}/refunds/{refundId}/cancelapproval - Undo approve refund
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/refunds/cancelapproval.html

        :param refund_id:  str
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: None
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/refunds/{refundId}/cancelapproval", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    None,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
