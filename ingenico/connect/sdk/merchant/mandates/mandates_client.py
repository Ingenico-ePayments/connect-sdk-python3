#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.mandates.create_mandate_response import CreateMandateResponse
from ingenico.connect.sdk.domain.mandates.get_mandate_response import GetMandateResponse


class MandatesClient(ApiResource):
    """
    Mandates client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(MandatesClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/mandates - Create mandate
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/mandates/create.html

        :param body:     :class:`ingenico.connect.sdk.domain.mandates.create_mandate_request.CreateMandateRequest`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.mandates.create_mandate_response.CreateMandateResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/mandates", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreateMandateResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def create_with_mandate_reference(self, unique_mandate_reference, body, context=None):
        """
        Resource /{merchantId}/mandates/{uniqueMandateReference} - Create mandate with mandatereference
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/mandates/createWithMandateReference.html

        :param unique_mandate_reference:  str
        :param body:                      :class:`ingenico.connect.sdk.domain.mandates.create_mandate_request.CreateMandateRequest`
        :param context:                   :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.mandates.create_mandate_response.CreateMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/mandates/{uniqueMandateReference}", path_context)
        try:
            return self._communicator.put(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreateMandateResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, unique_mandate_reference, context=None):
        """
        Resource /{merchantId}/mandates/{uniqueMandateReference} - Get mandate
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/mandates/get.html

        :param unique_mandate_reference:  str
        :param context:                   :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.mandates.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/mandates/{uniqueMandateReference}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    GetMandateResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def block(self, unique_mandate_reference, context=None):
        """
        Resource /{merchantId}/mandates/{uniqueMandateReference}/block - Block mandate
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/mandates/block.html

        :param unique_mandate_reference:  str
        :param context:                   :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.mandates.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/mandates/{uniqueMandateReference}/block", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    GetMandateResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def unblock(self, unique_mandate_reference, context=None):
        """
        Resource /{merchantId}/mandates/{uniqueMandateReference}/unblock - Unblock mandate
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/mandates/unblock.html

        :param unique_mandate_reference:  str
        :param context:                   :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.mandates.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/mandates/{uniqueMandateReference}/unblock", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    GetMandateResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def revoke(self, unique_mandate_reference, context=None):
        """
        Resource /{merchantId}/mandates/{uniqueMandateReference}/revoke - Revoke mandate
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/mandates/revoke.html

        :param unique_mandate_reference:  str
        :param context:                   :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.mandates.get_mandate_response.GetMandateResponse`
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
            "uniqueMandateReference": unique_mandate_reference,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/mandates/{uniqueMandateReference}/revoke", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    GetMandateResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
