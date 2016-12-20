#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.refund.definitions.bank_refund_method_specific_input import BankRefundMethodSpecificInput
from ingenico.connect.sdk.domain.refund.definitions.refund_customer import RefundCustomer
from ingenico.connect.sdk.domain.refund.definitions.refund_references import RefundReferences


class RefundRequest(DataObject):
    """
    Class RefundRequest
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_RefundRequest
    """

    __amount_of_money = None
    __bank_refund_method_specific_input = None
    __customer = None
    __refund_date = None
    __refund_references = None

    @property
    def amount_of_money(self):
        """
        :class:`AmountOfMoney`
        """
        return self.__amount_of_money

    @amount_of_money.setter
    def amount_of_money(self, value):
        self.__amount_of_money = value

    @property
    def bank_refund_method_specific_input(self):
        """
        :class:`BankRefundMethodSpecificInput`
        """
        return self.__bank_refund_method_specific_input

    @bank_refund_method_specific_input.setter
    def bank_refund_method_specific_input(self, value):
        self.__bank_refund_method_specific_input = value

    @property
    def customer(self):
        """
        :class:`RefundCustomer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def refund_date(self):
        """
        str
        """
        return self.__refund_date

    @refund_date.setter
    def refund_date(self, value):
        self.__refund_date = value

    @property
    def refund_references(self):
        """
        :class:`RefundReferences`
        """
        return self.__refund_references

    @refund_references.setter
    def refund_references(self, value):
        self.__refund_references = value

    def to_dictionary(self):
        dictionary = super(RefundRequest, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'amountOfMoney', self.amount_of_money)
        self._add_to_dictionary(dictionary, 'bankRefundMethodSpecificInput', self.bank_refund_method_specific_input)
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'refundDate', self.refund_date)
        self._add_to_dictionary(dictionary, 'refundReferences', self.refund_references)
        return dictionary

    def from_dictionary(self, dictionary):
        super(RefundRequest, self).from_dictionary(dictionary)
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'bankRefundMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['bankRefundMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankRefundMethodSpecificInput']))
            value = BankRefundMethodSpecificInput()
            self.bank_refund_method_specific_input = value.from_dictionary(dictionary['bankRefundMethodSpecificInput'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = RefundCustomer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'refundDate' in dictionary:
            self.refund_date = dictionary['refundDate']
        if 'refundReferences' in dictionary:
            if not isinstance(dictionary['refundReferences'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['refundReferences']))
            value = RefundReferences()
            self.refund_references = value.from_dictionary(dictionary['refundReferences'])
        return self
