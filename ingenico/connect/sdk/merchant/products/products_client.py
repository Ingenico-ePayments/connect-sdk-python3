#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.product.directory import Directory
from ingenico.connect.sdk.domain.product.payment_product_networks_response import PaymentProductNetworksResponse
from ingenico.connect.sdk.domain.product.payment_product_response import PaymentProductResponse
from ingenico.connect.sdk.domain.product.payment_products import PaymentProducts
from ingenico.connect.sdk.domain.publickey.public_key import PublicKey


class ProductsClient(ApiResource):
    """
    Products client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ApiResource`
        :param path_context: dict[str, str]
        """
        super(ProductsClient, self).__init__(parent, path_context)

    def find(self, query, context=None):
        """
        Resource /{merchantId}/products

        Get payment products
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products_get

        :param query:    :class:`FindProductsParams`
        :return: :class:`PaymentProducts`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the GlobalCollect platform,
                   the GlobalCollect platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the GlobalCollect platform returned any other error
        """
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/products", None)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProducts,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get(self, payment_product_id, query, context=None):
        """
        Resource /{merchantId}/products/{paymentProductId}

        Get payment product
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products__paymentProductId__get

        :param payment_product_id:  int
        :param query:               :class:`GetProductParams`
        :return: :class:`PaymentProductResponse`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/products/{paymentProductId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProductResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def directory(self, payment_product_id, query, context=None):
        """
        Resource /{merchantId}/products/{paymentProductId}/directory

        Get payment product directory
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products__paymentProductId__directory_get

        :param payment_product_id:  int
        :param query:               :class:`DirectoryParams`
        :return: :class:`Directory`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/products/{paymentProductId}/directory", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    Directory,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def networks(self, payment_product_id, query, context=None):
        """
        Resource /{merchantId}/products/{paymentProductId}/networks

        Get payment product networks
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products__paymentProductId__networks_get

        :param payment_product_id:  int
        :param query:               :class:`NetworksParams`
        :return: :class:`PaymentProductNetworksResponse`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/products/{paymentProductId}/networks", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProductNetworksResponse,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def public_key(self, payment_product_id, context=None):
        """
        Resource /{merchantId}/products/{paymentProductId}/publicKey

        Get payment product specific public key
        
        See also https://developer.globalcollect.com/documentation/api/server/#__merchantId__products__paymentProductId__publicKey_get

        :param payment_product_id:  int
        :return: :class:`PublicKey`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/{apiVersion}/{merchantId}/products/{paymentProductId}/publicKey", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    PublicKey,
                    context)

        except ResponseException as e:
            error_type = {
                404: ErrorResponse,
            }.get(e.status_code, ErrorResponse)
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
