#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.dispute.dispute_response import DisputeResponse
from ingenico.connect.sdk.domain.dispute.upload_dispute_file_response import UploadDisputeFileResponse
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse


class DisputesClient(ApiResource):
    """
    Disputes client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(DisputesClient, self).__init__(parent, path_context)

    def get(self, dispute_id, context=None):
        """
        Resource /{merchantId}/disputes/{disputeId} - Get dispute
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/disputes/get.html

        :param dispute_id:  str
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
            "disputeId": dispute_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/disputes/{disputeId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    DisputeResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def submit(self, dispute_id, context=None):
        """
        Resource /{merchantId}/disputes/{disputeId}/submit - Submit dispute
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/disputes/submit.html

        :param dispute_id:  str
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
            "disputeId": dispute_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/disputes/{disputeId}/submit", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    DisputeResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancel(self, dispute_id, context=None):
        """
        Resource /{merchantId}/disputes/{disputeId}/cancel - Cancel dispute
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/disputes/cancel.html

        :param dispute_id:  str
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
            "disputeId": dispute_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/disputes/{disputeId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    DisputeResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def upload_file(self, dispute_id, body, context=None):
        """
        Resource /{merchantId}/disputes/{disputeId} - Upload File
        
        See also https://epayments-api.developer-ingenico.com/fileserviceapi/v1/en_US/python/disputes/uploadFile.html

        :param dispute_id:  str
        :param body:        :class:`ingenico.connect.sdk.merchant.disputes.upload_file_request.UploadFileRequest`
        :param context:     :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.dispute.upload_dispute_file_response.UploadDisputeFileResponse`
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
            "disputeId": dispute_id,
        }
        uri = self._instantiate_uri("/files/v1/{merchantId}/disputes/{disputeId}", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    UploadDisputeFileResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
