#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
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
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(TokensClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/tokens - Create token
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/tokens/create.html

        :param body:     :class:`ingenico.connect.sdk.domain.token.create_token_request.CreateTokenRequest`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
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
        uri = self._instantiate_uri("/v1/{merchantId}/tokens", None)
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

    def get(self, token_id, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId} - Get token
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/tokens/get.html

        :param token_id:  str
        :param context:   :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.token.token_response.TokenResponse`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/tokens/{tokenId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    TokenResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def update(self, token_id, body, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId} - Update token
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/tokens/update.html

        :param token_id:  str
        :param body:      :class:`ingenico.connect.sdk.domain.token.update_token_request.UpdateTokenRequest`
        :param context:   :class:`ingenico.connect.sdk.call_context.CallContext`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/tokens/{tokenId}", path_context)
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

    def delete(self, token_id, query, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId} - Delete token
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/tokens/delete.html

        :param token_id:  str
        :param query:     :class:`ingenico.connect.sdk.merchant.tokens.delete_token_params.DeleteTokenParams`
        :param context:   :class:`ingenico.connect.sdk.call_context.CallContext`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/tokens/{tokenId}", path_context)
        try:
            return self._communicator.delete(
                    uri,
                    self._client_headers,
                    query,
                    None,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def approvesepadirectdebit(self, token_id, body, context=None):
        """
        Resource /{merchantId}/tokens/{tokenId}/approvesepadirectdebit - Approve SEPA DD mandate
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/tokens/approvesepadirectdebit.html

        :param token_id:  str
        :param body:      :class:`ingenico.connect.sdk.domain.token.approve_token_request.ApproveTokenRequest`
        :param context:   :class:`ingenico.connect.sdk.call_context.CallContext`
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
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/tokens/{tokenId}/approvesepadirectdebit", path_context)
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
