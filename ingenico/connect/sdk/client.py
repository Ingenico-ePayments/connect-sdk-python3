#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
from base64 import b64encode
from ingenico.connect.sdk.api_resource import ApiResource
from ingenico.connect.sdk.log.logging_capable import LoggingCapable
from ingenico.connect.sdk.merchant.merchant_client import MerchantClient


class Client(ApiResource, LoggingCapable):
    """
    Ingenico ePayments platform client.
    
    This client and all its child clients are bound to one specific value for the X-GCS-ClientMetaInfo header.
    To get a new client with a different header value, use with_client_meta_info.
    
    Thread-safe.
    """

    @staticmethod
    def API_VERSION():
        return "v1"

    def __init__(self, communicator, client_meta_info=None):
        """
        :param communicator:      :class:`ingenico.connect.sdk.communicator.Communicator`
        :param client_meta_info:  str
        """
        super(Client, self).__init__(communicator, None, client_meta_info)

    def with_client_meta_info(self, client_meta_info):
        """
        :param client_meta_info: JSON string containing the meta data for the client
        :return: a new Client which uses the passed meta data for the X-GCS-ClientMetaInfo header.
        :raise: MarshallerSyntaxException if the given clientMetaInfo is not a valid JSON string
        """
        if self._client_meta_info is None and client_meta_info is None:
            return self
        elif client_meta_info is None:
            return Client(self._communicator, None)
        else:
            # Checking to see if this is valid JSON (no JSON parse exceptions)
            self._communicator.marshaller.unmarshal(client_meta_info, object)
            client_meta_info = b64encode(client_meta_info.encode('UTF-8'))
            if client_meta_info == self._client_meta_info:
                return self
            else:
                return Client(self._communicator, client_meta_info)

    def close_idle_connections(self, idle_time):
        """
        Utility method that delegates the call to this client's communicator.

        :param idle_time: a datetime.timedelta object indicating the idle time
        """
        self._communicator.close_idle_connections(idle_time)

    def close_expired_connections(self):
        """
        Utility method that delegates the call to this client's communicator.
        """
        self._communicator.close_expired_connections()

    def enable_logging(self, communicator_logger):
        # delegate to the communicator
        self._communicator.enable_logging(communicator_logger)

    def disable_logging(self):
        # delegate to the communicator
        self._communicator.disable_logging()

    def close(self):
        """
        Releases any system resources associated with this object.
        """
        self._communicator.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def merchant(self, merchant_id):
        """
        Resource /{merchantId}

        :param merchant_id:  str
        :return: :class:`ingenico.connect.sdk.merchant.merchant_client.MerchantClient`
        """
        sub_context = {
            "merchantId": merchant_id,
        }
        return MerchantClient(self, sub_context)
