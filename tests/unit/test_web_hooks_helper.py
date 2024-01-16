import unittest
import uuid
from tests import file_utils
import os

from mockito import *

from ingenico.connect.sdk.domain.webhooks.web_hooks_event import WebhooksEvent
from ingenico.connect.sdk.marshaller import Marshaller
from ingenico.connect.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from ingenico.connect.sdk.request_header import RequestHeader
from ingenico.connect.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from ingenico.connect.sdk.webhooks.secret_key_not_available_exception import SecretKeyNotAvailableException
from ingenico.connect.sdk.webhooks.web_hooks_helper import WebhooksHelper
from ingenico.connect.sdk.webhooks.signature_validation_exception import SignatureValidationException
from ingenico.connect.sdk.webhooks.api_version_mismatch_exception import ApiVersionMismatchException


class WebhooksHelperTest(unittest.TestCase):
    __SIGNATURE_HEADER = "X-GCS-Signature"
    __SIGNATURE = "2S7doBj/GnJnacIjSJzr5fxGM5xmfQyFAwxv1I53ZEk="
    __KEY_ID_HEADER = "X-GCS-KeyId"
    __KEY_ID = "dummy-key-id"
    __SECRET_KEY = "hello+world"
    connection = None

    @staticmethod
    def clear_public_key_cache():
        InMemorySecretKeyStore.INSTANCE().clear()

    def test_unmarshal_api_version_mismatch(self):
        marshaller = mock(Marshaller)
        event = WebhooksEvent()
        event.api_version = "v0"
        body = self.__read_resource("valid-body")
        # raise Exception(event)
        when(marshaller).unmarshal(body.decode('utf-8'), WebhooksEvent).thenReturn(event)
        helper = self.__create_helper(marshaller)
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)
        ]
        self.assertRaises(ApiVersionMismatchException, helper.unmarshal, body, request_headers)

    def test_unmarshal_no_secret_key_available(self):
        self.clear_public_key_cache()
        helper = self.__create_helper()
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)
        ]
        self.assertRaises(SecretKeyNotAvailableException, helper.unmarshal, body, request_headers)

    def test_unmarshal_missing_headers(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, ())

    def test_unmarshal_duplicate_headers(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID),
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE + "1")
        ]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, request_headers)

    def test_unmarshal_string_success(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)
        ]
        event = helper.unmarshal(body, request_headers)
        self.assertEqual("v1", event.api_version)
        self.assertEqual("8ee793f6-4553-4749-85dc-f2ef095c5ab0", event.id)
        self.assertEqual("2017-02-02T11:24:14.040+0100", event.created)
        self.assertEqual("20000", event.merchant_id)
        self.assertEqual("payment.paid", event.type)

        self.assertIsNone(event.refund)
        self.assertIsNone(event.payout)
        self.assertIsNone(event.token)

        self.assertIsNotNone(event.payment)
        self.assertEqual("00000200000143570012", event.payment.id)
        self.assertIsNotNone(event.payment.payment_output)
        self.assertIsNotNone(event.payment.payment_output.amount_of_money)
        self.assertEqual(1000, event.payment.payment_output.amount_of_money.amount)
        self.assertEqual("EUR", event.payment.payment_output.amount_of_money.currency_code)
        self.assertIsNotNone(event.payment.payment_output.amount_of_money.currency_code)
        self.assertIsNotNone(event.payment.payment_output.references)
        self.assertEqual("200001681810", event.payment.payment_output.references.payment_reference)
        self.assertEqual("bankTransfer", event.payment.payment_output.payment_method)

        self.assertIsNone(event.payment.payment_output.card_payment_method_specific_output)
        self.assertIsNone(event.payment.payment_output.cash_payment_method_specific_output)
        self.assertIsNone(event.payment.payment_output.direct_debit_payment_method_specific_output)
        self.assertIsNone(event.payment.payment_output.invoice_payment_method_specific_output)
        self.assertIsNone(event.payment.payment_output.redirect_payment_method_specific_output)
        self.assertIsNone(event.payment.payment_output.sepa_direct_debit_payment_method_specific_output)
        self.assertIsNotNone(event.payment.payment_output.bank_transfer_payment_method_specific_output)
        self.assertEqual(11, event.payment.payment_output.bank_transfer_payment_method_specific_output.payment_product_id)

        self.assertEqual("PAID", event.payment.status)
        self.assertIsNotNone(event.payment.status_output)
        self.assertEqual(False, event.payment.status_output.is_cancellable)
        self.assertEqual("COMPLETED", event.payment.status_output.status_category)
        self.assertEqual(1000, event.payment.status_output.status_code)
        self.assertEqual("20170202112414", event.payment.status_output.status_code_change_date_time)
        self.assertEqual(True, event.payment.status_output.is_authorized)

    def test_unmarshal_string_invalid_body(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)

        body = self.__read_resource("invalid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)
        ]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, request_headers)

    def test_unmarshal_string_invalid_secret_key(self):
        helper = self.__create_helper()
        invalid_secret_key = "1" + self.__SECRET_KEY
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, invalid_secret_key)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)
        ]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, request_headers)

    def test_unmarshal_string_invalid_signature(self):
        helper = self.__create_helper()
        InMemorySecretKeyStore.INSTANCE().store_secret_key(self.__KEY_ID, self.__SECRET_KEY)
        body = self.__read_resource("valid-body")
        request_headers = [
            RequestHeader(self.__SIGNATURE_HEADER, "1" + self.__SIGNATURE),
            RequestHeader(self.__KEY_ID_HEADER, self.__KEY_ID)
        ]
        self.assertRaises(SignatureValidationException, helper.unmarshal, body, request_headers)

    @staticmethod
    def __read_resource(resource):
        output = file_utils.read_file(os.path.join("webhooks", resource))
        output = output.replace("\r", "")
        return str.encode(output)

    def test_are_equal_signatures_equal(self):
        signature = str(uuid.uuid4())
        large = self.__repeat(signature, 100)
        self.assertTrue(WebhooksHelper.are_equal_signatures(signature, signature))
        self.assertTrue(WebhooksHelper.are_equal_signatures(large, large))

    def test_are_equal_signatures_not_equal(self):
        signature = str(uuid.uuid4())
        large = self.__repeat(signature, 100)
        self.assertFalse(WebhooksHelper.are_equal_signatures("abc", signature))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature, "abc"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature, signature + "1"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature + "1", signature))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature.lower(), signature.upper()))
        self.assertFalse(WebhooksHelper.are_equal_signatures(signature.upper(), signature.lower()))

        self.assertFalse(WebhooksHelper.are_equal_signatures("abc", large))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large, "abc"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large + "1", large))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large, large + "1"))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large.lower(), large.upper()))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large.upper(), large.lower()))

        self.assertFalse(WebhooksHelper.are_equal_signatures(signature, large))
        self.assertFalse(WebhooksHelper.are_equal_signatures(large, signature))

    @staticmethod
    def __repeat(s, times):
        return s * times

    @staticmethod
    def __create_helper(marshaller=DefaultMarshaller.INSTANCE()):
        return WebhooksHelper(marshaller, InMemorySecretKeyStore.INSTANCE())

    if __name__ == '__main__':
        unittest.main()
