#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.riskassessments.risk_assessment_response import RiskAssessmentResponse


class RiskassessmentsClient(ApiResource):
    """
    Riskassessments client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(RiskassessmentsClient, self).__init__(parent, path_context)

    def bankaccounts(self, body, context=None):
        """
        Resource /{merchantId}/riskassessments/bankaccounts

        Risk-assess bank account
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__riskassessments_bankaccounts_post

        :param body:     :class:`RiskAssessmentBankAccount`
        :return: :class:`RiskAssessmentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/riskassessments/bankaccounts", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    RiskAssessmentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def cards(self, body, context=None):
        """
        Resource /{merchantId}/riskassessments/cards

        Risk-assess card
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__riskassessments_cards_post

        :param body:     :class:`RiskAssessmentCard`
        :return: :class:`RiskAssessmentResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/riskassessments/cards", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    RiskAssessmentResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
