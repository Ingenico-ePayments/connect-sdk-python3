#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.merchant.services.convert_amount_params import ConvertAmountParams


class ConvertAmountExample(object):

    def example(self):
        with self.__get_client() as client:
            query = ConvertAmountParams()
            query.source = "EUR"
            query.target = "USD"
            query.amount = 100

            response = client.merchant("merchantId").services().convert_amount(query)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
