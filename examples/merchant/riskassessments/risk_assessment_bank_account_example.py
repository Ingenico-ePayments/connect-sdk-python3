#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/
#
import os

from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.riskassessments.risk_assessment_bank_account import RiskAssessmentBankAccount
from ingenico.connect.sdk.domain.riskassessments.definitions.customer_risk_assessment import CustomerRiskAssessment
from ingenico.connect.sdk.domain.riskassessments.definitions.order_risk_assessment import OrderRiskAssessment


class RiskAssessmentBankAccountExample(object):

    def example(self):
        with self.__get_client() as client:
            bank_account_bban = BankAccountBban()
            bank_account_bban.account_number = "0532013000"
            bank_account_bban.bank_code = "37040044"
            bank_account_bban.country_code = "DE"

            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 100
            amount_of_money.currency_code = "EUR"

            billing_address = Address()
            billing_address.country_code = "US"

            customer = CustomerRiskAssessment()
            customer.billing_address = billing_address
            customer.locale = "en_US"

            order = OrderRiskAssessment()
            order.amount_of_money = amount_of_money
            order.customer = customer

            body = RiskAssessmentBankAccount()
            body.bank_account_bban = bank_account_bban
            body.order = order

            response = client.merchant("merchantId").riskassessments().bankaccounts(body)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)
