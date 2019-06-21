#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse


class FilesClient(ApiResource):
    """
    Files client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(FilesClient, self).__init__(parent, path_context)

    def get_file(self, file_id, context=None):
        """
        Resource /{merchantId}/files/{fileId} - Retrieve File
        
        See also https://epayments-api.developer-ingenico.com/fileserviceapi/v1/en_US/python/files/getFile.html

        :param file_id:  str
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: a tuple with the headers and a generator of body chunks
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
            "fileId": file_id,
        }
        uri = self._instantiate_uri("/files/v1/{merchantId}/files/{fileId}", path_context)
        try:
            return self._communicator.get_with_binary_response(
                    uri,
                    self._client_headers,
                    None,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
