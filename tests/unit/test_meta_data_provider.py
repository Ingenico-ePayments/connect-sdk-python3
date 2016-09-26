# -*- coding: UTF-8 -*-
import base64
import unittest

from ingenico.connect.sdk.defaultimpl.default_marshaller import DefaultMarshaller
from ingenico.connect.sdk.domain.metadata.shopping_cart_extension import ShoppingCartExtension
from ingenico.connect.sdk.meta_data_provider import MetaDataProvider
from ingenico.connect.sdk.request_header import RequestHeader


class MetaDataProviderTest(unittest.TestCase):
    """Contains tests to check that the meta data provider correctly stores allowed request headers
    and refuses prohibited headers
    """
    def test_server_meta_data_headers_full(self):
        """Tests that the MetaDataProvider can construct meta_data_headers when supplied with a full shopping cart"""
        shopping_cart_extension = ShoppingCartExtension("Ingenico.creator", "Extension", "1.0")
        meta_data_provider = MetaDataProvider("Ingenico", shopping_cart_extension)

        request_headers = meta_data_provider.meta_data_headers
        self.assertEqual(1, len(request_headers))
        self.assertServerMetaInfo(meta_data_provider, "Ingenico", shopping_cart_extension, request_headers[0])

    def test_get_server_metadata_headers_no_additional_headers(self):
        """Tests that the MetaDataProvider functions correctly without any additional headers as arguments"""
        meta_data_provider = MetaDataProvider("Ingenico")

        request_headers = meta_data_provider.meta_data_headers
        self.assertEqual(1, len(request_headers))
        self.assertServerMetaInfo(meta_data_provider, "Ingenico", None, request_headers[0])

    def test_get_server_metadata_headers_additional_headers(self):
        """Tests that the MetaDataProvider can handle multiple additional headers"""
        additional_headers = [RequestHeader("Header1", "&=$%"), RequestHeader("Header2", "blah blah"),
                              RequestHeader("Header3", "foo")]
        meta_data_provider = MetaDataProvider("Ingenico", None, additional_headers)
        request_headers = meta_data_provider.meta_data_headers

        self.assertEqual(4, len(request_headers))

        for index in range(1, 4):
            self.assertEqual(additional_headers[index-1].name, request_headers[index].name)
            self.assertEqual(additional_headers[index-1].value, request_headers[index].value)

    def test_constructor_with_prohibited_headers(self):
        """Tests that the MetaDataProvider constructor does not accept any headers marked as prohibited"""
        for name in MetaDataProvider.prohibited_headers:
            additional_headers = [RequestHeader("Header1", "Value1"),
                                  RequestHeader(name, "should be slashed and burnt"),
                                  RequestHeader("Header3", "Value3")]
            with self.assertRaises(Exception) as error:
                MetaDataProvider("Ingenico", None, additional_headers)
            self.assertIn(name, str(error.exception))

    def assertServerMetaInfo(self, meta_data_provider, integrator, shopping_cart_extension=None, request_header=None):
        """Assert that checks that the request_header is the default header "X-GCS-ServerMetaInfo",
        that the server_meta_data_info of the meta_data_provider is correct
        and that the shopping cart extension is consistent with the extension stored in meta_data_provider
        """
        self.assertEqual("X-GCS-ServerMetaInfo", request_header.name)
        self.assertIsNotNone(request_header.value)

        # server_meta_info is stored in json format and encoded using utf-8 and base64 encoding, decode it
        server_meta_info_json = base64.b64decode(request_header.value).decode('utf-8')
        server_meta_info = DefaultMarshaller.INSTANCE().unmarshal(server_meta_info_json, MetaDataProvider.ServerMetaInfo)
        self.assertEqual(meta_data_provider._platform_identifier, server_meta_info.platform_identifier)
        self.assertEqual(meta_data_provider._sdk_identifier, server_meta_info.sdk_identifier)
        self.assertEqual("Ingenico", server_meta_info.sdk_creator)
        self.assertEqual(integrator, server_meta_info.integrator)
        if shopping_cart_extension is None:
            self.assertIsNone(server_meta_info.shopping_cart_extension)
        else:
            self.assertEqual(shopping_cart_extension.creator, server_meta_info.shopping_cart_extension.creator)
            self.assertEqual(shopping_cart_extension.name, server_meta_info.shopping_cart_extension.name)
            self.assertEqual(shopping_cart_extension.version, server_meta_info.shopping_cart_extension.version)


if __name__ == '__main__':
    unittest.main()
