#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.sessions.session_response import SessionResponse


class SessionsClient(ApiResource):
    """
    Sessions client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(SessionsClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/sessions - Create session
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/sessions/create.html

        :param body:     :class:`ingenico.connect.sdk.domain.sessions.session_request.SessionRequest`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.sessions.session_response.SessionResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/sessions", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    SessionResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
