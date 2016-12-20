#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject


class LineItemInvoiceData(DataObject):
    """
    Class LineItemInvoiceData
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_LineItemInvoiceData
    """

    __description = None
    __merchant_linenumber = None
    __merchant_pagenumber = None
    __nr_of_items = None
    __price_per_item = None

    @property
    def description(self):
        """
        str
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def merchant_linenumber(self):
        """
        str
        """
        return self.__merchant_linenumber

    @merchant_linenumber.setter
    def merchant_linenumber(self, value):
        self.__merchant_linenumber = value

    @property
    def merchant_pagenumber(self):
        """
        str
        """
        return self.__merchant_pagenumber

    @merchant_pagenumber.setter
    def merchant_pagenumber(self, value):
        self.__merchant_pagenumber = value

    @property
    def nr_of_items(self):
        """
        str
        """
        return self.__nr_of_items

    @nr_of_items.setter
    def nr_of_items(self, value):
        self.__nr_of_items = value

    @property
    def price_per_item(self):
        """
        int
        """
        return self.__price_per_item

    @price_per_item.setter
    def price_per_item(self, value):
        self.__price_per_item = value

    def to_dictionary(self):
        dictionary = super(LineItemInvoiceData, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'description', self.description)
        self._add_to_dictionary(dictionary, 'merchantLinenumber', self.merchant_linenumber)
        self._add_to_dictionary(dictionary, 'merchantPagenumber', self.merchant_pagenumber)
        self._add_to_dictionary(dictionary, 'nrOfItems', self.nr_of_items)
        self._add_to_dictionary(dictionary, 'pricePerItem', self.price_per_item)
        return dictionary

    def from_dictionary(self, dictionary):
        super(LineItemInvoiceData, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        if 'merchantLinenumber' in dictionary:
            self.merchant_linenumber = dictionary['merchantLinenumber']
        if 'merchantPagenumber' in dictionary:
            self.merchant_pagenumber = dictionary['merchantPagenumber']
        if 'nrOfItems' in dictionary:
            self.nr_of_items = dictionary['nrOfItems']
        if 'pricePerItem' in dictionary:
            self.price_per_item = dictionary['pricePerItem']
        return self
