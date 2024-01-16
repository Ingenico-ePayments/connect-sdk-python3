#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.merchant.productgroups.get_productgroup_params import GetProductgroupParams


class GetPaymentProductGroupExample(object):

    def example(self):
        with self.__get_client() as client:
            query = GetProductgroupParams()
            query.country_code = "US"
            query.currency_code = "USD"
            query.locale = "en_US"
            query.amount = 1000
            query.is_recurring = True
            query.add_hide("fields")

            response = client.merchant("merchantId").productgroups().get("cards", query)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
