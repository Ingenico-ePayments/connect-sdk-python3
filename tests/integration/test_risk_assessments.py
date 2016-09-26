import unittest

from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.bank_account_bban import BankAccountBban
from ingenico.connect.sdk.domain.riskassessments.definitions.customer_risk_assessment import \
    CustomerRiskAssessment
from ingenico.connect.sdk.domain.riskassessments.definitions.order_risk_assessment import OrderRiskAssessment
from ingenico.connect.sdk.domain.riskassessments.risk_assessment_bank_account import RiskAssessmentBankAccount
from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID


class RiskAssessmentsTest(unittest.TestCase):
    """Test if the risk assessments service functions"""
    def test_risk_assessments(self):
        """Test if the risk assessments service functions"""
        bank_account_bban = BankAccountBban()
        bank_account_bban.country_code = "DE"
        bank_account_bban.account_number = "0532013000"
        bank_account_bban.bank_code = "37040044"
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = 100
        amount_of_money.currency_code = "EUR"
        customer = CustomerRiskAssessment()
        customer.locale = "en_GB"
        order = OrderRiskAssessment()
        order.amount_of_money = amount_of_money
        order.customer = customer
        body = RiskAssessmentBankAccount()
        body.order = order
        body.bank_account_bban = bank_account_bban

        with init_utils.create_client() as client:
            response = client.merchant(MERCHANT_ID).riskassessments().bankaccounts(body)
        self.assertGreater(len(response.results), 0)


if __name__ == '__main__':
    unittest.main()
