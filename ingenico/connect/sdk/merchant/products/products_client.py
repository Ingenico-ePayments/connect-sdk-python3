#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.response_exception import ResponseException
from ingenico.connect.sdk.domain.errors.error_response import ErrorResponse
from ingenico.connect.sdk.domain.product.device_fingerprint_response import DeviceFingerprintResponse
from ingenico.connect.sdk.domain.product.directory import Directory
from ingenico.connect.sdk.domain.product.get_customer_details_response import GetCustomerDetailsResponse
from ingenico.connect.sdk.domain.product.payment_product_networks_response import PaymentProductNetworksResponse
from ingenico.connect.sdk.domain.product.payment_product_response import PaymentProductResponse
from ingenico.connect.sdk.domain.product.payment_products import PaymentProducts


class ProductsClient(ApiResource):
    """
    Products client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.connect.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(ProductsClient, self).__init__(parent, path_context)

    def find(self, query, context=None):
        """
        Resource /{merchantId}/products - Get payment products
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/find.html

        :param query:    :class:`ingenico.connect.sdk.merchant.products.find_products_params.FindProductsParams`
        :param context:  :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.product.payment_products.PaymentProducts`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: GlobalCollectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v1/{merchantId}/products", None)
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
        Resource /{merchantId}/products/{paymentProductId} - Get payment product
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/get.html

        :param payment_product_id:  int
        :param query:               :class:`ingenico.connect.sdk.merchant.products.get_product_params.GetProductParams`
        :param context:             :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.product.payment_product_response.PaymentProductResponse`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v1/{merchantId}/products/{paymentProductId}", path_context)
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
        Resource /{merchantId}/products/{paymentProductId}/directory - Get payment product directory
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/directory.html

        :param payment_product_id:  int
        :param query:               :class:`ingenico.connect.sdk.merchant.products.directory_params.DirectoryParams`
        :param context:             :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.product.directory.Directory`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v1/{merchantId}/products/{paymentProductId}/directory", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    Directory,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def customer_details(self, payment_product_id, body, context=None):
        """
        Resource /{merchantId}/products/{paymentProductId}/customerDetails - Get customer details
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/customerDetails.html

        :param payment_product_id:  int
        :param body:                :class:`ingenico.connect.sdk.domain.product.get_customer_details_request.GetCustomerDetailsRequest`
        :param context:             :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.product.get_customer_details_response.GetCustomerDetailsResponse`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v1/{merchantId}/products/{paymentProductId}/customerDetails", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    GetCustomerDetailsResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def device_fingerprint(self, payment_product_id, body, context=None):
        """
        Resource /{merchantId}/products/{paymentProductId}/deviceFingerprint - Get device fingerprint
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/deviceFingerprint.html

        :param payment_product_id:  int
        :param body:                :class:`ingenico.connect.sdk.domain.product.device_fingerprint_request.DeviceFingerprintRequest`
        :param context:             :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.product.device_fingerprint_response.DeviceFingerprintResponse`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v1/{merchantId}/products/{paymentProductId}/deviceFingerprint", path_context)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    DeviceFingerprintResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def networks(self, payment_product_id, query, context=None):
        """
        Resource /{merchantId}/products/{paymentProductId}/networks - Get payment product networks
        
        See also https://epayments-api.developer-ingenico.com/s2sapi/v1/en_US/python/products/networks.html

        :param payment_product_id:  int
        :param query:               :class:`ingenico.connect.sdk.merchant.products.networks_params.NetworksParams`
        :param context:             :class:`ingenico.connect.sdk.call_context.CallContext`
        :return: :class:`ingenico.connect.sdk.domain.product.payment_product_networks_response.PaymentProductNetworksResponse`
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
            "paymentProductId": str(payment_product_id),
        }
        uri = self._instantiate_uri("/v1/{merchantId}/products/{paymentProductId}/networks", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    query,
                    PaymentProductNetworksResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
