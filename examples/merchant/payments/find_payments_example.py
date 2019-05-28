#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.merchant.payments.find_payments_params import FindPaymentsParams


class FindPaymentsExample(object):

    def example(self):
        with self.__get_client() as client:
            query = FindPaymentsParams()
            query.hosted_checkout_id = "15c09dac-bf44-486a-af6b-edfd8680a166"
            query.merchant_reference = "AcmeOrder0001"
            query.merchant_order_id = 123456
            query.offset = 0
            query.limit = 10

            response = client.merchant("merchantId").payments().find(query)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
