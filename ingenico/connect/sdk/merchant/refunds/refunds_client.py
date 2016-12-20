#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.refund.refund_response import RefundResponse


class RefundsClient(ApiResource):
    """
    Refunds client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(RefundsClient, self).__init__(parent, path_context)

    def get(self, refund_id, context=None):
        """
        Resource /{merchantId}/refunds/{refundId}

        Get refund
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__refunds__refundId__get

        :param refund_id:  str
        :return: :class:`RefundResponse`
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/refunds/{refundId}", path_context)
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
        Resource /{merchantId}/refunds/{refundId}/approve

        Approve refund
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__refunds__refundId__approve_post

        :param refund_id:  str
        :param body:       :class:`ApproveRefundRequest`
        :return: None
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/refunds/{refundId}/approve", path_context)
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
        Resource /{merchantId}/refunds/{refundId}/cancel

        Cancel refund
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__refunds__refundId__cancel_post

        :param refund_id:  str
        :return: None
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/refunds/{refundId}/cancel", path_context)
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
        Resource /{merchantId}/refunds/{refundId}/cancelapproval

        Undo approve refund
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__refunds__refundId__cancelapproval_post

        :param refund_id:  str
        :return: None
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
            "refundId": refund_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/refunds/{refundId}/cancelapproval", path_context)
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
