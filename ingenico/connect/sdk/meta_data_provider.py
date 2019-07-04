import platform
from base64 import b64encode
import re

from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.defaultimpl.default_marshaller import \
    DefaultMarshaller
from ingenico.connect.sdk.domain.metadata.shopping_cart_extension import ShoppingCartExtension
from .request_header import RequestHeader


class IterProperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func(owner)


class MetaDataProvider:
    """
    Provides meta info about the server.
    """
    __SDK_VERSION = "3.1.0"
    __SERVER_META_INFO_HEADER = "X-GCS-ServerMetaInfo"
    __prohibited_headers = [__SERVER_META_INFO_HEADER, "X-GCS-Idempotence-Key",
                            "Date", "Content-Type", "Authorization"]
    __PROHIBITED_HEADERS = tuple(sorted(__prohibited_headers, key=str.lower))
    __meta_data_headers = None

    class ServerMetaInfo(DataObject):
        platform_identifier = None
        sdk_identifier = None
        sdk_creator = None
        integrator = None
        shopping_cart_extension = None

        def to_dictionary(self):
            dictionary = super(MetaDataProvider.ServerMetaInfo, self).to_dictionary()
            if self.platform_identifier is not None:
                dictionary['platformIdentifier'] = self.platform_identifier
            if self.sdk_identifier is not None:
                dictionary['sdkIdentifier'] = self.sdk_identifier
            if self.sdk_creator is not None:
                dictionary['sdkCreator'] = self.sdk_creator
            if self.integrator is not None:
                dictionary['integrator'] = self.integrator
            if self.shopping_cart_extension is not None:
                dictionary['shoppingCartExtension'] = self.shopping_cart_extension.to_dictionary()
            return dictionary

        def from_dictionary(self, dictionary):
            super(MetaDataProvider.ServerMetaInfo, self).from_dictionary(dictionary)
            if 'platformIdentifier' in dictionary:
                self.platform_identifier = dictionary['platformIdentifier']
            if 'sdkIdentifier' in dictionary:
                self.sdk_identifier = dictionary['sdkIdentifier']
            if 'sdkCreator' in dictionary:
                self.sdk_creator = dictionary['sdkCreator']
            if 'integrator' in dictionary:
                self.integrator = dictionary['integrator']
            if 'shoppingCartExtension' in dictionary:
                if not isinstance(dictionary['shoppingCartExtension'], dict):
                    raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['shoppingCartExtension']))
                self.shopping_cart_extension = ShoppingCartExtension.create_from_dictionary(dictionary['shoppingCartExtension'])
            return self

    def __init__(self, integrator, shopping_cart_extension=None,
                 additional_request_headers=()):
        MetaDataProvider.__validate_additional_request_headers(
            additional_request_headers)

        def subber(name_or_value):
            return re.sub(r'\r?\n(?:(?![\r\n])\s)*', " ", name_or_value).strip()
        additional_request_headers = [RequestHeader(subber(header.name), subber(header.value))
                                      for header in additional_request_headers]

        server_meta_info = self.ServerMetaInfo()
        server_meta_info.platform_identifier = self._platform_identifier
        server_meta_info.sdk_identifier = self._sdk_identifier
        server_meta_info.sdk_creator = "Ingenico"
        server_meta_info.integrator = integrator
        server_meta_info.shopping_cart_extension = shopping_cart_extension

        server_meta_info_string = DefaultMarshaller.INSTANCE().marshal(
            server_meta_info)
        server_meta_info_header = RequestHeader(
            self.__SERVER_META_INFO_HEADER, b64encode(
                server_meta_info_string.encode('utf-8')))
        if not additional_request_headers:
            self.__meta_data_headers = tuple([server_meta_info_header])
        else:
            request_headers = [server_meta_info_header]
            request_headers.extend(additional_request_headers)
            self.__meta_data_headers = tuple(request_headers)

    @staticmethod
    def __validate_additional_request_headers(additional_request_headers):
        if additional_request_headers is not None:
            for additional_request_header in additional_request_headers:
                MetaDataProvider.__validate_additional_request_header(
                    additional_request_header)

    @staticmethod
    def __validate_additional_request_header(additional_request_header):
        try:
            if additional_request_header.name in MetaDataProvider.__PROHIBITED_HEADERS:
                raise ValueError("request header not allowed: ",
                                 str(additional_request_header))
        except AttributeError:
            raise AttributeError("Each request header should have an attribute 'name' and an attribute 'value'")

    @IterProperty
    def prohibited_headers(self):
        return self.__PROHIBITED_HEADERS

    @property
    def meta_data_headers(self):
        """
        :return: The server related headers containing the META data to be
         associated with the request (if any). This will always contain at least
         an automatically generated header X-GCS-ServerMetaInfo.
        """
        return self.__meta_data_headers

    @property
    def _platform_identifier(self):
        return platform.system() + " " + platform.release() + "/" + \
               platform.version() + " Python/" + platform.python_version() + \
               " (" + platform.python_implementation() + "; " + \
               str(platform.python_compiler()) + ")"

    @property
    def _sdk_identifier(self):
        return "Python3ServerSDK/v" + self.__SDK_VERSION
