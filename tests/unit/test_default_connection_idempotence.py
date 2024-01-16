import unittest
import uuid
import time
import os

import tests.file_utils as file_utils
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.payment.create_payment_request import CreatePaymentRequest
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.call_context import CallContext
from ingenico.connect.sdk.declined_payment_exception import DeclinedPaymentException
from ingenico.connect.sdk.idempotence_exception import IdempotenceException
from tests.unit.server_mock_utils import create_server_listening, create_client


class DefaultConnectionIdempotenceTest(unittest.TestCase):
    """
    Tests that sending the same request twice using DefaultConnection
     has the same effect as only sending one request
    """

    def setUp(self):
        # The server path the request arrived at
        self.request_path = None
        # Stores the idempotence header received at the server side
        self.idempotence_header = "unset"

    def test_idempotence_first_request(self):
        """Test a request with idempotence key where the first request is successful"""
        response_body = read_resource("idempotence_success.json")
        idempotence_key = str(uuid.uuid4())
        call_context = CallContext(idempotence_key)
        request = create_payment_request()
        test_path = "/v1/20000/payments"  # relative url through which the request should be sent
        additional_headers \
            = (("Content-Type", "application/json"),
               ("Location", "http://localhost/v1/20000/payments/000002000020142549460000100001"))
        handler = self.create_handler(response_code=201, body=response_body,
                                      additional_headers=additional_headers)
        with create_server_listening(handler) as address:
            with create_client(address) as client:
                response = client.merchant("20000").payments().create(request, call_context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at the wrong path')
        self.assertEqual(idempotence_key, self.idempotence_header,
                         "Wrong idempotence key is sent in the request")
        self.assertEqual(idempotence_key, call_context.idempotence_key)

    def test_idempotence_second_request(self):
        """
        Test that the client can successfully handle a response
         indicating a request has been sent prior
        """
        response_body = read_resource("idempotence_success.json")
        idempotence_key = str(uuid.uuid4())
        idempotence_timestamp = str(int(time.time() * 1000))
        call_context = CallContext(idempotence_key)
        request = create_payment_request()
        test_path = "/v1/20000/payments"  # relative url through which the request should be sent
        additional_headers \
            = (("Content-Type", "application/json"),
               ("Location", "http://localhost/v1/20000/payments/000002000020142549460000100001"),
               ("X-GCS-Idempotence-Request-Timestamp", idempotence_timestamp))
        handler = \
            self.create_handler(response_code=201,
                                body=response_body,
                                additional_headers=additional_headers)
        with create_server_listening(handler) as address:
            with create_client(address) as client:
                response = client.merchant("20000").payments().create(request, call_context)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at the wrong path')
        self.assertEqual(idempotence_key, self.idempotence_header,
                         "Wrong idempotence key is sent in the request")
        self.assertEqual(idempotence_key, call_context.idempotence_key)
        self.assertEqual(int(idempotence_timestamp),
                         int(call_context.idempotence_request_timestamp))

    def test_idempotence_first_failure(self):
        """Test a request where a request is rejected without prior requests"""
        response_body = read_resource("idempotence_rejected.json")
        idempotence_key = str(uuid.uuid4())
        call_context = CallContext(idempotence_key)
        request = create_payment_request()
        test_path = "/v1/20000/payments"  # relative url through which the request should be sent
        handler = self.create_handler(response_code=402, body=response_body,
                                      additional_headers=(("Content-Type", "application/json"),))
        with create_server_listening(handler) as address:
            with create_client(address) as client:
                with self.assertRaises(DeclinedPaymentException) as exc:
                    client.merchant("20000").payments().create(request, call_context)
        self.assertEqual(402, exc.exception.status_code)
        self.assertEqual(response_body, exc.exception.response_body)
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at the wrong path')
        self.assertEqual(idempotence_key, self.idempotence_header,
                         "Wrong idempotence key is sent in the request")
        self.assertEqual(idempotence_key, call_context.idempotence_key)
        self.assertIsNone(call_context.idempotence_request_timestamp)

    def test_idempotence_second_failure(self):
        """Test a request where a request is rejected with a prior request"""
        response_body = read_resource("idempotence_rejected.json")
        idempotence_key = str(uuid.uuid4())
        idempotence_timestamp = str(int(time.time() * 1000))
        call_context = CallContext(idempotence_key)
        request = create_payment_request()
        # relative url through which the request should be sent
        test_path = "/v1/20000/payments"
        additional_headers \
            = (("Content-Type", "application/json"),
               ("X-GCS-Idempotence-Request-Timestamp", idempotence_timestamp))
        handler =\
            self.create_handler(response_code=402, body=response_body,
                                additional_headers=additional_headers)
        with create_server_listening(handler) as address:
            with create_client(address) as client:
                with self.assertRaises(DeclinedPaymentException) as exc:
                    client.merchant("20000").payments()\
                        .create(request, call_context)
        self.assertEqual(402, exc.exception.status_code)
        self.assertEqual(response_body, exc.exception.response_body)
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at the wrong path')
        self.assertEqual(idempotence_key, self.idempotence_header,
                         "Wrong idempotence key is sent in the request")
        self.assertEqual(idempotence_key, call_context.idempotence_key)
        self.assertEqual(int(idempotence_timestamp),
                         int(call_context.idempotence_request_timestamp))

    def test_idempotence_duplicate_request(self):
        """Test a request where a request arrived twice"""
        response_body = read_resource("idempotence_duplicate_failure.json")
        idempotence_key = str(uuid.uuid4())
        idempotence_timestamp = str(int(time.time() * 1000))
        call_context = CallContext(idempotence_key)
        request = create_payment_request()
        test_path = "/v1/20000/payments"  # relative url through which the request should be sent
        additional_headers \
            = (("Content-Type", "application/json"),
               ("X-GCS-Idempotence-Request-Timestamp", idempotence_timestamp))
        handler \
            = self.create_handler(response_code=409, body=response_body,
                                  additional_headers=additional_headers)
        with create_server_listening(handler) as address:
            with create_client(address) as client:
                with self.assertRaises(IdempotenceException) as exc:
                    client.merchant("20000").payments().create(request, call_context)
        self.assertEqual(409, exc.exception.status_code)
        self.assertEqual(response_body, exc.exception.response_body)
        self.assertEqual(idempotence_key, exc.exception.idempotence_key)
        self.assertEqual(idempotence_key, self.idempotence_header,
                         "Wrong idempotence key is sent in the request")
        self.assertEqual(idempotence_key, call_context.idempotence_key)
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at the wrong path')
        self.assertEqual(int(idempotence_timestamp),
                         int(call_context.idempotence_request_timestamp))

    def create_handler(self, response_code=200, body='',
                       additional_headers=()):
        """
        Creates a request handler that receives the request on the
         server side

        :param response_code: status code of the desired response
        :param body: the body of the response message to return, it
         should be in json format
        :param additional_headers: additional headers that are added to
         the handler's response
        If the request is sent through the proper path,
         self.request_successful will be set to true, false otherwise
        """
        def handler_func(handler):
            try:
                self.idempotence_header = handler.headers['X-GCS-Idempotence-Key']
                # record if the request was sent through the expected path
                self.request_path = handler.path
                handler.protocol_version = 'HTTP/1.1'
                handler.send_response(response_code)
                for header in additional_headers:
                    handler.send_header(*header)
                handler.send_header('dummy', None)
                handler.send_header('Content-Length', len(bytes(body, "utf-8")))
                handler.end_headers()
                handler.wfile.write(bytes(body, "utf-8"))
            except ConnectionAbortedError:
                pass
        return handler_func


def create_payment_request():
    """Convenience method that creates a payment request"""
    amount_of_money = AmountOfMoney()
    amount_of_money.amount = 2345
    amount_of_money.currency_code = "CAD"
    billing_address = Address()
    billing_address.country_code = "CA"
    customer = Customer()
    customer.billing_address = billing_address
    order = Order()
    order.amount_of_money = amount_of_money
    order.customer = customer
    card = Card()
    card.cvv = "123"
    card.card_number = "4567350000427977"
    card.expiry_date = "1220"
    card_payment_input = CardPaymentMethodSpecificInput()
    card_payment_input.payment_product_id = 1
    card_payment_input.card = card
    body = CreatePaymentRequest()
    body.order = order
    body.card_payment_method_specific_input = card_payment_input
    return body


def read_resource(relative_path):
    return file_utils.read_file(os.path.join("default_implementation",
                                             relative_path))


if __name__ == '__main__':
    unittest.main()
