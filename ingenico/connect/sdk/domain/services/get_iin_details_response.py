#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.services.definitions.iin_detail import IINDetail


class GetIINDetailsResponse(DataObject):
    """
    Class GetIINDetailsResponse
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_GetIINDetailsResponse
    """

    __co_brands = None
    __country_code = None
    __is_allowed_in_context = None
    __payment_product_id = None

    @property
    def co_brands(self):
        """
        list[:class:`IINDetail`]
        """
        return self.__co_brands

    @co_brands.setter
    def co_brands(self, value):
        self.__co_brands = value

    @property
    def country_code(self):
        """
        str
        """
        return self.__country_code

    @country_code.setter
    def country_code(self, value):
        self.__country_code = value

    @property
    def is_allowed_in_context(self):
        """
        bool
        """
        return self.__is_allowed_in_context

    @is_allowed_in_context.setter
    def is_allowed_in_context(self, value):
        self.__is_allowed_in_context = value

    @property
    def payment_product_id(self):
        """
        int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    def to_dictionary(self):
        dictionary = super(GetIINDetailsResponse, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'coBrands', self.co_brands)
        self._add_to_dictionary(dictionary, 'countryCode', self.country_code)
        self._add_to_dictionary(dictionary, 'isAllowedInContext', self.is_allowed_in_context)
        self._add_to_dictionary(dictionary, 'paymentProductId', self.payment_product_id)
        return dictionary

    def from_dictionary(self, dictionary):
        super(GetIINDetailsResponse, self).from_dictionary(dictionary)
        if 'coBrands' in dictionary:
            if not isinstance(dictionary['coBrands'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['coBrands']))
            self.co_brands = []
            for coBrands_element in dictionary['coBrands']:
                coBrands_value = IINDetail()
                self.co_brands.append(coBrands_value.from_dictionary(coBrands_element))
        if 'countryCode' in dictionary:
            self.country_code = dictionary['countryCode']
        if 'isAllowedInContext' in dictionary:
            self.is_allowed_in_context = dictionary['isAllowedInContext']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        return self
