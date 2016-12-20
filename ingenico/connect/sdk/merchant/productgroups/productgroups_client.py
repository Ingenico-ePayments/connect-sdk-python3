#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.product.payment_product_group_response import PaymentProductGroupResponse
from ingenico.connect.sdk.domain.product.payment_product_groups import PaymentProductGroups


class ProductgroupsClient(ApiResource):
    """
    Productgroups client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(ProductgroupsClient, self).__init__(parent, path_context)

    def find(self, query, context=None):
        """
        Resource /{merchantId}/productgroups

        Get payment product groups
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__productgroups_get

        :param query:    :class:`FindProductgroupsParams`
        :return: :class:`PaymentProductGroups`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/productgroups", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProductGroups,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, payment_product_group_id, query, context=None):
        """
        Resource /{merchantId}/productgroups/{paymentProductGroupId}

        Get payment product group
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__productgroups__paymentProductGroupId__get

        :param payment_product_group_id:  str
        :param query:                     :class:`GetProductgroupParams`
        :return: :class:`PaymentProductGroupResponse`
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
            "paymentProductGroupId": payment_product_group_id,
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/productgroups/{paymentProductGroupId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProductGroupResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
