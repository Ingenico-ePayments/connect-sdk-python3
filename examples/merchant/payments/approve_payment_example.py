#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.payment.approve_payment_request import ApprovePaymentRequest
from ingenico.connect.sdk.domain.payment.definitions.approve_payment_non_sepa_direct_debit_payment_method_specific_input import ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.order_approve_payment import OrderApprovePayment
from ingenico.connect.sdk.domain.payment.definitions.order_references_approve_payment import OrderReferencesApprovePayment


class ApprovePaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            direct_debit_payment_method_specific_input = ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput()
            direct_debit_payment_method_specific_input.date_collect = "20150201"
            direct_debit_payment_method_specific_input.token = "bfa8a7e4-4530-455a-858d-204ba2afb77e"

            references = OrderReferencesApprovePayment()
            references.merchant_reference = "AcmeOrder0001"

            order = OrderApprovePayment()
            order.references = references

            body = ApprovePaymentRequest()
            body.amount = 2980
            body.direct_debit_payment_method_specific_input = direct_debit_payment_method_specific_input
            body.order = order

            response = client.merchant("merchantId").payments().approve("paymentId", body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
