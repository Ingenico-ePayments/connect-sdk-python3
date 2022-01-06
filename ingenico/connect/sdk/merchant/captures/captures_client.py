#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.capture.capture_response import CaptureResponse
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.refund.refund_error_response import RefundErrorResponse
from ingenico.connect.sdk.domain.refund.refund_response import RefundResponse


class CapturesClient(ApiResource):
    """
    Captures client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(CapturesClient, self).__init__(parent, path_context)

    def get(self, capture_id, context=None):
        """
        Resource /{merchantId}/captures/{captureId} - Get capture
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/captures/get.html

        :param capture_id:  str
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
            "captureId": capture_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/captures/{captureId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    CaptureResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def refund(self, capture_id, body, context=None):
        """
        Resource /{merchantId}/captures/{captureId}/refund - Create Refund
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/captures/refund.html

        :param capture_id:  str
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
            "captureId": capture_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/captures/{captureId}/refund", path_context)
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
