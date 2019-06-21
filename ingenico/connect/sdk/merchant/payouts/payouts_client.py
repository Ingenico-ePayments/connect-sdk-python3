#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.payout.find_payouts_response import FindPayoutsResponse
from ingenico.connect.sdk.domain.payout.payout_error_response import PayoutErrorResponse
from ingenico.connect.sdk.domain.payout.payout_response import PayoutResponse


class PayoutsClient(ApiResource):
    """
    Payouts client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(PayoutsClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/payouts - Create payout
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payouts/create.html

        :param body:     :class:`ingenico.connect.sdk.domain.payout.create_payout_request.CreatePayoutRequest`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payout.payout_response.PayoutResponse`
        :raise: DeclinedPayoutException if the Ingenico ePayments platform declined / rejected the payout. The payout result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/payouts", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    PayoutResponse,
                    context)

        except ResponseException as e:
            error_type = PayoutErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def find(self, query, context=None):
        """
        Resource /{merchantId}/payouts - Find payouts
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payouts/find.html

        :param query:    :class:`ingenico.connect.sdk.merchant.payouts.find_payouts_params.FindPayoutsParams`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payout.find_payouts_response.FindPayoutsResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/payouts", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    FindPayoutsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, payout_id, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId} - Get payout
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payouts/get.html

        :param payout_id:  str
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payout.payout_response.PayoutResponse`
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payouts/{payoutId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PayoutResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def approve(self, payout_id, body, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId}/approve - Approve payout
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payouts/approve.html

        :param payout_id:  str
        :param body:       :class:`ingenico.connect.sdk.domain.payout.approve_payout_request.ApprovePayoutRequest`
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.payout.payout_response.PayoutResponse`
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payouts/{payoutId}/approve", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    PayoutResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancel(self, payout_id, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId}/cancel - Cancel payout
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payouts/cancel.html

        :param payout_id:  str
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payouts/{payoutId}/cancel", path_context)
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

    def cancelapproval(self, payout_id, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId}/cancelapproval - Undo approve payout
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/payouts/cancelapproval.html

        :param payout_id:  str
        :param context:    :class:`ingenico.connect.sdk.call_context.CallContext`
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/v1/{merchantId}/payouts/{payoutId}/cancelapproval", path_context)
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
