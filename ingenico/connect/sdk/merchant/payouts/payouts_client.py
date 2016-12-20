#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.payout.payout_error_response import PayoutErrorResponse
from ingenico.connect.sdk.domain.payout.payout_response import PayoutResponse


class PayoutsClient(ApiResource):
    """
    Payouts client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(PayoutsClient, self).__init__(parent, path_context)

    def create(self, body, context=None):
        """
        Resource /{merchantId}/payouts

        Create payout
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payouts_post

        :param body:     :class:`CreatePayoutRequest`
        :return: :class:`PayoutResponse`
        :raise: DeclinedPayoutException if the GlobalCollect platform declined / rejected the payout. The payout result will be available from the exception.
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payouts", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    PayoutResponse,
                    context)

        except ResponseException as e:
            error_type = {
                400: PayoutErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, payout_id, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId}

        Get payout
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payouts__payoutId__get

        :param payout_id:  str
        :return: :class:`PayoutResponse`
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payouts/{payoutId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PayoutResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def approve(self, payout_id, body, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId}/approve

        Approve payout
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payouts__payoutId__approve_post

        :param payout_id:  str
        :param body:       :class:`ApprovePayoutRequest`
        :return: :class:`PayoutResponse`
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payouts/{payoutId}/approve", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    PayoutResponse,
                    context)

        except ResponseException as e:
            error_type = {
                402: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancel(self, payout_id, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId}/cancel

        Cancel payout
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payouts__payoutId__cancel_post

        :param payout_id:  str
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payouts/{payoutId}/cancel", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    None,
                    context)

        except ResponseException as e:
            error_type = {
                402: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cancelapproval(self, payout_id, context=None):
        """
        Resource /{merchantId}/payouts/{payoutId}/cancelapproval

        Undo approve payout
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__payouts__payoutId__cancelapproval_post

        :param payout_id:  str
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
            "payoutId": payout_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/payouts/{payoutId}/cancelapproval", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    None,
                    context)

        except ResponseException as e:
            error_type = {
                405: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
