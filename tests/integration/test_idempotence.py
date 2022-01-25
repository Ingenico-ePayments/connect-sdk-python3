import unittest
import uuid
import tests.integration.init_utils as init_utils
from tests.integration.init_utils import MERCHANT_ID
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.payment.create_payment_request import CreatePaymentRequest
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_method_specific_input import \
    RedirectPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.redirect_payment_product809_specific_input import \
    RedirectPaymentProduct809SpecificInput
from ingenico.connect.sdk.call_context import CallContext
from ingenico.connect.sdk.declined_payment_exception import DeclinedPaymentException


class IdempotenceTest(unittest.TestCase):
    """Test that the client can successfully detect that an idempotent request is sent twice"""
    def test_idempotence(self):
        """Test that the client can successfully detect that an idempotent request is sent twice"""

        amount_of_money = AmountOfMoney()
        amount_of_money.currency_code = "EUR"
        amount_of_money.amount = 100
        billing_address = Address()
        billing_address.country_code = "NL"
        customer = Customer()
        customer.locale = "en"
        customer.billing_address = billing_address
        order = Order()
        order.amount_of_money = amount_of_money
        order.customer = customer
        payment_product_input = RedirectPaymentProduct809SpecificInput()
        payment_product_input.issuer_id = "INGBNL2A"
        payment_method_input = RedirectPaymentMethodSpecificInput()
        payment_method_input.return_url = "http://example.com"
        payment_method_input.payment_product_id = 809
        payment_method_input.payment_product809_specific_input = payment_product_input
        body = CreatePaymentRequest()
        body.order = order
        body.redirect_payment_method_specific_input = payment_method_input
        idempotence_key = str(uuid.uuid4())
        context = CallContext(idempotence_key)

        with init_utils.create_client() as client:
            def do_create_payment():
                # For this test it doesn't matter if the response is successful or declined,
                # as long as idempotence is handled correctly
                try:
                    return client.merchant(MERCHANT_ID).payments().create(body, context)
                except DeclinedPaymentException as e:
                    return e.create_payment_result

            result = do_create_payment()

            payment_id = result.payment.id
            status = result.payment.status

            self.assertEqual(idempotence_key, context.idempotence_key)
            self.assertIsNone(context.idempotence_request_timestamp)

            result_2 = do_create_payment()

            payment_id_2 = result_2.payment.id
            status_2 = result_2.payment.status
            self.assertEqual(payment_id, payment_id_2)
            self.assertEqual(status, status_2)
            self.assertEqual(idempotence_key, context.idempotence_key)
            self.assertIsNotNone(context.idempotence_request_timestamp)


if __name__ == '__main__':
    unittest.main()
