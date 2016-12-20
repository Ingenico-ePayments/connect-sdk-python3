#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.definitions.amount_of_money import AmountOfMoney
from ingenico.connect.sdk.domain.payment.definitions.additional_order_input import AdditionalOrderInput
from ingenico.connect.sdk.domain.payment.definitions.customer import Customer
from ingenico.connect.sdk.domain.payment.definitions.line_item import LineItem
from ingenico.connect.sdk.domain.payment.definitions.order_references import OrderReferences


class Order(DataObject):
    """
    Class Order
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_Order
    """

    __additional_input = None
    __amount_of_money = None
    __customer = None
    __items = None
    __references = None

    @property
    def additional_input(self):
        """
        :class:`AdditionalOrderInput`
        """
        return self.__additional_input

    @additional_input.setter
    def additional_input(self, value):
        self.__additional_input = value

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
    def customer(self):
        """
        :class:`Customer`
        """
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def items(self):
        """
        list[:class:`LineItem`]
        """
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    @property
    def references(self):
        """
        :class:`OrderReferences`
        """
        return self.__references

    @references.setter
    def references(self, value):
        self.__references = value

    def to_dictionary(self):
        dictionary = super(Order, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'additionalInput', self.additional_input)
        self._add_to_dictionary(dictionary, 'amountOfMoney', self.amount_of_money)
        self._add_to_dictionary(dictionary, 'customer', self.customer)
        self._add_to_dictionary(dictionary, 'items', self.items)
        self._add_to_dictionary(dictionary, 'references', self.references)
        return dictionary

    def from_dictionary(self, dictionary):
        super(Order, self).from_dictionary(dictionary)
        if 'additionalInput' in dictionary:
            if not isinstance(dictionary['additionalInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['additionalInput']))
            value = AdditionalOrderInput()
            self.additional_input = value.from_dictionary(dictionary['additionalInput'])
        if 'amountOfMoney' in dictionary:
            if not isinstance(dictionary['amountOfMoney'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['amountOfMoney']))
            value = AmountOfMoney()
            self.amount_of_money = value.from_dictionary(dictionary['amountOfMoney'])
        if 'customer' in dictionary:
            if not isinstance(dictionary['customer'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['customer']))
            value = Customer()
            self.customer = value.from_dictionary(dictionary['customer'])
        if 'items' in dictionary:
            if not isinstance(dictionary['items'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['items']))
            self.items = []
            for items_element in dictionary['items']:
                items_value = LineItem()
                self.items.append(items_value.from_dictionary(items_element))
        if 'references' in dictionary:
            if not isinstance(dictionary['references'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['references']))
            value = OrderReferences()
            self.references = value.from_dictionary(dictionary['references'])
        return self
