#
# This class was auto-generated from the API references found at
# https://epayments-api.developer-ingenico.com/s2sapi/v1/
#
import os

from ingenico.connect.sdk.api_exception import ApiException
from ingenico.connect.sdk.declined_payment_exception import DeclinedPaymentException
from ingenico.connect.sdk.factory import Factory
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.definitions.company_information import CompanyInformation
from ingenico.connect.sdk.domain.payment.create_payment_request import CreatePaymentRequest
from ingenico.connect.sdk.domain.payment.definitions.address_personal import AddressPersonal
from ingenico.connect.sdk.domain.payment.definitions.browser_data import BrowserData
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.contact_details import ContactDetails
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.customer_device import CustomerDevice
from ingenico.connect.sdk.domain.payment.definitions.line_item import LineItem
from ingenico.connect.sdk.domain.payment.definitions.line_item_invoice_data import LineItemInvoiceData
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.domain.payment.definitions.order_invoice_data import OrderInvoiceData
from ingenico.connect.sdk.domain.payment.definitions.order_references import OrderReferences
from ingenico.connect.sdk.domain.payment.definitions.personal_information import PersonalInformation
from ingenico.connect.sdk.domain.payment.definitions.personal_name import PersonalName
from ingenico.connect.sdk.domain.payment.definitions.redirection_data import RedirectionData
from ingenico.connect.sdk.domain.payment.definitions.shipping import Shipping
from ingenico.connect.sdk.domain.payment.definitions.shopping_cart import ShoppingCart
from ingenico.connect.sdk.domain.payment.definitions.three_d_secure import ThreeDSecure


class CreatePaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            card = Card()
            card.card_number = "4567350000427977"
            card.cardholder_name = "Wile E. Coyote"
            card.cvv = "123"
            card.expiry_date = "1299"

            authentication_amount = AmountOfMoney()
            authentication_amount.amount = 2980
            authentication_amount.currency_code = "EUR"

            redirection_data = RedirectionData()
            redirection_data.return_url = "https://hostname.myownwebsite.url"

            three_d_secure = ThreeDSecure()
            three_d_secure.authentication_amount = authentication_amount
            three_d_secure.authentication_flow = "browser"
            three_d_secure.challenge_canvas_size = "600x400"
            three_d_secure.challenge_indicator = "challenge-requested"
            three_d_secure.exemption_request = "none"
            three_d_secure.redirection_data = redirection_data
            three_d_secure.skip_authentication = False

            card_payment_method_specific_input = CardPaymentMethodSpecificInput()
            card_payment_method_specific_input.card = card
            card_payment_method_specific_input.is_recurring = False
            card_payment_method_specific_input.merchant_initiated_reason_indicator = "delayedCharges"
            card_payment_method_specific_input.payment_product_id = 1
            card_payment_method_specific_input.three_d_secure = three_d_secure
            card_payment_method_specific_input.transaction_channel = "ECOMMERCE"

            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 2980
            amount_of_money.currency_code = "EUR"

            billing_address = Address()
            billing_address.additional_info = "b"
            billing_address.city = "Monument Valley"
            billing_address.country_code = "US"
            billing_address.house_number = "13"
            billing_address.state = "Utah"
            billing_address.street = "Desertroad"
            billing_address.zip = "84536"

            company_information = CompanyInformation()
            company_information.name = "Acme Labs"
            company_information.vat_number = "1234AB5678CD"

            contact_details = ContactDetails()
            contact_details.email_address = "wile.e.coyote@acmelabs.com"
            contact_details.fax_number = "+1234567891"
            contact_details.phone_number = "+1234567890"

            browser_data = BrowserData()
            browser_data.color_depth = 24
            browser_data.java_enabled = False
            browser_data.screen_height = "1200"
            browser_data.screen_width = "1920"

            device = CustomerDevice()
            device.accept_header = "texthtml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            device.browser_data = browser_data
            device.ip_address = "123.123.123.123"
            device.locale = "en-US"
            device.timezone_offset_utc_minutes = "420"
            device.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15"

            name = PersonalName()
            name.first_name = "Wile"
            name.surname = "Coyote"
            name.surname_prefix = "E."
            name.title = "Mr."

            personal_information = PersonalInformation()
            personal_information.date_of_birth = "19490917"
            personal_information.gender = "male"
            personal_information.name = name

            customer = Customer()
            customer.account_type = "none"
            customer.billing_address = billing_address
            customer.company_information = company_information
            customer.contact_details = contact_details
            customer.device = device
            customer.locale = "en_US"
            customer.merchant_customer_id = "1234"
            customer.personal_information = personal_information

            invoice_data = OrderInvoiceData()
            invoice_data.invoice_date = "20140306191500"
            invoice_data.invoice_number = "000000123"

            references = OrderReferences()
            references.descriptor = "Fast and Furry-ous"
            references.invoice_data = invoice_data
            references.merchant_order_id = 123456
            references.merchant_reference = "AcmeOrder0001"

            shipping_name = PersonalName()
            shipping_name.first_name = "Road"
            shipping_name.surname = "Runner"
            shipping_name.title = "Miss"

            address = AddressPersonal()
            address.additional_info = "Suite II"
            address.city = "Monument Valley"
            address.country_code = "US"
            address.house_number = "1"
            address.name = shipping_name
            address.state = "Utah"
            address.street = "Desertroad"
            address.zip = "84536"

            shipping = Shipping()
            shipping.address = address

            items = []

            item1_amount_of_money = AmountOfMoney()
            item1_amount_of_money.amount = 2500
            item1_amount_of_money.currency_code = "EUR"

            item1_invoice_data = LineItemInvoiceData()
            item1_invoice_data.description = "ACME Super Outfit"
            item1_invoice_data.nr_of_items = "1"
            item1_invoice_data.price_per_item = 2500

            item1 = LineItem()
            item1.amount_of_money = item1_amount_of_money
            item1.invoice_data = item1_invoice_data

            items.append(item1)

            item2_amount_of_money = AmountOfMoney()
            item2_amount_of_money.amount = 480
            item2_amount_of_money.currency_code = "EUR"

            item2_invoice_data = LineItemInvoiceData()
            item2_invoice_data.description = "Aspirin"
            item2_invoice_data.nr_of_items = "12"
            item2_invoice_data.price_per_item = 40

            item2 = LineItem()
            item2.amount_of_money = item2_amount_of_money
            item2.invoice_data = item2_invoice_data

            items.append(item2)

            shopping_cart = ShoppingCart()
            shopping_cart.items = items

            order = Order()
            order.amount_of_money = amount_of_money
            order.customer = customer
            order.references = references
            order.shipping = shipping
            order.shopping_cart = shopping_cart

            body = CreatePaymentRequest()
            body.card_payment_method_specific_input = card_payment_method_specific_input
            body.order = order

            try:
                response = client.merchant("merchantId").payments().create(body)
            except DeclinedPaymentException as e:
                self.handle_declined_payment(e.create_payment_result)
            except ApiException as e:
                self.handle_api_errors(e.errors)

    def __get_client(self):
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name=configuration_file_name,
                                               api_key_id=api_key_id, secret_api_key=secret_api_key)

    def handle_declined_payment(self, create_payment_result):
        # handle the result here
        pass

    def handle_api_errors(self, errors):
        # handle the errors here
        pass
