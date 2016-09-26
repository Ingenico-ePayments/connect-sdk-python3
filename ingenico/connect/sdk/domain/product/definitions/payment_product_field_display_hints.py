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
    
    Attributes:
        always_show:           bool
        display_order:         int
        form_element:          :class:`PaymentProductFieldFormElement`
        label:                 str
        mask:                  str
        obfuscate:             bool
        placeholder_label:     str
        preferred_input_type:  str
        tooltip:               :class:`PaymentProductFieldTooltip`
     """

    always_show = None
    display_order = None
    form_element = None
    label = None
    mask = None
    obfuscate = None
    placeholder_label = None
    preferred_input_type = None
    tooltip = None

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
