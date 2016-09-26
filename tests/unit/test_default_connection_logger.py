import os
import re
import time
import unittest

from requests.exceptions import Timeout

import tests.file_utils as file_utils
from ingenico.connect.sdk.communication_exception import CommunicationException
from ingenico.connect.sdk.declined_payment_exception import DeclinedPaymentException
from ingenico.connect.sdk.domain.definitions.address import Address
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.definitions.card import Card
from ingenico.connect.sdk.domain.payment.create_payment_request import CreatePaymentRequest
from ingenico.connect.sdk.domain.payment.definitions.card_payment_method_specific_input import \
    CardPaymentMethodSpecificInput
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.order import Order
from ingenico.connect.sdk.global_collect_exception import GlobalCollectException
from ingenico.connect.sdk.log.communicator_logger import CommunicatorLogger
from ingenico.connect.sdk.merchant.services.convert_amount_params import ConvertAmountParams
from ingenico.connect.sdk.not_found_exception import NotFoundException
from ingenico.connect.sdk.validation_exception import ValidationException
from tests.unit.server_mock_utils import create_server_listening, create_client


class DefaultConnectionLoggerTest(unittest.TestCase):
    """Tests that services can operate through DefaultConnection and that their network traffic is appropriately logged
    """

    def setUp(self):
        self.request_path = None  # Indicating whether or not a request has arrived at the correct server path
        self.client = None  # Stores the client used in testing so callbacks can reach it

    def test_logging_test_connection(self):
        """Test that a GET service without parameters can connect to a server and is logged appropriately"""
        test_path = "/v1/1234/services/testconnection"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("testConnection.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                client.enable_logging(logger)
                response = client.merchant("1234").services().testconnection()

        self.assertIsNotNone(response)
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual('OK', response.result)
        self.assertEqual(2, len(logger.entries))
        # for request and response, check that the message exists in the logs and there are no errors
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1])
        # for request and response, check that their output is as predicted and that they match each other
        self.assertRequestAndResponse(request_entry[0], response_entry[0], "testConnection")

    def test_logging_convert_amount(self):
        """Test that a GET service with parameters can connect to a server and is logged appropriately"""
        test_path = "/v1/1234/services/convert/amount"  # relative url through which the request should be sent
        logger = TestLogger()

        query_params = ConvertAmountParams()
        query_params.amount = 1000
        query_params.source = "EUR"
        query_params.target = "USD"

        response_body = read_resource("convertAmount.json")
        handler = self.create_handler(body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                client.enable_logging(logger)
                response = client.merchant("1234").services().convertAmount(query_params)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.converted_amount)
        self.assertEqual(test_path, self.request_path.split("?")[0],
                         'Request has arrived at {} instead of {}'.format(self.request_path.split("?")[0], test_path))
        self.assertLogsRequestAndResponse(logger, "convertAmount")

    def test_delete_token(self):
        """Test that a POST service without body and a void response can connect to a server and is logged appropriately
        """
        test_path = "/v1/1234/tokens/5678"  # relative url through which the request should be sent
        logger = TestLogger()

        handler = self.create_handler(response_code=204)
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                client.enable_logging(logger)
                client.merchant("1234").tokens().delete("5678", None)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "deleteToken")

    def test_create_payment(self):
        """Test that a POST service with 201 response can connect to a server and is logged appropriately"""
        test_path = "/v1/1234/payments"  # relative url through which the request should be sent
        logger = TestLogger()

        request = create_payment_request()

        response_body = read_resource("createPayment.json")
        handler = self.create_handler(response_code=201, body=response_body,
                                      additional_headers=(("content-Type", "application/json"),
                                                          ("Location",
                                                           "http://localhost/v1/1234/payments/000000123410000595980000100001"
                                                           )))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                client.enable_logging(logger)
                response = client.merchant("1234").payments().create(request)

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.payment)
        self.assertIsNotNone(response.payment.id)
        self.assertEqual(test_path, self.request_path,
                         'Request has arrived at "{1}" while it should have been delivered to "{0}"'.format(
                             test_path, self.request_path))
        self.assertLogsRequestAndResponse(logger, "createPayment")

    def test_create_payment_invalid_card_number(self):
        """Test that a POST service that is invalid results in an error, which is logged appropriately"""
        test_path = "/v1/1234/payments"  # relative url through which the request should be sent
        logger = TestLogger()

        request = create_payment_request()

        response_body = read_resource("createPayment.failure.invalidCardNumber.json")
        handler = self.create_handler(response_code=400, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                client.enable_logging(logger)
                self.assertRaises(ValidationException, client.merchant("1234").payments().create, request)

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "createPayment_failure_invalidCardNumber")

    def test_create_payment_rejected(self):
        """Test that a POST service that is rejected results in an error, which is logged appropriately"""
        test_path = "/v1/1234/payments"  # relative url through which the request should be sent
        logger = TestLogger()

        request = create_payment_request()

        response_body = read_resource("createPayment.failure.rejected.json")
        handler = self.create_handler(response_code=402, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                client.enable_logging(logger)
                with self.assertRaises(DeclinedPaymentException) as exc:
                    client.merchant("1234").payments().create(request)

        self.assertIsNotNone(exc.exception.create_payment_result)
        self.assertIsNotNone(exc.exception.create_payment_result.payment)
        self.assertIsNotNone(exc.exception.create_payment_result.payment.id)
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "createPayment_failure_rejected")

    def test_logging_unknown_server_error(self):
        """Test that a GET service that results in an error is logged appropriately"""
        test_path = "/v1/1234/services/testconnection"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("unknownServerError.json")
        handler = self.create_handler(response_code=500, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                client.enable_logging(logger)
                with self.assertRaises(GlobalCollectException):
                    client.merchant("1234").services().testconnection()

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "testConnection", "unknownServerError")

    def test_non_json(self):
        """Test that a GET service that results in a not found error is logged appropriately"""
        test_path = "/v1/1234/services/testconnection"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))
        with create_server_listening(handler) as address:  # start server to listen to request
            with create_client(address, connect_timeout=0.500, socket_timeout=0.050) as client:
                client.enable_logging(logger)
                with self.assertRaises(NotFoundException):
                    client.merchant("1234").services().testconnection()

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertLogsRequestAndResponse(logger, "testConnection", "notFound")

    def test_read_timeout(self):
        """Test that if an exception is thrown before log due to a timeout, it is logged"""
        test_path = "/v1/1234/services/testconnection"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))

        def delayed_response(*args, **kwargs):
            time.sleep(0.100)
            handler(*args, **kwargs)

        with create_server_listening(delayed_response) as address:  # start server to listen to request
            with create_client(address, socket_timeout=0.05) as client:  # create client under test
                client.enable_logging(logger)
                with self.assertRaises(CommunicationException):
                    client.merchant("1234").services().testconnection()

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(2, len(logger.entries))
        # for request and response, check that the message exists in the logs and there is an error in the response
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1])
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNotNone(response_entry[1])
        # for request and error, check that their output is as predicted and that they match each other
        self.assertRequestAndError(request_entry[0], response_entry[0], "testConnection")
        self.assertIsInstance(response_entry[1], Timeout, "logger should have logged a timeout error")

    def test_log_request_only(self):
        """Test that a request can be logged separately by disabling log between request and response"""
        test_path = "/v1/1234/services/testconnection"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("testConnection.json")
        handler = self.create_handler(response_code=200, body=response_body,
                                      additional_headers=(('Content-type', 'application/json'),))

        def disable_logging_response(*args, **kwargs):  # handler that disables the log of the client
            self.client.disable_logging()  # before responding
            handler(*args, **kwargs)

        with create_server_listening(disable_logging_response) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                self.client = client
                client.enable_logging(logger)
                response = client.merchant("1234").services().testconnection()

        self.assertEqual("OK", response.result)
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        # check that the request message exists in the logs and there are no errors
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1],
                          "Error '{}' logged that should not have been thrown".format(request_entry[1]))
        # check that the request is formatted correctly
        self.assertRequest(request_entry[0], "testConnection")

    def test_log_response_only(self):
        """Test that a response can be logged separately by enabling log between request and response"""
        test_path = "/v1/1234/services/testconnection"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("testConnection.json")
        handler = self.create_handler(response_code=200, body=response_body,
                                      additional_headers=(("Content-Type", "application/json"),))

        def enable_logging_response(*args, **kwargs):  # handler that enables the log of the client
            self.client.enable_logging(logger)  # before responding
            handler(*args, **kwargs)

        with create_server_listening(enable_logging_response) as address:  # start server to listen to request
            with create_client(address) as client:  # create client under test
                self.client = client
                response = client.merchant("1234").services().testconnection()

        self.assertEqual("OK", response.result)
        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        # check that the response message exists in the logs and there are no errors
        response_entry = logger.entries[0]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1],
                          "Error '{}' logged that should not have been thrown".format(response_entry[1]))
        # check that the response is formatted correctly
        self.assertResponse(response_entry[0], "testConnection")

    def test_log_error_only(self):
        """Test that an error can be logged separately by enabling log between request and response"""
        test_path = "/v1/1234/services/testconnection"  # relative url through which the request should be sent
        logger = TestLogger()

        response_body = read_resource("notFound.html")
        handler = self.create_handler(response_code=404, body=response_body,
                                      additional_headers=(("Content-Type", "text/html"),))

        def enable_logging_late_response(*args, **kwargs):  # handler that enables the log of the client
            self.client.enable_logging(logger)  # and waits for a timeout before responding
            time.sleep(0.1)
            handler(*args, **kwargs)

        with create_server_listening(enable_logging_late_response) as address:  # start server to listen to request
            with create_client(address, connect_timeout=0.500, socket_timeout=0.050) as client:
                self.client = client
                with self.assertRaises(CommunicationException):
                    client.merchant("1234").services().testconnection()

        self.assertEqual(test_path, self.request_path, 'Request has arrived at the wrong path')
        self.assertEqual(1, len(logger.entries))
        # check that the response message exists in the logs and there are no errors
        error_entry = logger.entries[0]
        self.assertIsNotNone(error_entry[0])
        self.assertIsNotNone(error_entry[1])
        # check that the error is formatted correctly
        self.assertError(error_entry[0])
        self.assertIsInstance(error_entry[1], Timeout,
                              "logger should have logged a timeout error, logged {} instead".format(error_entry[1]))

    def assertLogsRequestAndResponse(self, logger, request_resource_prefix, response_resource_prefix=None):
        """Assert that the logs of the logger contain both request and response and no errors,
        then check that the request and response match using "assertRequestAndResponse"
        """
        if response_resource_prefix is None:
            response_resource_prefix = request_resource_prefix
        self.assertEqual(2, len(logger.entries))
        # for request and response, check that the message exists in the logs and there are no errors
        request_entry = logger.entries[0]
        self.assertIsNotNone(request_entry[0])
        self.assertIsNone(request_entry[1],
                          "Error '{}' logged that should not have been thrown".format(request_entry[1]))
        response_entry = logger.entries[1]
        self.assertIsNotNone(response_entry[0])
        self.assertIsNone(response_entry[1],
                          "Error '{}' logged that should not have been thrown".format(response_entry[1]))
        # for request and response, check that their output is as predicted and that they match each other
        self.assertRequestAndResponse(request_entry[0], response_entry[0],
                                      request_resource_prefix, response_resource_prefix)

    def assertRequestAndResponse(self, request_message, response_message,
                                 request_resource_prefix, response_resource_prefix=None):
        """Assert that the request and response messages match the request and response regular expressions stored in
        'request_resource_prefix'.request and 'response_resource_prefix'.response respectively.

        If response_resource_prefix is not given it is assumed to be equal to request_resource_prefix"""
        if response_resource_prefix is None:
            response_resource_prefix = request_resource_prefix
        request_id = self.assertRequest(request_message, request_resource_prefix)
        self.assertResponse(response_message, response_resource_prefix, request_id)

    def assertRequestAndError(self, request_message, error_message, resource_prefix):
        """Assert that the request message matches the request regular expression stored in 'resource_prefix.request'
        and the error is a valid error message and refers to the request"""
        request_id = self.assertRequest(request_message, resource_prefix)
        self.assertError(error_message, request_id)

    def assertRequest(self, request_message, request_resource_prefix):
        """Assert that the request message matches the regex stored in 'request_resource_prefix'.request

        :param request_message: the request message to match
        :param request_resource_prefix: prefix of the regex file location,
        it will be appended with '.request' to obtain the file location
        :return: the request_id for use in matching the corresponding response or error
        """
        request_resource = request_resource_prefix + "_request"
        regex = globals()[request_resource](request_message, self)
        if type(regex) == type(""):
            request_pattern = re.compile(regex, re.DOTALL)
            match = request_pattern.match(request_message.get_message())
            print(globals()[request_resource])
            if match is None:
                raise AssertionError("request message '" + request_message.get_message() +
                                     "' does not match pattern " + str(request_pattern))
            self.assertRegex(request_message, request_pattern)
            return match.group(1)
        return regex[0]

    def assertResponse(self, response_message, response_resource_prefix, request_id=None):
        """Assert that the response message matches the regex stored in 'response_resource_prefix'.response

        :param response_message: the response message to match
        :param response_resource_prefix: prefix of the regex file location,
        it will be appended with '.response' to obtain the file location
        :param request_id: if a request_id is provided, it is matched against the response_id found in the response,
        failing the assert if not equal
        """
        response_resource = response_resource_prefix + "_response"
        # for each response call the corresponding asserting function
        regex = globals()[response_resource](response_message, self)
        if type(regex) == type(""):
            response_pattern = re.compile(regex, re.DOTALL)
            match = response_pattern.match(response_message.get_message())
            if match is None:
                raise AssertionError("response message '" + response_message.get_message() +
                                     "' does not match pattern " + str(response_pattern))
            if request_id is not None:
                self.assertEqual(request_id, match.group(1),
                                 "request_id '{0}' does not match response_id '{1}'".format(request_id, match.group(1)))

    def assertError(self, error_message, request_id=None):
        """Assert that the error message matches the regex stored in 'generic.error'

        :param error_message: the error message to match
        :param request_id: if a request_id is provided, it is matched against the error_id found in the error,
        failing the assert if not equal
        """
        error_resource = "generic_error"
        error_pattern_string = globals()[error_resource]()
        error_pattern = re.compile(error_pattern_string, re.DOTALL)
        match = error_pattern.match(error_message)
        if match is None:
            raise AssertionError("response message '" + error_message +
                                 "' does not match pattern " + str(error_pattern_string))
        if request_id is not None:
            self.assertEqual(request_id, match.group(1),
                             "request_id '{0}' does not match error_id '{1}'".format(request_id, match.group(1)))

    def assertHeaderIn(self, _tuple, _list):
        # If tuple has incorrect number of elements, assume it is not in the list
        self.assertIn((_tuple[0].lower(), _tuple[1]),
                      list(map((lambda el: (el[0].lower(), el[1])), _list)))

    def create_handler(self, response_code=200, body='',  # path='',
                       additional_headers=()):
        """Creates a request handler that receives the request on the server side

        :param response_code: status code of the desired response
        :param body: the body of the response message to return, it should be in json format
        :param additional_headers: additional headers that are added to the handler's response
        If the request is sent through the proper path, self.request_successful will be set to true, false otherwise
        """

        def handler_func(handler):
            self.request_path = handler.path  # record if the request was sent through the expected path
            handler.protocol_version = 'HTTP/1.1'
            try:
                handler.send_response(response_code)
                for header in additional_headers:
                    handler.send_header(*header)
                handler.send_header('Dummy', None)
                handler.send_header('Content-Length', len(bytes(body, "utf-8")))
                handler.end_headers()
                handler.wfile.write(bytes(body, "utf-8"))
            except ConnectionAbortedError:
                pass

        return handler_func


def create_payment_request():
    """Creates a commonly used payment for testing"""
    amount_of_money = AmountOfMoney()
    amount_of_money.currency_code = "CAD"
    amount_of_money.amount = 2345
    billing_address = Address()
    billing_address.country_code = "CA"
    customer = Customer()
    customer.billing_address = billing_address
    order = Order()
    order.amount_of_money = amount_of_money
    order.customer = customer
    card = Card()
    card.cvv = "123"
    card.card_number = "1234567890123456"
    card.expiry_date = "1220"
    payment_specific_input = CardPaymentMethodSpecificInput()
    payment_specific_input.payment_product_id = 1
    payment_specific_input.card = card
    request = CreatePaymentRequest()
    request.order = order
    request.card_payment_method_specific_input = payment_specific_input
    return request


class TestLogger(CommunicatorLogger):
    def __init__(self):
        CommunicatorLogger.__init__(self)
        self.entries = []

    def log_request(self, request_log_message):
        self.entries.append((request_log_message, None))

    def log_response(self, response_log_message):
        self.entries.append((response_log_message, None))

    def log(self, message, thrown=None):
        self.entries.append((message, thrown))


def replace_all_java_regex():
    r"""Script to convert all \Q \E java regex pattern files used by this test to python equivalent"""
    replace_java_regex("convertAmount.request")
    replace_java_regex("convertAmount.response")
    replace_java_regex("createPayment.failure.invalidCardNumber.request")
    replace_java_regex("createPayment.failure.invalidCardNumber.response")
    replace_java_regex("createPayment.failure.rejected.request")
    replace_java_regex("createPayment.failure.rejected.response")
    replace_java_regex("createPayment.request")
    replace_java_regex("createPayment.response")
    replace_java_regex("deleteToken.request")
    replace_java_regex("deleteToken.response")
    replace_java_regex("generic.error")
    replace_java_regex("notFound.response")
    replace_java_regex("testConnection.request")
    replace_java_regex("testConnection.response")
    replace_java_regex("unknownServerError.response")


def replace_java_regex(relative_path):
    r"""Reads a source file containing java regex patterns and writes it back in python regex.

    Recognises: \Qxxx\E as literal content xxx
    """
    result = ""
    text = read_resource(relative_path)
    substrings = re.split(r"\\Q|\\E", text)
    # even substrings now contain regular expressions and odd substrings are to be escaped because they should be quoted
    for i, substring in enumerate(substrings):
        if i % 2 == 0:
            result += substring
        if i % 2 == 1:
            result += re.escape(substring)
    file_utils.write_file(os.path.join("default_implementation", relative_path), result)


# reads a file names file_name stored under resources/default_implementation
def read_resource(file_name): return file_utils.read_file(os.path.join("default_implementation", file_name))


# ------------------------ REGEX SOURCES ------------------


def convertAmount_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/v1/1234/services/convert/amount?source=EUR&amount=1000&target=USD')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))

    test.assertIsNone(request.body)

    return request.request_id, False


def convertAmount_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def createPayment_failure_invalidCardNumber_request(request, test):
    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/v1/1234/payments')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)

    # Note: originaly 'application/json; charset=UTF-8', but I think that was a Java specific thing
    test.assertEqual(request.content_type, 'application/json')

    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))

    return request.request_id, False


def createPayment_failure_invalidCardNumber_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 400)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def createPayment_failure_rejected_request(request, test):

    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/v1/1234/payments')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)

    # Note: originaly 'application/json; charset=UTF-8', but I think that was a Java specific thing
    test.assertEqual(request.content_type, 'application/json')

    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))

    return request.request_id, False

def createPayment_failure_rejected_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 402)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False

def createPayment_request_test():
    return re.compile(r"""^  headers:[ ]+Connection.*$""", re.M)


def createPayment_request(request, test):
    test.assertEqual(request.method, "POST")
    test.assertEqual(request.uri, '/v1/1234/payments')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)

    # Note: originaly 'application/json; charset=UTF-8', but I think that was a Java specific thing
    test.assertEqual(request.content_type, 'application/json')

    test.assertIsNotNone(request.body)
    test.assertTrue(len(request.body))

    return request.request_id, False

def createPayment_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 201)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertHeaderIn(('Location', '"http://localhost/v1/1234/payments/000000123410000595980000100001"'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False

def deleteToken_request(request, test):
    test.assertEqual(request.method, "DELETE")
    test.assertEqual(request.uri, '/v1/1234/tokens/5678')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))

    return request.request_id, False


def deleteToken_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 204)
    test.assertIsNone(response.content_type)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNone(response.body)
    return response.request_id, False


def generic_error():
    return r"""Error\ occurred\ for\ outgoing\ request\ \(requestId\=\'([-a-zA-Z0-9]+)\'\,\ \d\.\d+\ s\)"""


def notFound_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 404)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"text/html"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'text/html')
    test.assertIsNotNone(response.body)
    test.assertEqual(response.body, "Not Found")
    return response.request_id, False

def testConnection_request(request, test):
    test.assertEqual(request.method, "GET")
    test.assertEqual(request.uri, '/v1/1234/services/testconnection')

    headers = request.get_header_list()
    test.assertHeaderIn(('Authorization', '"********"'), headers)
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertTrue(len(list(filter((lambda header: header[0] == 'X-GCS-ServerMetaInfo'), headers))))

    return request.request_id, False


def testConnection_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 200)
    test.assertEqual(response.content_type, 'application/json')
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False


def unknownServerError_response(response, test):
    test.assertIsNotNone(response.get_duration())
    test.assertEqual(response.get_status_code(), 500)
    headers = response.get_header_list()
    test.assertTrue(len(list(filter((lambda header: header[0] == 'Date'), headers))))
    test.assertHeaderIn(('Content-Type', '"application/json"'), headers)
    test.assertHeaderIn(('Dummy', '""'), headers)
    test.assertEqual(response.content_type, 'application/json')
    test.assertIsNotNone(response.body)
    test.assertTrue(len(response.body))
    return response.request_id, False

if __name__ == '__main__':
    unittest.main()
