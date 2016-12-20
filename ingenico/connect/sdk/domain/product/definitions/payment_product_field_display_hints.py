#
# This class was auto-generated from the API references found at
# https://developer.globalcollect.com/documentation/api/server/
#
from ingenico.connect.sdk.data_object import DataObject
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_form_element import PaymentProductFieldFormElement
from ingenico.connect.sdk.domain.product.definitions.payment_product_field_tooltip import PaymentProductFieldTooltip


class PaymentProductFieldDisplayHints(DataObject):
    """
    Class PaymentProductFieldDisplayHints
    
    See also https://developer.globalcollect.com/documentation/api/server/#schema_PaymentProductFieldDisplayHints
    """

    __always_show = None
    __display_order = None
    __form_element = None
    __label = None
    __mask = None
    __obfuscate = None
    __placeholder_label = None
    __preferred_input_type = None
    __tooltip = None

    @property
    def always_show(self):
        """
        bool
        """
        return self.__always_show

    @always_show.setter
    def always_show(self, value):
        self.__always_show = value

    @property
    def display_order(self):
        """
        int
        """
        return self.__display_order

    @display_order.setter
    def display_order(self, value):
        self.__display_order = value

    @property
    def form_element(self):
        """
        :class:`PaymentProductFieldFormElement`
        """
        return self.__form_element

    @form_element.setter
    def form_element(self, value):
        self.__form_element = value

    @property
    def label(self):
        """
        str
        """
        return self.__label

    @label.setter
    def label(self, value):
        self.__label = value

    @property
    def mask(self):
        """
        str
        """
        return self.__mask

    @mask.setter
    def mask(self, value):
        self.__mask = value

    @property
    def obfuscate(self):
        """
        bool
        """
        return self.__obfuscate

    @obfuscate.setter
    def obfuscate(self, value):
        self.__obfuscate = value

    @property
    def placeholder_label(self):
        """
        str
        """
        return self.__placeholder_label

    @placeholder_label.setter
    def placeholder_label(self, value):
        self.__placeholder_label = value

    @property
    def preferred_input_type(self):
        """
        str
        """
        return self.__preferred_input_type

    @preferred_input_type.setter
    def preferred_input_type(self, value):
        self.__preferred_input_type = value

    @property
    def tooltip(self):
        """
        :class:`PaymentProductFieldTooltip`
        """
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value):
        self.__tooltip = value

    def to_dictionary(self):
        dictionary = super(PaymentProductFieldDisplayHints, self).to_dictionary()
        self._add_to_dictionary(dictionary, 'alwaysShow', self.always_show)
        self._add_to_dictionary(dictionary, 'displayOrder', self.display_order)
        self._add_to_dictionary(dictionary, 'formElement', self.form_element)
        self._add_to_dictionary(dictionary, 'label', self.label)
        self._add_to_dictionary(dictionary, 'mask', self.mask)
        self._add_to_dictionary(dictionary, 'obfuscate', self.obfuscate)
        self._add_to_dictionary(dictionary, 'placeholderLabel', self.placeholder_label)
        self._add_to_dictionary(dictionary, 'preferredInputType', self.preferred_input_type)
        self._add_to_dictionary(dictionary, 'tooltip', self.tooltip)
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProductFieldDisplayHints, self).from_dictionary(dictionary)
        if 'alwaysShow' in dictionary:
            self.always_show = dictionary['alwaysShow']
        if 'displayOrder' in dictionary:
            self.display_order = dictionary['displayOrder']
        if 'formElement' in dictionary:
            if not isinstance(dictionary['formElement'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['formElement']))
            value = PaymentProductFieldFormElement()
            self.form_element = value.from_dictionary(dictionary['formElement'])
        if 'label' in dictionary:
            self.label = dictionary['label']
        if 'mask' in dictionary:
            self.mask = dictionary['mask']
        if 'obfuscate' in dictionary:
            self.obfuscate = dictionary['obfuscate']
        if 'placeholderLabel' in dictionary:
            self.placeholder_label = dictionary['placeholderLabel']
        if 'preferredInputType' in dictionary:
            self.preferred_input_type = dictionary['preferredInputType']
        if 'tooltip' in dictionary:
            if not isinstance(dictionary['tooltip'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['tooltip']))
            value = PaymentProductFieldTooltip()
            self.tooltip = value.from_dictionary(dictionary['tooltip'])
        return self
