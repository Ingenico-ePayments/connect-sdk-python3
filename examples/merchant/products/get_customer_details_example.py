#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.key_value_pair import KeyValuePair
from ingenico.connect.sdk.domain.product.get_customer_details_request import GetCustomerDetailsRequest


class GetCustomerDetailsExample(object):

    def example(self):
        with self.__get_client() as client:
            values = []

            value1 = KeyValuePair()
            value1.key = "fiscalNumber"
            value1.value = "01234567890"

            values.append(value1)

            body = GetCustomerDetailsRequest()
            body.country_code = "SE"
            body.values = values

            response = client.merchant("merchantId").products().customer_details(9000, body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
