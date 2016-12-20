#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.token.create_token_response import CreateTokenResponse
from ingenico.connect.sdk.domain.token.token_response import TokenResponse


class TokensClient(ApiResource):
    """
    Tokens client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(TokensClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/tokens

        Create token
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__tokens_post

        :param body:     :class:`CreateTokenRequest`
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
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/tokens", None)
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
                403: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def delete(self, token_id, query, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId}

        Delete token
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__tokens__tokenId__delete

        :param token_id:  str
        :param query:     :class:`DeleteTokenParams`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/tokens/{tokenId}", path_context)
        try:
            return self._communicator.delete(
                    uri,
                    self._client_headers,
                    query,
                    None,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, token_id, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId}

        Get token
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__tokens__tokenId__get

        :param token_id:  str
        :return: :class:`TokenResponse`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/tokens/{tokenId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    TokenResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def update(self, token_id, body, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId}

        Update token
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__tokens__tokenId__put

        :param token_id:  str
        :param body:      :class:`UpdateTokenRequest`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/tokens/{tokenId}", path_context)
        try:
            return self._communicator.put(
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

    def approvesepadirectdebit(self, token_id, body, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId}/approvesepadirectdebit

        Approve SEPA DD mandate
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__tokens__tokenId__approvesepadirectdebit_post

        :param token_id:  str
        :param body:      :class:`ApproveTokenRequest`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/tokens/{tokenId}/approvesepadirectdebit", path_context)
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
