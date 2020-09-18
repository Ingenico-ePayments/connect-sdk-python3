#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.product.create_payment_product_session_request import CreatePaymentProductSessionRequest
from ingenico.connect.sdk.domain.product.definitions.mobile_payment_product_session302_specific_input import MobilePaymentProductSession302SpecificInput


class CreatePaymentProductSessionExample(object):

    def example(self):
        with self.__get_client() as client:
            payment_product_session302_specific_input = MobilePaymentProductSession302SpecificInput()
            payment_product_session302_specific_input.display_name = "Ingenico"
            payment_product_session302_specific_input.domain_name = "pay1.secured-by-ingenico.com"
            payment_product_session302_specific_input.validation_url = "<VALIDATION URL RECEIVED FROM APPLE>"

            body = CreatePaymentProductSessionRequest()
            body.payment_product_session302_specific_input = payment_product_session302_specific_input

            response = client.merchant("merchantId").products().sessions(302, body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
