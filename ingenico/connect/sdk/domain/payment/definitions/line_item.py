#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.payment.definitions.line_item_invoice_data import LineItemInvoiceData
from ingenico.connect.sdk.domain.payment.definitions.line_item_level3_interchange_information import LineItemLevel3InterchangeInformation


class LineItem(DataObject):
    """
    Class LineItem
    See also https://developer.globalcollect.com/documentation/api/server/#schema_LineItem
    
    Attributes:
        amount_of_money:                 :class:`AmountOfMoney`
        invoice_data:                    :class:`LineItemInvoiceData`
        level3_interchange_information:  :class:`LineItemLevel3InterchangeInformation`
     """

    amount_of_money = None
    invoice_data = None
    level3_interchange_information = None

    def to_dictionary(self):
        dictionary = super(LineItem, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountOfMoney', self.amount_of_money)
        self._add_to_dictionary(dictionary, 'invoiceData', self.invoice_data)
        self._add_to_dictionary(dictionary, 'level3InterchangeInformation', self.level3_interchange_information)
        return dictionary

    def from_dictionary(self, dictionary):
        super(LineItem, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'invoiceData' in dictionary:
            if not isinstance(dictionary['invoiceData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['invoiceData']))
            value = LineItemInvoiceData()
            self.invoice_data = value.from_dictionary(dictionary['invoiceData'])
        if 'level3InterchangeInformation' in dictionary:
            if not isinstance(dictionary['level3InterchangeInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['level3InterchangeInformation']))
            value = LineItemLevel3InterchangeInformation()
            self.level3_interchange_information = value.from_dictionary(dictionary['level3InterchangeInformation'])
        return self
