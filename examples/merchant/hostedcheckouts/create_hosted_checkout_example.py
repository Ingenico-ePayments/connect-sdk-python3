#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.hostedcheckout.create_hosted_checkout_request import CreateHostedCheckoutRequest
from ingenico.connect.sdk.domain.hostedcheckout.definitions.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.order import Order


class CreateHostedCheckoutExample(object):

    def example(self):
        with self.__get_client() as client:
            hosted_checkout_specific_input = HostedCheckoutSpecificInput()
            hosted_checkout_specific_input.locale = "en_GB"
            hosted_checkout_specific_input.variant = "testVariant"

            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 2345
            amount_of_money.currency_code = "USD"

            billing_address = Address()
            billing_address.country_code = "US"

            customer = Customer()
            customer.billing_address = billing_address

            order = Order()
            order.amount_of_money = amount_of_money
            order.customer = customer

            body = CreateHostedCheckoutRequest()
            body.hosted_checkout_specific_input = hosted_checkout_specific_input
            body.order = order

            response = client.merchant("merchantId").hostedcheckouts().create(body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
