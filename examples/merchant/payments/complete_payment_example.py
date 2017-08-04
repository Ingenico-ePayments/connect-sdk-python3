#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.card_without_cvv import CardWithoutCvv
from ingenico.connect.sdk.domain.payment.complete_payment_request import CompletePaymentRequest
from ingenico.connect.sdk.domain.payment.definitions.complete_payment_card_payment_method_specific_input import CompletePaymentCardPaymentMethodSpecificInput


class CompletePaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            card = CardWithoutCvv()
            card.card_number = "67030000000000003"
            card.cardholder_name = "Wile E. Coyote"
            card.expiry_date = "1220"

            card_payment_method_specific_input = CompletePaymentCardPaymentMethodSpecificInput()
            card_payment_method_specific_input.card = card

            body = CompletePaymentRequest()
            body.card_payment_method_specific_input = card_payment_method_specific_input

            response = client.merchant("merchantId").payments().complete("paymentId", body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
