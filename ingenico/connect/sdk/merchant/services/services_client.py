#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.services.bank_details_response import BankDetailsResponse
from ingenico.connect.sdk.domain.services.convert_amount import ConvertAmount
from ingenico.connect.sdk.domain.services.get_iin_details_response import GetIINDetailsResponse
from ingenico.connect.sdk.domain.services.get_privacy_policy_response import GetPrivacyPolicyResponse
from ingenico.connect.sdk.domain.services.test_connection import TestConnection


class ServicesClient(ApiResource):
    """
    Services client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(ServicesClient, self).__init__(parent, path_context)

    def convert_amount(self, query, context=None):
        """
        Resource /{merchantId}/services/convert/amount - Convert amount
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/services/convertAmount.html

        :param query:    :class:`ingenico.connect.sdk.merchant.services.convert_amount_params.ConvertAmountParams`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.services.convert_amount.ConvertAmount`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/services/convert/amount", None)
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

    def bankaccount(self, body, context=None):
        """
        Resource /{merchantId}/services/convert/bankaccount - Convert bankaccount
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/services/bankaccount.html

        :param body:     :class:`ingenico.connect.sdk.domain.services.bank_details_request.BankDetailsRequest`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.services.bank_details_response.BankDetailsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/services/convert/bankaccount", None)
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
        Resource /{merchantId}/services/getIINdetails - Get IIN details
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/services/getIINdetails.html

        :param body:     :class:`ingenico.connect.sdk.domain.services.get_iin_details_request.GetIINDetailsRequest`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.services.get_iin_details_response.GetIINDetailsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/services/getIINdetails", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    GetIINDetailsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def privacypolicy(self, query, context=None):
        """
        Resource /{merchantId}/services/privacypolicy - Get privacy policy
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/services/privacypolicy.html

        :param query:    :class:`ingenico.connect.sdk.merchant.services.privacypolicy_params.PrivacypolicyParams`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.services.get_privacy_policy_response.GetPrivacyPolicyResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/services/privacypolicy", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    GetPrivacyPolicyResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def testconnection(self, context=None):
        """
        Resource /{merchantId}/services/testconnection - Test connection
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/services/testconnection.html

        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.services.test_connection.TestConnection`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/services/testconnection", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    TestConnection,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
