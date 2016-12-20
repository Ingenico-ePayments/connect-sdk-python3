#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.services.bank_details_response import BankDetailsResponse
from ingenico.connect.sdk.domain.services.convert_amount import ConvertAmount
from ingenico.connect.sdk.domain.services.get_iin_details_response import GetIINDetailsResponse
from ingenico.connect.sdk.domain.services.test_connection import TestConnection


class ServicesClient(ApiResource):
    """
    Services client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(ServicesClient, self).__init__(parent, path_context)

    def convert_amount(self, query, context=None):
        """
        Resource /{merchantId}/services/convert/amount

        Convert amount
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__services_convert_amount_get

        :param query:    :class:`ConvertAmountParams`
        :return: :class:`ConvertAmount`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/services/convert/amount", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    ConvertAmount,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def convertAmount(self, query, context=None):
        """
        Deprecated. Use convert_amount instead.
        """
        return self.convert_amount(query, context)

    def bankaccount(self, body, context=None):
        """
        Resource /{merchantId}/services/convert/bankaccount

        Convert Bankaccount
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__services_convert_bankaccount_post

        :param body:     :class:`BankDetailsRequest`
        :return: :class:`BankDetailsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/services/convert/bankaccount", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    BankDetailsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_iin_details(self, body, context=None):
        """
        Resource /{merchantId}/services/getIINdetails

        Get IIN details
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__services_getIINdetails_post

        :param body:     :class:`GetIINDetailsRequest`
        :return: :class:`GetIINDetailsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/services/getIINdetails", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    GetIINDetailsResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def getIINdetails(self, body, context=None):
        """
        Deprecated. Use get_iin_details instead.
        """
        return self.get_iin_details(body, context)

    def testconnection(self, context=None):
        """
        Resource /{merchantId}/services/testconnection

        Test connection
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__services_testconnection_get

        :return: :class:`TestConnection`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/services/testconnection", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    TestConnection,
                    context)

        except ResponseException as e:
            error_type = {
                403: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
